# -*- coding: utf-8 -*-
# @Time : 2020/11/28 14:49 
# @Author : Jason
# @File : data_Refreshing_module.py
# @Software: PyCharm

import math
import pandas as pd
import os

# 合并两个excel表的内容，且仅保留df1的区域列
def combine_two_datafame(df1, df2):
    len_Column1 = df1.shape[1]  # 返回df1的列数
    result = pd.concat([df1, df2], axis=1)
    # pd.concat是合并俩df，但是把区域重复合并了，下面进行删除操作
    result = result.drop(result.columns[[len_Column1]], axis=1)
    # 一个问题是drop后两个district的列都被drop了，那么原本解决方法应该是先保存一列district然后在接上去
    # 但是由于该数据的格式，可以导出重新复制一遍，没必要再写
    return result

# 批量处理所有csv文件，并使用combine_two_dataframe合并
def batch_process_csv(dir_str):
    file_name = os.listdir(dir_str)  # 返回指定目录下的所有文件和目录名
    file_dir = [os.path.join(dir_str, x) for x in file_name]  # 得到所有文件路径
    combine_df = pd.DataFrame()
    for i in range(len(file_dir)):  # 遍历整个file_dir,得到每个路径
        df = pd.read_csv(file_dir[i])  # 得到该csv的df
        combine_df = combine_two_datafame(combine_df, df)  # combine_df每次与得到的df合并
    return combine_df

# 给每个城市赋上它们的编码，放在最后新的一列
# 由于处理数据的形式，每个城市或区县只出现一次，所以没必要使用该def，人工赋值一遍即可
def city_code_assign(df):
    # 城市的名字和编码需要手动填写
    dict = {
        "Jason": 222,
        "Adam": 222,
        "Bob": 222,
    }
    # 在df后面再加一行
    df["City_code"] = 0
    len_Line = df.shape[0]  # 返回df的行数
    for i in range(len_Line):  # 遍历每一行df
        thisCity = df.iloc[i, 0]  # thiscity赋值为城市名字
        for key in dict.keys():  # 遍历字典
            if (thisCity == key):  # 如果字典里这个名字和thiscity符合
                df.iloc[i, "City_code"] = dict[key]  # 那么给该行df的City_code列赋上对应的值
                break  # 已经找到值了，那么跳出循环，继续匹配df的下一行
    return df

# 按城市编码排序
def rank_city_code(df):
    df.sort_values(by="City_code", inplace=True, ascending=True)  # 按照升序排序
    return df

# 填补缺失值
def missing_data_filling(df):
    len_Line = df.shape[0]  # 返回df的列数
    len_Row = df.shape[1];  # 返回df的行数
    for i in range(len_Line):  # 遍历每一行和列df
        for j in range(len_Row):
            number = df.iloc[i, j]  # 记录值
            if ((type(number) != str) and math.isnan(number)):  # 判断相等 需要用math平且需要判断number不能为str
                df.iloc[i, j] = 999998765.43
    return df
