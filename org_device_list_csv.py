import meraki
import csv
import sys

dashboard = meraki.DashboardAPI(suppress_logging=True)

org_id="355279"

networks=dashboard.organizations.getOrganizationNetworks(org_id)
network_lookup={network["id"]:network["name"] for network in networks}

devices=dashboard.organizations.getOrganizationDevices(org_id)

device_csv=csv.writer(sys.stdout)

device_csv.writerow(["network","name","model","serial","ip"])

for device in devices:
    try:
        ip=device["lanIp"]
    except KeyError:
        try:
            ip=device["wan1Ip"]
        except KeyError:
            ip="N/A"
    device_csv.writerow([network_lookup[device["networkId"]],device["name"],device["model"],device["serial"],ip])
