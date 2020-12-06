# -*- coding: utf-8 -*-
# @Time : 2020/11/30 20:06 
# @Author : Jason
# @File : data_Refreshing重庆.py 
# @Software: PyCharm

import sys
import pandas as pd
# import my method from another py file
sys.path.append('C:\\Users\\dcdn\\PycharmProjects\\untitled\\中津产教融合\\数据清洗')
import data_Refreshing_module as drm

# batch process for all csv files and return the combined df
df = drm.batch_process_csv(r'C:\Users\dcdn\Desktop\重庆市')

# output first round, assign their city code manually
df.to_csv('C:/Users/dcdn/Desktop/重庆_Result_raw.csv', encoding="utf_8_sig")

# -----------------------------------------
# the code above and below will be processed respectively
# -----------------------------------------

# # since we miss the city name and city code, so manual processes are get those two data
# # read processed csv file back as a df
# new_df = pd.read_csv('C:/Users/dcdn/Desktop/重庆_Result_raw.csv')
#
# # the new file already has city code, so we have rank them
# new_df = drm.rank_city_code(new_df)
#
# # fill the missing value as required
# new_df = drm.missing_data_filling(new_df)
#
# # then the data is complete, output get csv file or excel file
# new_df.to_csv('C:/Users/dcdn/Desktop/重庆_Result_Finished.csv', encoding="utf_8_sig")
