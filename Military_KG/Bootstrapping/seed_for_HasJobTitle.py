# 根据HasNationalityOf抽取出的triple_seed来继续抽取HasJobTitle的triple和sent
# 首先尝试关系模式例如：“美国总统特朗普表示……”，其中美国和特朗普已经被识别成人名和国家名，存储在HasNationalityOf中了
# 所以暂时先尝试该方法

from tqdm import tqdm
from LTP_operation import LTP

ltp = LTP()
file_1 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\news_mixed.txt'
file_2 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\HasNationalityOf\\seed_triple.txt'
file_3 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\HasJobTitle\\seed_triple.txt'
file_4 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\HasNationalityOf\\pattern.txt'

fh_1 = open(file_1, 'r', encoding='UTF-8')
fh_2 = open(file_2, 'r', encoding='UTF-8')
fh_3 = open(file_3, 'a+', encoding='UTF-8')
fh_4 = open(file_4, 'a+', encoding='UTF-8')

lines_1 = fh_2.readlines()
print(len(lines_1))

for line in tqdm(lines_1):
    items = line.split()
    if items[1] not in items[2]:
        items[1] = items[1][0]
        print(items)

    left = int(items[2].index(items[1]))

    right = int(items[2].index(items[0]))
    print(left,right)
    JobTitle = items[2][left + len(items[1]):right]
    print(items[2])
    print(JobTitle)
    items = line.split()
    fh_3.write(items[0])
    fh_3.write('  ')
    fh_3.write(items[1]+JobTitle)
    fh_3.write('  ')
    fh_3.write(items[2])
    fh_3.write('\n')
