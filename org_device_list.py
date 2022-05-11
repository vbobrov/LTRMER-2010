import texttable
import meraki

dashboard = meraki.DashboardAPI(suppress_logging=True)

org_id="1045047"

networks=dashboard.organizations.getOrganizationNetworks(org_id)
network_lookup={network["id"]:network["name"] for network in networks}

devices=dashboard.organizations.getOrganizationDevices(org_id)

device_table=texttable.Texttable(max_width=0)
#org_table.set_cols_dtype(["i","t"])
device_table.header(["network","name","model","serial","ip"])

for device in devices:
    try:
        ip=device["lanIp"]
    except KeyError:
        try:
            ip=device["wan1Ip"]
        except KeyError:
            ip="N/A"
    device_table.add_row([network_lookup[device["networkId"]],device["name"],device["model"],device["serial"],ip])

print(device_table.draw())