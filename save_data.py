# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

def save_show_data():
    from main import hottest_15, hottest_16, hottest_17, hottest_18, hottest_19, hottest_20
    from main import hottest_15_data, hottest_16_data, hottest_17_data, hottest_18_data, hottest_19_data, hottest_20_data
    from main import coldest_15, coldest_16, coldest_17, coldest_18, coldest_19, coldest_20
    from main import coldest_15_data, coldest_16_data, coldest_17_data, coldest_18_data, coldest_19_data, coldest_20_data
    df_Temp = pd.DataFrame({'hottest_temp': pd.Series([hottest_15, hottest_16, hottest_17, hottest_18, hottest_19, hottest_20], 
                                                   index=[2015, 2016, 2017, 2018, 2019, 2020]),
                         'hottest_data': pd.Series([hottest_15_data, hottest_16_data, hottest_17_data, hottest_18_data, hottest_19_data, hottest_20_data],
                                                   index=[2015, 2016, 2017, 2018, 2019, 2020]),
                         'coldest_temp': pd.Series([coldest_15, coldest_16, coldest_17, coldest_18, coldest_19, coldest_20], 
                                                   index=[2015, 2016, 2017, 2018, 2019, 2020]),
                         'coldest_data':pd.Series([coldest_15_data, coldest_16_data, coldest_17_data, coldest_18_data, coldest_19_data, coldest_20_data], 
                                                   index=[2015, 2016, 2017, 2018, 2019, 2020])
                        })
    
    df_Temp.to_csv("Temp_statistics.csv")
    
    return df_Temp


