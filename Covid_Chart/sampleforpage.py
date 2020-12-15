

# Use the following command to
# install requierd modules
# pip install covid
# pip install matplotlib


import matplotlib.pyplot as plt
from covid import Covid

covid = Covid()
TotalActiveCases = covid.get_total_active_cases()
TotalDeathsCases = covid.get_total_deaths()
TotalRecoveredCases = covid.get_total_recovered()

CovidStatusList = [TotalActiveCases,
                   TotalDeathsCases,
                   TotalRecoveredCases]

CovidStatusListLabels = ["Total Active Cases",
                         "Total Deaths Cases",
                         "Total Recovered Cases"]

pieChartColors = ["Yellow", "DarkRed", "LightGreen"]

explodedDistince = [0.1, 0.1, 0.1]

plt.pie(CovidStatusList, labels=CovidStatusListLabels,
        explode=explodedDistince, colors=pieChartColors, 
        shadow=True)

plt.show()
