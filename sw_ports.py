import texttable
import meraki
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-s",metavar="<serial>",required=True)
args=parser.parse_args()

dashboard = meraki.DashboardAPI(suppress_logging=True)

switch_ports=dashboard.switch.getDeviceSwitchPortsStatuses(args.s)

port_table=texttable.Texttable(max_width=0)
port_table.header(["Port","Status","Speed","Duplex","CDP","LLDP"])

for port in switch_ports:
    port_table.add_row([port["portId"],port["status"],port["speed"],port["duplex"],port["cdp"]["platform"] if "cdp" in port else "",port["lldp"]["systemName"] if "lldp" in port else ""])

print(port_table.draw())