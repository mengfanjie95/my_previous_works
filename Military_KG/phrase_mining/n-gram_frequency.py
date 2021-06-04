# 统计n-gram频次

from tqdm import tqdm
import string

file_1 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\news_mixed.txt'
file_2 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\n-gram_frequency.txt'
fh_1 = open(file_1, 'r', encoding='UTF-8')
fh_2 = open(file_2, 'a+', encoding='UTF-8')
lines = fh_1.readlines()
n = len(lines)
txt = lines[0]
symbol = ['。', '，', '、', '；', '：', '？', '！', '“', '‘', '（', '）', '……', '《', '》', '【', '】', '<', '>', '▲', ' ', '"', '”']
# for i in tqdm(txt):
#     if i in symbol:
#         txt = txt.replace(i,'')
for item in tqdm(symbol):
    txt = txt.translate(str.maketrans('', '', item))
print(txt)

m = len(txt)
print(m)
word_2 = {}
word_3 = {}
word_4 = {}
word_5 = {}
word_6 = {}
word_7 = {}

# for i in tqdm(range(m - 1)):
#     if txt[i] + txt[i + 1] not in word_2:
#         word_2[txt[i] + txt[i + 1]] = 1
#     else:
#         word_2[txt[i] + txt[i + 1]] = word_2[txt[i] + txt[i + 1]] + 1

# for i in tqdm(range(m - 2)):
#     if txt[i] + txt[i + 1] + txt[i + 2] not in word_3:
#         word_3[txt[i] + txt[i + 1] + txt[i + 2]] = 1
#     else:
#         word_3[txt[i] + txt[i + 1] + txt[i + 2]] = word_3[txt[i] + txt[i + 1] + txt[i + 2]] + 1

# for i in tqdm(range(m - 3)):
#     if txt[i] + txt[i + 1] + txt[i + 2] + txt[i + 3] not in word_4:
#         word_4[txt[i] + txt[i + 1] + txt[i + 2] + txt[i + 3]] = 1
#     else:
#         word_4[txt[i] + txt[i + 1] + txt[i + 2] + txt[i + 3]] = word_4[txt[i] + txt[i + 1] + txt[i + 2] + txt[i + 3]] + 1

# for i in tqdm(range(m-4)):
#     if txt[i]+txt[i+1]+txt[i+2]+txt[i+3]+txt[i+4] not in word_5:
#         word_5[txt[i]+txt[i+1]+txt[i+2]+txt[i+3]+txt[i+4]] = 1
#     else:
#         word_5[txt[i]+txt[i+1]+txt[i+2]+txt[i+3]+txt[i+4]] = word_5[txt[i]+txt[i+1]+txt[i+2]+txt[i+3]+txt[i+4]] +1

# for i in tqdm(range(m-5)):
#     if txt[i]+txt[i+1]+txt[i+2]+txt[i+3]+txt[i+4]+txt[i+5] not in word_6:
#         word_6[txt[i]+txt[i+1]+txt[i+2]+txt[i+3]+txt[i+4]+txt[i+5]] = 1
#     else:
#         word_6[txt[i]+txt[i+1]+txt[i+2]+txt[i+3]+txt[i+4]+txt[i+5]] = word_6[txt[i]+txt[i+1]+txt[i+2]+txt[i+3]+txt[i+4]+txt[i+5]] +1

for i in tqdm(range(m - 6)):
    if txt[i] + txt[i + 1] + txt[i + 2] + txt[i + 3] + txt[i + 4] + txt[i + 5] + txt[i + 6] not in word_7:
        word_7[txt[i] + txt[i + 1] + txt[i + 2] + txt[i + 3] + txt[i + 4] + txt[i + 5] + txt[i + 6]] = 1
    else:
        word_7[txt[i] + txt[i + 1] + txt[i + 2] + txt[i + 3] + txt[i + 4] + txt[i + 5] + txt[i + 6]] = word_7[txt[i] + txt[i + 1] +txt[i + 2] +
                                                                                                           txt[i + 3] +txt[i + 4] +
                                                                                                           txt[i + 5] +txt[i + 6]] + 1

Ks = []
Vs = []
for k, v in tqdm(word_7.items()):
    if v > 50:
        Ks.append(k)
        Vs.append(v)

fh_2.write('\n')
fh_2.write(str(Ks))
fh_2.write('\n')
fh_2.write(str(Vs))
fh_2.write('\n')
