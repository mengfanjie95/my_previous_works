# 根据extraction_dataproperty_name.py抽取出的每项武器的dataproperty，整理到
# 对应的excel文件中，然后分别再进行抽取，抽取结束后再写到owl文件中

import os
from tqdm import tqdm
import pandas as pd

txt_directory = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\Weapons\\weapons.txt'
files_directory = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\Weapons\\types'
files = os.listdir(files_directory)
fh = open(txt_directory,'r',encoding='utf-8')
lines = fh.readlines()
for file in tqdm(files):
    index_1 = 1
    # file就是excel的文件名，也是对应的武器类名
    file_directory = files_directory + '\\' + file
    df = pd.read_excel(file_directory).astype(str)
    columns = list(df.columns)
    # print(columns)
    for line in lines:
        items = line.split('$')
        items_length = len(items)
        if items[-2].split('"')[3] == file[:-5]:
            for i in range(items_length):
                if len(items[i].split('"')) > 4:
                    if items[i].split('"')[1].strip() in columns:
                        index_2 = df.columns.get_loc(items[i].split('"')[1].strip())
                        df.iat[index_1,index_2] = items[i].split('"')[3].strip()
            index_1 = index_1 + 1
    df.to_excel(files_directory + '\\' + file,index=False)









