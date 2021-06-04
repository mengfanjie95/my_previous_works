from tqdm import tqdm
import jieba

jieba.load_userdict('military_words.txt')

# # 建立中文的停用词表
# def stopwordslist(filepath):
#     stopwords = [line.strip() for line in open(filepath, 'r', encoding='GBK').readlines()]
#     return stopwords

file_1 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\news.txt'
file_2 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\news_seg.txt'

fh_1 = open(file_1,'r',encoding='UTF-8')
fh_2 = open(file_2,'w',encoding='UTF-8')

lines = fh_1.readlines()
point = []
for line in tqdm(lines):
    if 'http' in line:
        k = lines.index(line)
        point.append(k)


n = len(point)
for i in tqdm(range(n-1)):
    news = ''
    # fh_2.write(lines[point[i]-1])
    result_1 = jieba.cut(lines[point[i]-1].strip(),HMM=True)
    fh_2.write("/".join(result_1))
    fh_2.write('\n')
    fh_2.write(lines[point[i]])
    #fh_2.write('\n')
    for k in range(point[i] + 1,point[i+1] - 1):
        news = news + lines[k].strip()
    result_2 = jieba.cut(news,HMM=True)
    fh_2.write("/".join(result_2))
    fh_2.write('\n')
    fh_2.write('\n')








