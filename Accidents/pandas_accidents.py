import pandas as pd

data = pd.read_csv("Accidents7904.csv", low_memory=False)

# print("total rows: {0}".format(len(data)))
# print(list(data))

print("\nAccidents")
print("-----------")

accidents_sunday = data[data.Day_of_Week == 1]
accidents_sunday_20_plus_cars = data[(data.Day_of_Week == 1) & (data.Number_of_Vehicles > 20)]
accidents_sunday_20_plus_cars_rain = data[(data.Day_of_Week == 1) & (data.Number_of_Vehicles > 20) & (data.Weather_Conditions == 2)]

print("Accidents which happened on a Sunday: {0}".format(len(accidents_sunday)))
print("Accidents which happened on a Sunday involving >20 cars: {0}".format(len(accidents_sunday_20_plus_cars)))
print("Accidents which happened on a Sunday involving >20 cars in the rain: {0}".format(len(accidents_sunday_20_plus_cars_rain)))

london_data = data[data['Police_Force'] == 1 & (data.Day_of_Week == 1)]
london_data_2000 = london_data[(pd.to_datetime(london_data['Date']) > pd.to_datetime('2000-01-01')) & (pd.to_datetime(london_data['Date']) < pd.to_datetime('2000-12-31'))]

print("Accidents in London in the year 2000 on a Sunday: {0}".format(len(london_data_2000)))

london_data_2000.to_csv('AccidentsModified.csv')