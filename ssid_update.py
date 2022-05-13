import meraki
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-n",metavar="<networkId>",help="Meraki Network ID",required=True)
parser.add_argument("-s",metavar="<ssid>",help="SSID Name",required=True)
parser.add_argument("-i",metavar="<ssidnum>",help="SSID Number",type=int,required=True)
parser.add_argument("-r",metavar="<radiusip>",help="RADIUS Server IP",required=True)
parser.add_argument("-k",metavar="<radiuskey>",help="RADIUS Server Secret",required=True)
parser.add_argument("-d",help="Disable SSID",action="store_true",default=False)

args=parser.parse_args()

dashboard = meraki.DashboardAPI(suppress_logging=True)

dashboard.wireless.updateNetworkWirelessSsid(
    args.n,
    args.i,
    name=args.s,
    enabled=not args.d,
    authMode="8021x-radius",
    encryptionMode="wpa",
    wpaEncryptionMode="WPA1 and WPA2",
    splashPage="Cisco ISE",
    radiusServers=[
        {
            "host": args.r,
            "port": 1812,
            "secret": args.k
        }
    ],
    radiusAccountingServers=[
        {
            "host": args.r,
            "port": 1813,
            "secret": args.k
        }
    ],
    radiusCoaEnabled=True
)
print("SSID Updated Successfully")