import texttable
import meraki
import argparse

parser=argparse.ArgumentParser()
status_group=parser.add_mutually_exclusive_group(required=True)
status_group.add_argument("-e",metavar="<description>",help="Enable matching switch ports")
status_group.add_argument("-d",metavar="<description>",help="Disable matching switch ports")
args=parser.parse_args()

if args.e:
    enable_ports=True
    action="Enable"
    description=args.e
else:
    enable_ports=False
    action="Disable"
    description=args.d

dashboard = meraki.DashboardAPI(suppress_logging=True)

org_id="1045047"

port_table=texttable.Texttable(max_width=0)

port_table.header(["Switch","Serial","Port"])

devices=dashboard.organizations.getOrganizationDevices(org_id)

port_actions=[]
for device in devices:
    if device["productType"]=="switch":
        switch_ports=dashboard.switch.getDeviceSwitchPorts(device["serial"])
        for port in switch_ports:
            if port["name"]==description:
                port_actions.append({
                    "resource": f"/devices/{device['serial']}/switch/ports/{port['portId']}",
                    "operation": "update",
                    "body": {
                        "enabled": enable_ports
                    }
                })
                port_table.add_row([device["name"],device["serial"],port["portId"]])

if port_actions:
    print(port_table.draw())
    confirm=input(f"{action} listed ports? (y/[n]): ")
    if confirm=="y":
        dashboard.organizations.createOrganizationActionBatch(org_id,port_actions,confirmed=True,synchronous=True)
        print("Ports updated")
    else:
        print("Action canceled")
else:
    print("No ports found")