# 根据种子库中的数据获得的pattern ： 国家+ 职位 + 人名

from tqdm import tqdm
from LTP_operation import LTP

ltp = LTP()
file_1 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\news_mixed.txt'
file_2 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\LocatedIn\\seed_triple.txt'
file_3 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\LocatedIn\\seed_sent.txt'
file_4 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\LocatedIn\\pattern.txt'

fh_1 = open(file_1, 'r', encoding='UTF-8')
fh_2 = open(file_2, 'r', encoding='UTF-8')
fh_3 = open(file_3, 'a+', encoding='UTF-8')
fh_4 = open(file_4, 'a+', encoding='UTF-8')

# 先读取所有的新闻
lines_1 = fh_1.readlines()
txt = ''
for line in tqdm(lines_1):
    txt = txt + line.strip()

# 将所有的新闻分句
sents = ltp.sent_split(txt)

# 对实体种子库和新闻进行软匹配，找到种子句子