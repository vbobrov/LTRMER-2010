import texttable
import meraki

dns_servers=["1.1.1.1","4.2.2.2","9.9.9.9"]

new_rules=[]

for dns_server in dns_servers:
    new_rules.append({
            "comment": f"Block UDP {dns_server}",
            "policy": "deny",
            "protocol": "udp",
            "srcPort": "Any",
            "srcCidr": "Any",
            "destPort": "53",
            "destCidr": "8.8.8.8/32",
            "syslogEnabled": False
        }
    )
    new_rules.append({
            "comment": f"Block TCP {dns_server}",
            "policy": "deny",
            "protocol": "tcp",
            "srcPort": "Any",
            "srcCidr": "Any",
            "destPort": "53",
            "destCidr": "8.8.8.8/32",
            "syslogEnabled": False
        }
    )

org_id="1045047"

dashboard = meraki.DashboardAPI(suppress_logging=True)

networks=dashboard.organizations.getOrganizationNetworks(org_id)

for network in networks:
    print(f"Processing {network['name']}")
    l3_rules=dashboard.appliance.getNetworkApplianceFirewallL3FirewallRules(network["id"])
    #remove the last Default rule
    l3_rules["rules"].pop()
    #prepend the rules
    l3_rules=dashboard.appliance.updateNetworkApplianceFirewallL3FirewallRules(network["id"],rules=new_rules+l3_rules["rules"])
    firewall_table=texttable.Texttable(max_width=0)
    firewall_table.header(["Policy","Protocol","Src","Src Port","Dst","Dst Port","Comment"])
    for rule in l3_rules["rules"]:
        firewall_table.add_row([rule["policy"],rule["protocol"],rule["srcCidr"],rule["srcPort"],rule["destCidr"],rule["destPort"],rule["comment"]])
    print(firewall_table.draw())
