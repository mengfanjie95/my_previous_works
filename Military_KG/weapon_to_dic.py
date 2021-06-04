# 将5800种武器名称抽取出来，写入分词的词典中
from tqdm import tqdm

file_1 = 'D:\文件夹汇总\项目\军事知识图谱\\军事词库.txt'
file_2 = 'D:\文件夹汇总\项目\军事知识图谱\QAonMilitaryKG-master\data\\military.json'

fh_1 = open(file_1,'a+',encoding='UTF-8')
fh_2 = open(file_2,'r',encoding='UTF-8')
lines = fh_2.readlines()
for line in lines:
    words = line.split('"')
    weapon = words[9]
    if '/' not in weapon:
        fh_1.write(weapon)
        fh_1.write('\n')
    else:
        fh_1.write(weapon.split('/')[0])
        fh_1.write('\n')
        fh_1.write(weapon.split('/')[1])
        fh_1.write('\n')



