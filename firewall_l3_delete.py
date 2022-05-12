import meraki

org_id="1045047"

dashboard = meraki.DashboardAPI(suppress_logging=True)

networks=dashboard.organizations.getOrganizationNetworks(org_id)

for network in networks:
    print(f"Removing all rules from {network['name']}")
    l3_rules=dashboard.appliance.updateNetworkApplianceFirewallL3FirewallRules(network["id"],rules=[])
