# 完成C-value指标的计算

from tqdm import tqdm
import math

def C_value(x,y):
    return ("{:.4f}".format(math.log2(len(x))*int(y)))


file_path_1 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\n-gram_frequency_operation.txt'
file_path_2 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\C_value.txt'

fh_1 = open(file_path_1,'r',encoding='UTF-8')
fh_2 = open(file_path_2,'a+',encoding='UTF-8')
lines = fh_1.readlines()


line_2 = lines[0].strip().split(',')
fre_2 = lines[1].strip().split(',')
C_2 = []
line_3 = lines[3].strip().split(',')
fre_3 = lines[4].strip().split(',')
C_3 = []
line_4 = lines[6].strip().split(',')
fre_4 = lines[7].strip().split(',')
C_4 = []
line_5 = lines[9].strip().split(',')
fre_5 = lines[10].strip().split(',')
C_5 = []
line_6 = lines[12].strip().split(',')
fre_6 = lines[13].strip().split(',')
C_6 = []
line_7 = lines[15].strip().split(',')
fre_7 = lines[16].strip().split(',')
C_7 = []


n2 = len(line_2)
for i in tqdm(range(n2)):
    # print(line_2[i],fre_2[i])
    C_2.append(C_value(line_2[i],fre_2[i]))

n3 = len(line_3)
for i in tqdm(range(n3)):
    C_3.append(C_value(line_3[i],fre_3[i]))

n4 = len(line_4)
for i in tqdm(range(n4)):
    C_4.append(C_value(line_4[i],fre_4[i]))

n5 = len(line_5)
for i in tqdm(range(n5)):
    C_5.append(C_value(line_5[i],fre_5[i]))

n6 = len(line_6)
for i in tqdm(range(n6)):
    C_6.append(C_value(line_6[i],fre_6[i]))

n7 = len(line_7)
for i in tqdm(range(n7)):
    C_7.append(C_value(line_7[i],fre_7[i]))


fh_2.write('\n')
fh_2.write(str(line_2))
fh_2.write('\n')
fh_2.write(str(fre_2))
fh_2.write('\n')
fh_2.write(str(C_2))
fh_2.write('\n')


fh_2.write('\n')
fh_2.write(str(line_3))
fh_2.write('\n')
fh_2.write(str(fre_3))
fh_2.write('\n')
fh_2.write(str(C_3))
fh_2.write('\n')


fh_2.write('\n')
fh_2.write(str(line_4))
fh_2.write('\n')
fh_2.write(str(fre_4))
fh_2.write('\n')
fh_2.write(str(C_4))
fh_2.write('\n')


fh_2.write('\n')
fh_2.write(str(line_5))
fh_2.write('\n')
fh_2.write(str(fre_5))
fh_2.write('\n')
fh_2.write(str(C_5))
fh_2.write('\n')


fh_2.write('\n')
fh_2.write(str(line_6))
fh_2.write('\n')
fh_2.write(str(fre_6))
fh_2.write('\n')
fh_2.write(str(C_6))
fh_2.write('\n')


fh_2.write('\n')
fh_2.write(str(line_7))
fh_2.write('\n')
fh_2.write(str(fre_7))
fh_2.write('\n')
fh_2.write(str(C_7))
fh_2.write('\n')



