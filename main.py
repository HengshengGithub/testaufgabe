# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from day_temp import max_min_day # import max_min_day function for plot hottest and coldest days of each year


# laod date from file temperatures.csv
df = pd.read_csv('temperatures.csv')


# convert the timesteps of the temperature data to 15 min. intervals
for k in range(0, (len(df['Wert'])*4-3), 4):
    for i in range(k+1, k+4):
        insertRow = pd.DataFrame([['TT_TU_MN009', 2014, df['Zeitstempel'][i-1]+15, np.nan, np.nan, np.nan]], columns=['Produkt_Code', 'SDO_ID', 'Zeitstempel', 'Wert', 'Qualitaet_Niveau', 'Qualitaet_Byte'])
        above = df.loc[:i-1]
        below = df.loc[i:]
        df = above.append(insertRow, ignore_index=True).append(below, ignore_index=True)
        # Using double for-loop here, so it run a litte slowly
        
df['Wert'].interpolate(method='linear', limit_direction='forward', axis=0, inplace=True)    # Using linear interpolation for temperature
df['Qualitaet_Niveau'].interpolate(method='nearest', limit_direction='forward', axis=0, inplace=True)   # Using nearest interpolation for temperature
df['Qualitaet_Byte'].interpolate(method='nearest', limit_direction='forward', axis=0, inplace=True)     # Using nearest interpolation for temperature

df.to_csv('Temp_timesteps.csv')   # save csv file for new timesteps (with 15 min timesteps)


# Find the hottest and coldest tempertures for every year
#for 2015
index_15 = df[df['Zeitstempel'].values ==201601010000].index[0]-1       # create index
hottest_15 = df['Wert'][:index_15].max()
hottest_15_data = df['Zeitstempel'][df['Wert'][:index_15].idxmax()]
coldest_15 = df['Wert'][:index_15].min()
coldest_15_data = df['Zeitstempel'][df['Wert'][:index_15].idxmin()]

#for 2016
index_16_start = df[df['Zeitstempel'].values ==201601010000].index[0]
index_16_end   = df[df['Zeitstempel'].values ==201701010000].index[0]-1
hottest_16 = df['Wert'][index_16_start:index_16_end].max()
hottest_16_data = df['Zeitstempel'][df['Wert'][index_16_start:index_16_end].idxmax()]
coldest_16 = df['Wert'][index_16_start:index_16_end].min()
coldest_16_data = df['Zeitstempel'][df['Wert'][index_16_start:index_16_end].idxmin()]

#for 2017
index_17_start = df[df['Zeitstempel'].values ==201701010000].index[0]
index_17_end = df[df['Zeitstempel'].values ==201801010000].index[0]-1
hottest_17 = df['Wert'][index_17_start:index_17_end].max()
hottest_17_data = df['Zeitstempel'][df['Wert'][index_17_start:index_17_end].idxmax()]
coldest_17 = df['Wert'][index_17_start:index_17_end].min()
coldest_17_data = df['Zeitstempel'][df['Wert'][index_17_start:index_17_end].idxmin()]

#for 2018
index_18_start = df[df['Zeitstempel'].values ==201801010000].index[0]
index_18_end = df[df['Zeitstempel'].values ==201901010000].index[0]-1
hottest_18 = df['Wert'][index_18_start:index_18_end].max()
hottest_18_data = df['Zeitstempel'][df['Wert'][index_18_start:index_18_end].idxmax()]
coldest_18 = df['Wert'][index_18_start:index_18_end].min()
coldest_18_data = df['Zeitstempel'][df['Wert'][index_18_start:index_18_end].idxmin()]

#for 2019
index_19_start = df[df['Zeitstempel'].values ==201901010000].index[0]
index_19_end = df[df['Zeitstempel'].values ==202001010000].index[0]-1
hottest_19 = df['Wert'][index_19_start:index_19_end].max()
hottest_19_data = df['Zeitstempel'][df['Wert'][index_19_start:index_19_end].idxmax()]
coldest_19 = df['Wert'][index_19_start:index_19_end].min()
coldest_19_data = df['Zeitstempel'][df['Wert'][index_19_start:index_19_end].idxmin()]

#for 2020
index_20 = df[df['Zeitstempel'].values ==202001010000].index[0]
hottest_20 = df['Wert'][index_20:].max()
hottest_20_data = df['Zeitstempel'][df['Wert'][index_20:].idxmax()]
coldest_20 = df['Wert'][index_20:].min()
coldest_20_data = df['Zeitstempel'][df['Wert'][index_20:].idxmin()]



# function for save csv file
df_Temp = pd.DataFrame({'hottest_temp': pd.Series([hottest_15, hottest_16, hottest_17, hottest_18, hottest_19, hottest_20], 
                                               index=[2015, 2016, 2017, 2018, 2019, 2020]),
                     'hottest_data': pd.Series([hottest_15_data, hottest_16_data, hottest_17_data, hottest_18_data, hottest_19_data, hottest_20_data],
                                               index=[2015, 2016, 2017, 2018, 2019, 2020]),
                     'coldest_temp': pd.Series([coldest_15, coldest_16, coldest_17, coldest_18, coldest_19, coldest_20], 
                                               index=[2015, 2016, 2017, 2018, 2019, 2020]),
                     'coldest_data':pd.Series([coldest_15_data, coldest_16_data, coldest_17_data, coldest_18_data, coldest_19_data, coldest_20_data], 
                                               index=[2015, 2016, 2017, 2018, 2019, 2020])
                    })      # create DataFrame for save

df_Temp.to_csv("Temp_statistics.csv")       # save csv



# plot hottest and coldest days of each year
max_min_day(df)



# one more analysis
# average temperatur for each year

mean_T_15 = np.mean(df['Wert'][:index_15])
mean_T_16 = np.mean(df['Wert'][index_16_start:index_16_end])
mean_T_17 = np.mean(df['Wert'][index_17_start:index_17_end])
mean_T_18 = np.mean(df['Wert'][index_18_start:index_18_end])
mean_T_19 = np.mean(df['Wert'][index_19_start:index_19_end])
mean_T_20 = np.mean(df['Wert'][index_20:])

#plot the average temperatur for each year
x = [2015, 2016, 2017, 2018, 2019, '2020*']
y = [mean_T_15, mean_T_16, mean_T_17, mean_T_18, mean_T_19, mean_T_20]
plt.plot(x, y, marker='^')
plt.title('average temperatur for each year')
plt.text(0,5.8,'*for 2020: until 25022020', size = 7)
plt.show()


        
        

        

        
        













