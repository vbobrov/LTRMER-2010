import texttable
import meraki

dashboard = meraki.DashboardAPI(suppress_logging=True)

org_list=dashboard.organizations.getOrganizations()

org_table=texttable.Texttable()
org_table.set_cols_dtype(["i","t"])
org_table.add_row(["id","name"])

for org in org_list:
    org_table.add_row([org['id'],org['name']])

print(org_table.draw())