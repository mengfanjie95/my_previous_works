# 把各项武器的内容抽取出来
from tqdm import tqdm

file_1 = 'D:\文件夹汇总\项目\军事知识图谱\QAonMilitaryKG-master\data\\military.json'
file_2 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\\weapons.txt'

fh_1 = open(file_1,'r',encoding='utf-8')
fh_2 = open(file_2,'w',encoding='utf-8')

lines = fh_1.readlines()
for line in tqdm(lines):
    infos = line.split(',')
    strs = '## '
    for info in infos:
        # print(info[2:4])
        if info[2:4] not in ['简介','图片','"_']:
            strs = strs + '$' + info.strip()
    fh_2.write(strs)
    fh_2.write('\n')



