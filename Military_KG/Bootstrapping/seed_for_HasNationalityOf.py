# 分析得出，对于HasNationalityOf这样的关系，关系模式应该较为单一(模式数量和复杂度低)
# 所以暂时先尝试该方法

from tqdm import tqdm
from LTP_operation import LTP

ltp = LTP()
file_1 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\news_mixed.txt'
file_2 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\HasNationalityOf\\seed_triple.txt'
file_3 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\HasNationalityOf\\seed_sent.txt'
file_4 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\HasNationalityOf\\pattern.txt'

fh_1 = open(file_1, 'r', encoding='UTF-8')
fh_2 = open(file_2, 'a+', encoding='UTF-8')
fh_3 = open(file_3, 'a+', encoding='UTF-8')
fh_4 = open(file_4, 'a+', encoding='UTF-8')

# 先读取所有的新闻
lines_1 = fh_1.readlines()
txt = ''
for line in tqdm(lines_1):
    txt = txt + line.strip()

# 将所有的新闻分句
sents = ltp.sent_split(txt)

sents_len = len(sents)


# 将句子中的不必要信息删除

for i in tqdm(range(sents_len)):
    if '】' in sents[i]:
        left = int(sents[i].index('】'))
        length = len(sents[i])
        # print(left, length)
        # print(sent)
        sents[i] = sents[i][int(left + 1):]

# 对每个句子进行ner，先收集大概600对实体对，
for i in tqdm(range(601, sents_len)):

    netags = list(ltp.ner(sents[i]))
    words = ltp.seg(sents[i]).split('/')
    # print(type(list(netags)),list(netags))
    if 'S-Nh' in netags and 'S-Ns' in netags:
        # print(words[netags.index('S-Nh')],words[netags.index('S-Ns')])
        fh_2.write(words[netags.index('S-Nh')])
        fh_2.write('  ')
        fh_2.write(words[netags.index('S-Ns')])
        fh_2.write('  ')
        fh_2.write(sents[i].strip())
        fh_2.write('\n')
    if sents.index(sents[i]) == 15000:
        break
fh_2.close()
