# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from save_data import save_show_data


# laod date from file temperatures.csv
df = pd.read_csv('temperatures.csv')


for k in range(0, (len(df['Wert'])*4-3), 4):
    for i in range(k+1, k+4):
        insertRow = pd.DataFrame([['TT_TU_MN009', 2014, df['Zeitstempel'][i-1]+15, np.nan, np.nan, np.nan]], columns=['Produkt_Code', 'SDO_ID', 'Zeitstempel', 'Wert', 'Qualitaet_Niveau', 'Qualitaet_Byte'])
        above = df.loc[:i-1]
        below = df.loc[i:]
        df = above.append(insertRow, ignore_index=True).append(below, ignore_index=True)
        
df['Wert'].interpolate(method='linear', limit_direction='forward', axis=0, inplace=True)
df['Qualitaet_Niveau'].interpolate(method='nearest', limit_direction='forward', axis=0, inplace=True)
df['Qualitaet_Byte'].interpolate(method='nearest', limit_direction='forward', axis=0, inplace=True)



# Find the hottest and coldest tempertures for everyear
index_15 = df[df['Zeitstempel'].values ==201601010000].index[0]-1
hottest_15 = df['Wert'][:index_15].max()
hottest_15_data = df['Zeitstempel'][df['Wert'][:index_15].idxmax()]
coldest_15 = df['Wert'][:index_15].min()
coldest_15_data = df['Zeitstempel'][df['Wert'][:index_15].idxmin()]

index_16_start = df[df['Zeitstempel'].values ==201601010000].index[0]
index_16_end   = df[df['Zeitstempel'].values ==201701010000].index[0]-1
hottest_16 = df['Wert'][index_16_start:index_16_end].max()
hottest_16_data = df['Zeitstempel'][df['Wert'][index_16_start:index_16_end].idxmax()]
coldest_16 = df['Wert'][index_16_start:index_16_end].min()
coldest_16_data = df['Zeitstempel'][df['Wert'][index_16_start:index_16_end].idxmin()]

index_17_start = df[df['Zeitstempel'].values ==201701010000].index[0]
index_17_end = df[df['Zeitstempel'].values ==201801010000].index[0]-1
hottest_17 = df['Wert'][index_17_start:index_17_end].max()
hottest_17_data = df['Zeitstempel'][df['Wert'][index_17_start:index_17_end].idxmax()]
coldest_17 = df['Wert'][index_17_start:index_17_end].min()
coldest_17_data = df['Zeitstempel'][df['Wert'][index_17_start:index_17_end].idxmin()]

index_18_start = df[df['Zeitstempel'].values ==201801010000].index[0]
index_18_end = df[df['Zeitstempel'].values ==201901010000].index[0]-1
hottest_18 = df['Wert'][index_18_start:index_18_end].max()
hottest_18_data = df['Zeitstempel'][df['Wert'][index_18_start:index_18_end].idxmax()]
coldest_18 = df['Wert'][index_18_start:index_18_end].min()
coldest_18_data = df['Zeitstempel'][df['Wert'][index_18_start:index_18_end].idxmin()]

index_19_start = df[df['Zeitstempel'].values ==201901010000].index[0]
index_19_end = df[df['Zeitstempel'].values ==202001010000].index[0]-1
hottest_19 = df['Wert'][index_19_start:index_19_end].max()
hottest_19_data = df['Zeitstempel'][df['Wert'][index_19_start:index_19_end].idxmax()]
coldest_19 = df['Wert'][index_19_start:index_19_end].min()
coldest_19_data = df['Zeitstempel'][df['Wert'][index_19_start:index_19_end].idxmin()]

index_20 = df[df['Zeitstempel'].values ==202001010000].index[0]
hottest_20 = df['Wert'][index_20:].max()
hottest_20_data = df['Zeitstempel'][df['Wert'][index_20:].idxmax()]
coldest_20 = df['Wert'][index_20:].min()
coldest_20_data = df['Zeitstempel'][df['Wert'][index_20:].idxmin()]



# function for save csv file
df_Temp = save_show_data()

'''
for j in range(0, 365):
    test_15_T = np.mean(df['Wert'][0: 95])
    T_max = -100
    if test_15_T > T_max:
        T_max = test_15_T
    else:
        continue
'''











