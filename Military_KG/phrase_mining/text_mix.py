# 将所有的文章放到一起，用于统计n-gram的频次等

from tqdm import tqdm
file_1 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\news.txt'
file_2 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\news_mixed.txt'
fh_1 = open(file_1,'r',encoding='UTF-8')
fh_2 = open(file_2,'w',encoding='UTF-8')
lines = fh_1.readlines()
n = len(lines)
i = 0
while i < n:
    # if lines[i][0:4].strip() == 'http':
    #     print(lines[i])
    # if lines[i] == '\n':
    #     pass
    if lines[i][0:4].strip() != 'http' and lines[i] != '\n' and lines[i - 1][0:4].strip() != 'http' and lines[i - 1] != '\n':

        fh_2.write(lines[i].strip())
        fh_2.write('\n')
    i = i + 1
fh_2.close()



