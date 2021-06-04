# 统计各类武器分别需要添加哪些dataproperties，统计后筛选
from tqdm import tqdm

file = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\weapons.txt'
fh = open(file,'r',encoding='utf-8')
lines = fh.readlines()
weapon_1 = [] # 飞行器
weapon_2 = [] # 舰船舰艇
weapon_3 = [] # 枪械与单兵
weapon_4 = [] # 坦克装甲车辆
weapon_5 = [] # 火炮
weapon_6 = [] # 导弹武器
weapon_7 = [] # 太空装备
weapon_8 = [] # 爆炸物
for line in tqdm(lines):
    items = line.split('$')
    items_length = len(items)
    #print(items[-2].split('"')[1])


    if items[-2].split('"')[3] == '飞行器':
        for i in range(items_length):
            content = ''
            if len(items[i].split('"')) > 4:
                weapon_1.append(items[i].split('"')[1])


    if items[-2].split('"')[3] == '舰船与舰艇':
        for i in range(items_length):
            content = ''
            if len(items[i].split('"')) > 4:
                weapon_2.append(items[i].split('"')[1])

    if items[-2].split('"')[3] == '枪械与单兵':
        for i in range(items_length):
            content = ''
            if len(items[i].split('"')) > 4:
                weapon_3.append(items[i].split('"')[1])

    if items[-2].split('"')[3] == '坦克装甲车辆':
        for i in range(items_length):
            content = ''
            if len(items[i].split('"')) > 4:
                weapon_4.append(items[i].split('"')[1])

    if items[-2].split('"')[3] == '火炮':
        for i in range(items_length):
            content = ''
            if len(items[i].split('"')) > 4:
                weapon_5.append(items[i].split('"')[1])

    if items[-2].split('"')[3] == '导弹武器':
        for i in range(items_length):
            content = ''
            if len(items[i].split('"')) > 4:
                weapon_6.append(items[i].split('"')[1])

    if items[-2].split('"')[3] == '太空装备':
        for i in range(items_length):
            content = ''
            if len(items[i].split('"')) > 4:
                weapon_7.append(items[i].split('"')[1])

    if items[-2].split('"')[3] == '爆炸物':
        for i in range(items_length):
            content = ''
            if len(items[i].split('"')) > 4:
                weapon_8.append(items[i].split('"')[1])



print(set(weapon_1))
print(set(weapon_2))
print(set(weapon_3))
print(set(weapon_4))
print(set(weapon_5))
print(set(weapon_6))
print(set(weapon_7))
print(set(weapon_8))





