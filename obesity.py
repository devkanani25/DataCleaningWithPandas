import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.ExcelFile("obes-phys-acti-diet-eng-2015-tab.xlsx")

print(data.sheet_names) # prints the names of the Excel sheets

def obesity_by_agegroup():
    data_age = data.parse(u'7.2', skiprows=3, skipfooter=14) # parses data from sheet 7.2, skipping the first 3 rows and last 14 rows

    # removes unnecessary columns
    data_age.drop('Unnamed: 1', axis=1, inplace=True)
    data_age.drop(data_age.index[0], inplace=True)

    data_age.set_index('Year', inplace=True) # sets 'Year' as the index
    
    data_age = data_age.iloc[::-1] # reverses the DataFrame as Year was originally in descending order, but ascending needed

    print(data_age) # prints the DataFrame

    data_age_minus_total = data_age.drop('Total', axis=1) # drops the 'Total' column as it's unnecessary

    # plots and displays the DataFrame
    # data_age_minus_total.plot()
    # plt.show()

    print("\nChart a graph of the above data")
    agegroup = input("Enter an Age Group to compare with Under 16's or type 'all' to see every age group: ")
    if agegroup == 'all':
        data_age_minus_total.plot()
        plt.show()
    else:
        # compares age groups 'Under 16' and '35-44'
        data_age_minus_total[agegroup].plot(label=agegroup)
        data_age_minus_total['Under 16'].plot(label="Under 16")
        plt.legend(loc="upper left")
        plt.ylabel('FAE with primary diagnosis of obesity')
        plt.show()
     
    return data_age_minus_total

def obesity_by_gender():
    data_gender = data.parse(u'7.1', skiprows=3, skipfooter=14)
    
    data_gender.at[1, 'Year'] = '2013/14'
    data_gender.at[2, 'Year'] = '2012/13'
    data_gender.at[8, 'Year'] = '2006/07'
       
    data_gender.drop('Unnamed: 1', axis=1, inplace=True)
    data_gender.drop(data_gender.index[0], inplace=True)
    
    data_gender.set_index('Year', inplace=True)
    data_gender = data_gender.iloc[::-1]
        
    print(data_gender)
    
    data_gender_minus_total = data_gender.drop('Total', axis=1, inplace=True)
    
    gender_array = ['Male','Female','Unknown']
    
    print("\nChart a graph of the above data")
    gender = input("Enter a gender (Male/Female/Unknown): ")
    data_gender[gender].plot(label=gender)
    second_gender = input("Enter another gender (Male/Female/Unknown) or type 'No' if you don't want a second gender: ")
    if (second_gender in gender_array):
        data_gender[second_gender].plot(label=second_gender)
    plt.legend(loc="upper left")
    plt.ylabel('FAE with primary diagnosis of obesity')
    plt.show()
    

obesity_by_agegroup_predict(obesity_by_agegroup())

#choice = input("See Obesity by Age (A) or Gender (G)? ")
#if choice == 'A':
#    obesity_by_agegroup()
#elif choice == 'G':
#    obesity_by_gender()

