from kpis import KPIs
from currentkpis import CurrentKPIs
from forecastkpis import ForecastKPIs

# Report on current KPI values

# Without "Context Manager"
"""
kpis = KPIs()
currentKPIs = CurrentKPIs(kpis)
forecastKPIs = ForecastKPIs(kpis)
kpis.set_kpis(25, 10, 5)
kpis.set_kpis(100, 50, 30)
kpis.set_kpis(50, 10, 20)

print('\n***Detaching the currentKPIs observer.***\n\n')
kpis.detach(currentKPIs)
kpis.set_kpis(150, 110, 120)
"""

# With "Context Manager"
with KPIs() as kpis:
    with CurrentKPIs(kpis), ForecastKPIs(kpis):
        kpis.set_kpis(25, 10, 5)
        kpis.set_kpis(100, 50, 30)
        kpis.set_kpis(50, 10, 20)

print('\n***Exited context managers.***\n\n')
kpis.set_kpis(150, 110, 120)
