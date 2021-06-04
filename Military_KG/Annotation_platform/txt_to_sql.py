# 将处理好的文本转化为sql中的insert语句

from tqdm import tqdm

file_path_1 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\news_annotation.txt'
file_path_2 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\seg_insert.txt'
file_path_3 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\train_insert.txt'

fh_1 = open(file_path_1,'r',encoding='UTF-8')
fh_2 = open(file_path_2,'w',encoding='UTF-8')
fh_3 = open(file_path_3,'w',encoding='UTF-8')


lines = fh_1.readlines()
n = len(lines)
n = int(n/2)

for i in tqdm(range(n)):
    # 先写插入到seg_nominal表中的语句
    seg_sent = "INSERT INTO `seg_nominal` VALUES (" + str(i+1) + ", '" + lines[2 * i].strip().replace("'",'"') + "', " + "'', " + "'" +lines[2 * i + 1].strip().replace("'",'"') + "', '', 'user1');"
    fh_2.write(seg_sent)
    fh_2.write('\n')

    # 再写插入到traindata表中的语句
    train_sent = "INSERT INTO `traindata` VALUES (" + str(i+1) + "," + " '" + lines[2 * i].strip().replace("'",'"') + "', "+ "NULL, NULL, 0," + " 'user1', '', 0);"
    fh_3.write(train_sent)
    fh_3.write('\n')

