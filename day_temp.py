# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def max_min_day(df):
    y = 365
    # hottest for every year
    T_max_15 = -100
    for j in range(0, y):
        hottest_15_T = np.mean(df['Wert'][j*96: j*96+95])
        if hottest_15_T > T_max_15:
            T_max_15 = hottest_15_T
            
    T_max_16 = -100
    for j in range(y, 2*y+1):
        hottest_16_T = np.mean(df['Wert'][j*96: j*96+95])
        if hottest_16_T > T_max_16:
            T_max_16 = hottest_16_T
            
    T_max_17 = -100
    for j in range(2*y+1, 3*y+1):
        hottest_17_T = np.mean(df['Wert'][j*96: j*96+95])
        if hottest_17_T > T_max_17:
            T_max_17 = hottest_17_T
            
    T_max_18 = -100
    for j in range(3*y+1, 4*y+1):
        hottest_18_T = np.mean(df['Wert'][j*96: j*96+95])
        if hottest_18_T > T_max_18:
            T_max_18 = hottest_18_T
            
    T_max_19 = -100
    for j in range(4*y+1, 5*y+1):
        hottest_19_T = np.mean(df['Wert'][j*96: j*96+95])
        if hottest_19_T > T_max_19:
            T_max_19 = hottest_19_T
            
    T_max_20 = -100
    for j in range(5*y+1, 5*y+56):
        hottest_20_T = np.mean(df['Wert'][j*96: j*96+95])
        if hottest_20_T > T_max_20:
            T_max_20 = hottest_20_T
            
    
    # coldest for every year
    T_min_15 = 100
    for j in range(0, y):
        coldest_15_T = np.mean(df['Wert'][j*96: j*96+95])
        if coldest_15_T < T_min_15:
            T_min_15 = coldest_15_T
            
    T_min_16 = 100
    for j in range(y, 2*y+1):
        coldest_16_T = np.mean(df['Wert'][j*96: j*96+95])
        if coldest_16_T < T_min_16:
            T_min_16 = coldest_16_T
            
    T_min_17 = 100
    for j in range(2*y+1, 3*y+1):
        coldest_17_T = np.mean(df['Wert'][j*96: j*96+95])
        if coldest_17_T < T_min_17:
            T_min_17 = coldest_17_T
            
    T_min_18 = 100
    for j in range(3*y+1, 4*y+1):
        coldest_18_T = np.mean(df['Wert'][j*96: j*96+95])
        if coldest_18_T < T_min_18:
            T_min_18 = coldest_18_T
            
    T_min_19 = 100
    for j in range(4*y+1, 5*y+1):
        coldest_19_T = np.mean(df['Wert'][j*96: j*96+95])
        if coldest_19_T < T_min_19:
            T_min_19 = coldest_19_T
            
    T_min_20 = 100
    for j in range(5*y+1, 5*y+56):
        coldest_20_T = np.mean(df['Wert'][j*96: j*96+95])
        if coldest_20_T < T_min_20:
            T_min_20 = coldest_20_T
            
    # plot        
    x = [2015, 2016, 2017, 2018, 2019, '2020*']
    y1 = [T_max_15, T_max_16, T_max_17, T_max_18, T_max_19, T_max_20]
    y2 = [T_min_15, T_min_16, T_min_17, T_min_18, T_min_19, T_min_20]
    plt.plot(x, y1, color='r', marker='^', label='T_max')
    plt.plot(x, y2, color='b', marker='s', label='T_min')
    plt.legend(loc = 'center right')
    plt.title('Temperatures for the hottest and coldest days of each year')
    plt.text(0,-10,'*for 2020: until 25022020', size = 7)
    plt.show()
    
            
            



