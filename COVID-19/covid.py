import pandas as pd
import matplotlib.pyplot as plt

cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
deaths_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

cases = pd.read_csv(cases_url)
deaths = pd.read_csv(deaths_url)

cases.drop(cases.columns[[0,2,3]], axis=1, inplace=True)
idxKorea = cases[cases['Country/Region'] == 'Korea, South'].index[0]
cases.at[idxKorea,'Country/Region'] = 'South Korea'
cases.set_index('Country/Region')
cases = cases.groupby('Country/Region').sum()
cases.columns = pd.to_datetime(cases.columns)

#print(cases)

deaths.drop(deaths.columns[[0,2,3]], axis=1, inplace=True)
idxKorea = deaths[deaths['Country/Region'] == 'Korea, South'].index[0]
deaths.at[idxKorea,'Country/Region'] = 'South Korea'
deaths.set_index('Country/Region')
deaths = deaths.groupby('Country/Region').sum()
deaths.columns = pd.to_datetime(deaths.columns)

#print(deaths)

def worldwide_cases(data):

    column_names = list(data.columns)
    total_cases_latest = data[column_names[len(column_names)-1]].sum()
    worldwide_cases_over_time = []

    for i in range(0,len(column_names)):
        worldwide_cases_over_time.append(data[column_names[i]].sum())

    print("Number of Worldwide Cases:",len(worldwide_cases_over_time))
    print("Number of dates:",len(column_names))

    print(total_cases_latest)
    print(data.tail(40))

    plt.plot(column_names,worldwide_cases_over_time)
    plt.show()


#worldwide_cases(cases)

def worldwide_cases_simpler(data):
    
    data.loc['Total'] = data.sum()
    print(data)
    
    data.loc['Total'].plot()
    
    scale = input("Do you want a linear or log scale? ")
    plt.legend(loc="upper left")
    plt.ylabel("World cumulative cases over time")
    plt.yscale(scale)
    plt.show()

#worldwide_cases_simpler(cases)

def plot_countries(data):

    number_to_plot = int(input("How many countries do you want to plot? "))
    
    #countries_to_plot = []
    
    for i in range(0,number_to_plot):
        country_to_plot = input("Enter a country: ")
        data.loc[country_to_plot].plot()
    
    scale = input("Do you want a linear or log scale? ")
    
    plt.legend(loc="upper left")
    plt.ylabel("Cumulative cases over time")
    plt.yscale(scale)
    plt.show()
        

#plot_countries(cases)

def top_ten_daily(data):

    #print(list(data.columns))
    date = input("Choose a date to see top 10 by country (format: yyyy-mm-dd): ")
    
    top_10 = data.sort_values(by = date, ascending = False)[[date]].copy()
    print(top_10.head(10))

def snapshot(data,country="none"):

    first_date = input("Choose a starting date for the range: ")
    second_date = input("Choose an ending date for the range: ")
    if second_date < first_date:
        print("Error: date range specified is invalid")
    else:
        if country != "none":
            snapshot = data.loc[:,first_date:second_date].copy()
            print(snapshot.loc[[country]])
        else:
            snapshot = data.loc[:,first_date:second_date].copy()
            print(snapshot)

def snapshot_by_country(data):

    country = input("Choose a country: ")
    snapshot(data,country)
    

type = input("What dataset would you like to see?\n Cases\n Deaths\n")

df = None
if type == "Cases":
    df = cases
    print(cases)
elif type == "Deaths":
    df = deaths
    print(deaths)
else:
    print("Invalid dataset")

task = input("What do you want to do with the data?\n Plot worldwide cumulative totals\n Plot individual country cumulative totals\n Look at a snapshot of all countries\n Look at a snapshot of one country\n")


#snapshot_by_country(cases)
#top_ten_daily(cases)
#top_ten_daily(deaths)
