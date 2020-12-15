from covid import Covid
import matplotlib.pyplot as plt

covid = Covid()
# cases = covid.get_status_by_country_name("us")
# cases = covid.get_data()
TotalActiveCases = covid.get_total_active_cases()
# TotalConfirmedCases = covid.get_total_confirmed_cases()
TotalDeathsCases = covid.get_total_deaths()
TotalRecoveredCases = covid.get_total_recovered()
CovidStatusList = [TotalActiveCases, TotalDeathsCases, TotalRecoveredCases]
mylabels = ["Total Active Cases",
            "Total Deaths Cases", "Total Recovered Cases"]
mycolors = ["y", "r", "g"]
myexplode = [0.1, 0.1, 0.1]

# print(CovidStatusList,"\n",mylabels,"\n",myexplode)

# print("TotalConfirmedCases: ", TotalConfirmedCases)
# print("TotalActiveCases: ", TotalActiveCases)
# print("TotalDeathsCases: ", TotalDeathsCases)
# print("TotalRecoveredCases: ", TotalRecoveredCases)
plt.pie(CovidStatusList, labels=mylabels,
        explode=myexplode, colors=mycolors, shadow=True)
plt.legend(title="Covid-19 Status:")
plt.show()


# print(cases)
# for x in cases:
#     print(x, ":", cases[x])
