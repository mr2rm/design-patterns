from kpi_data import KPI_Data

# Report on current KPI values
# TODO: report in other ways (e.g. email, REST API)
# TODO: add new KPI

for kpi in KPI_Data:
    if kpi.name == 'open':
        print(f'Current open tickets: {kpi.value}')
    elif kpi.name == 'new':
        print(f'New tickets in last hour: {kpi.value}')
    elif kpi.name == 'closed':
        print(f'Tickets closed in last hour: {kpi.value}')
