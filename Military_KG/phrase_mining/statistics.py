# 统计每个n-gram的具体最大最小频次，以及在各个频段间的比例，用来设定最终的最低阈值
# 对于不同的n来说，n-gram的最小频次应该是不同的


file = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\n-gram_frequency.txt'
fh = open(file, 'r', encoding='UTF-8')
lines = fh.readlines()
for i in range(6):
    words = lines[3 * i].strip().split(',')
    num = lines[3 * i + 1].strip().split(',')
    new_num = [int(x) for x in num]
    # print(max(new_num))
    # print(min(new_num))
    Max = max(new_num)
    Min = min(new_num)
    Mid = (Max + Min)/2+Max
    org_1 = 0
    org_2 = 0
    for value in new_num:
        if value > Min and value < Mid:
            org_1 = org_1 + 1
        else:
            org_2 = org_2 + 1
    



