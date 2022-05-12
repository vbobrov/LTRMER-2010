import texttable
import meraki
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-n",metavar="<networkId>",required=True)
args=parser.parse_args()

dashboard = meraki.DashboardAPI(suppress_logging=True)

ssids=dashboard.wireless.getNetworkWirelessSsids(args.n)

ssid_table=texttable.Texttable(max_width=0)
ssid_table.header(["#","Name","Status","Auth","Radius Servers","Encryption","Mode"])

for ssid in ssids:
    if "open" in ssid["authMode"]:
        encryption="N/A"
        encryption_mode="N/A"
    else:
        encryption=ssid["encryptionMode"]
        encryption_mode=ssid["wpaEncryptionMode"]
    
    if "radius" in ssid["authMode"]:
        radius_servers=[]
        for server in ssid["radiusServers"]:
            radius_servers.append(f"{server['host']}:{server['port']}")
    else:
        radius_servers=["N/A"]

    ssid_table.add_row([ssid["number"],ssid["name"],"Enabled" if ssid["enabled"] else "disabled",ssid["authMode"],"\n".join(radius_servers),encryption,encryption_mode])

print(ssid_table.draw())