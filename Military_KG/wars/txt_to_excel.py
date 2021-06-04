# 将爬取的战争信息整合到excel中

import pandas as pd
import os
from  tqdm import tqdm


file_1 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\\wars_info.txt'
file_2 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\\wars_info.xlsx'
fh = open(file_1,'r',encoding='utf-8')
df = pd.read_excel(file_2).astype(str)
# items = []
# lines = fh.readlines()
# for line in lines:
#     if '$' in line:
#         items.append(line[1:].strip())
# print(set(items))
# 0 名称
# 1 外文名
# 2 时间
# 3 地点
# 4 参战方
# 5 参战兵力
# 6 结果
# 7 伤亡情况
# 8 主要指挥官
# 9 战后条约
# 10 别名

lines = fh.readlines()
war_index = 0
length = len(lines)
for i in tqdm(range(length)):
    if '#' in lines[i]:
        df.iat[war_index,0] = lines[i+2]
        war_index = war_index + 1
    else:
        if '$' in lines[i]:
            if lines[i][1:].strip() == '外文名':
                df.iat[war_index - 1,1] = lines[i+1].strip()
            if lines[i][1:].strip() == '时间':
                df.iat[war_index - 1,2] = lines[i+1].strip()
            if lines[i][1:].strip() == '地点':
                df.iat[war_index - 1,3] = lines[i+1].strip()
            if lines[i][1:].strip() == '参战方':
                df.iat[war_index - 1,4] = lines[i+1].strip()
            if lines[i][1:].strip() == '参战方兵力':
                df.iat[war_index - 1,5] = lines[i+1].strip()
            if lines[i][1:].strip() == '结果':
                df.iat[war_index - 1,6] = lines[i+1].strip()
            if lines[i][1:].strip() == '伤亡情况':
                df.iat[war_index - 1,7] = lines[i+1].strip()
            if lines[i][1:].strip() == '主要指挥官':
                df.iat[war_index - 1,8] = lines[i+1].strip()
            if lines[i][1:].strip() == '战后条约':
                df.iat[war_index - 1,9] = lines[i+1].strip()
            if lines[i][1:].strip() == '别名':
                df.iat[war_index - 1,10] = lines[i+1].strip()


df.to_excel(file_2,index=False)





