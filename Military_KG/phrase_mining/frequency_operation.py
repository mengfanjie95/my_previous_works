# 先进行子短语频数减去父短语频数的操作
from tqdm import tqdm

file_path_1 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\n-gram_frequency.txt'
file_path_2 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\n-gram_frequency_operation.txt'
fh_1 = open(file_path_1,'r',encoding='UTF-8')
fh_2 = open(file_path_2,'a+',encoding='UTF-8')
lines = fh_1.readlines()

word_2 = {}
word_3 = {}
word_4 = {}
word_5 = {}
word_6 = {}
word_7 = {}

line_2 = lines[0].strip().split(',')
fre_2 = lines[1].strip().split(',')
line_3 = lines[3].strip().split(',')
fre_3 = lines[4].strip().split(',')
line_4 = lines[6].strip().split(',')
fre_4 = lines[7].strip().split(',')
line_5 = lines[9].strip().split(',')
fre_5 = lines[10].strip().split(',')
line_6 = lines[12].strip().split(',')
fre_6 = lines[13].strip().split(',')
line_7 = lines[15].strip().split(',')
fre_7 = lines[16].strip().split(',')

print(fre_2)

n2 = len(line_2)
for i in range(n2):
    if int(fre_2[i]) > 50:
        word_2[line_2[i]] = int(fre_2[i])

n3 = len(line_3)
for i in range(n3):
    if int(fre_3[i]) > 50:
        word_3[line_3[i]] = int(fre_3[i])

n4 = len(line_4)
for i in range(n4):
    if int(fre_4[i]) > 50:
        word_4[line_4[i]] = int(fre_4[i])

n5 = len(line_5)
for i in range(n5):
    if int(fre_5[i]) > 50:
        word_5[line_5[i]] = int(fre_5[i])

n6 = len(line_6)
for i in range(n6):
    if int(fre_6[i]) > 50:
        word_6[line_6[i]] = int(fre_6[i])

n7 = len(line_7)
for i in range(n7):
    if int(fre_7[i]) > 50:
        word_7[line_7[i]] = int(fre_7[i])


# 对字长为2的序列操作
for k2, v2 in tqdm(word_2.items()):
    for k3,v3 in word_3.items():
        if k2 in k3 :
            word_2[k2] = v2-v3

    for k4,v4 in word_4.items():
        if k2 in k4 :
            word_2[k2] = v2-v4

    for k5,v5 in word_5.items():
        if k2 in k5 :
            word_2[k2] = v2-v5

    for k6,v6 in word_6.items():
        if k2 in k6 :
            word_2[k2] = v2-v6

    for k7,v7 in word_7.items():
        if k2 in k7 :
            word_2[k2] = v2-v7

# 对字长为3的序列操作
for k3, v3 in tqdm(word_3.items()):

    for k4,v4 in word_4.items():
        if k3 in k4 :
            word_3[k3] = v3-v4

    for k5,v5 in word_5.items():
        if k3 in k5 :
            word_3[k3] = v3-v5

    for k6,v6 in word_6.items():
        if k3 in k6 :
            word_3[k3] = v3-v6

    for k7,v7 in word_7.items():
        if k3 in k7 :
            word_3[k3] = v3-v7



# 对字长为4的序列操作
for k4, v4 in tqdm(word_4.items()):

    for k5,v5 in word_5.items():
        if k4 in k5 :
            word_4[k4] = v4-v5

    for k6,v6 in word_6.items():
        if k4 in k6 :
            word_4[k4] = v4-v6

    for k7,v7 in word_7.items():
        if k4 in k7 :
            word_4[k4] = v4-v7


# 对字长为5的序列操作
for k5, v5 in tqdm(word_5.items()):

    for k6,v6 in word_6.items():
        if k5 in k6 :
            word_5[k5] = v5-v6

    for k7,v7 in word_7.items():
        if k5 in k7 :
            word_5[k5] = v5-v7


# 对字长为6的序列操作
for k6, v6 in tqdm(word_6.items()):

    for k7,v7 in word_7.items():
        if k6 in k7 :
            word_6[k6] = v6-v7






Ks = []
Vs = []
for k, v in tqdm(word_2.items()):
    if v > 100:
        Ks.append(k)
        Vs.append(v)

fh_2.write('\n')
fh_2.write(str(Ks))
fh_2.write('\n')
fh_2.write(str(Vs))
fh_2.write('\n')


Ks = []
Vs = []
for k, v in tqdm(word_3.items()):
    if v > 100:
        Ks.append(k)
        Vs.append(v)

fh_2.write('\n')
fh_2.write(str(Ks))
fh_2.write('\n')
fh_2.write(str(Vs))
fh_2.write('\n')


Ks = []
Vs = []
for k, v in tqdm(word_4.items()):
    if v > 100:
        Ks.append(k)
        Vs.append(v)

fh_2.write('\n')
fh_2.write(str(Ks))
fh_2.write('\n')
fh_2.write(str(Vs))
fh_2.write('\n')


Ks = []
Vs = []
for k, v in tqdm(word_5.items()):
    if v > 100:
        Ks.append(k)
        Vs.append(v)

fh_2.write('\n')
fh_2.write(str(Ks))
fh_2.write('\n')
fh_2.write(str(Vs))
fh_2.write('\n')


Ks = []
Vs = []
for k, v in tqdm(word_6.items()):
    if v > 100:
        Ks.append(k)
        Vs.append(v)

fh_2.write('\n')
fh_2.write(str(Ks))
fh_2.write('\n')
fh_2.write(str(Vs))
fh_2.write('\n')


Ks = []
Vs = []
for k, v in tqdm(word_7.items()):
    if v > 100:
        Ks.append(k)
        Vs.append(v)

fh_2.write('\n')
fh_2.write(str(Ks))
fh_2.write('\n')
fh_2.write(str(Vs))
fh_2.write('\n')

