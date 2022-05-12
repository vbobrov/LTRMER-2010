import texttable
import meraki
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-n",metavar="<networkId>",required=True)
args=parser.parse_args()

dashboard = meraki.DashboardAPI(suppress_logging=True)

shaping_rules=dashboard.appliance.getNetworkApplianceTrafficShapingRules(args.n)

shaping_table=texttable.Texttable(max_width=0)
shaping_table.header(["Definition","Limits","Priority","DSCP"])

if shaping_rules["defaultRulesEnabled"]:
    print("Default Rules are enabled")
else:
    print("Default Rules ae disabled")

for rule in shaping_rules["rules"]:
    definitions=[]
    for definition in rule["definitions"]:
        if "application" in definition["type"]:
            definitions.append(definition["value"]["name"])
        else:
            definitions.append(definition["value"])
    shaping_table.add_row(["\n".join(definitions),f"Up: {rule['perClientBandwidthLimits']['bandwidthLimits']['limitUp']} KB/s\nDown: {rule['perClientBandwidthLimits']['bandwidthLimits']['limitDown']} KB/s",rule["priority"],"Unchanged" if rule["dscpTagValue"] is None else rule["dscpTagValue"]])

print(shaping_table.draw())