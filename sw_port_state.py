import meraki
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-s",metavar="<serial>",help="Switch serial number",required=True)
status_group=parser.add_mutually_exclusive_group(required=True)
status_group.add_argument("-e",metavar="<portId",type=int,help="Enable switch port")
status_group.add_argument("-d",metavar="<portId",type=int,help="Disable switch port")
args=parser.parse_args()

dashboard = meraki.DashboardAPI(suppress_logging=True)

if args.e:
    dashboard.switch.updateDeviceSwitchPort(args.s,args.e,enabled=True)
else:
    dashboard.switch.updateDeviceSwitchPort(args.s,args.d,enabled=False)

