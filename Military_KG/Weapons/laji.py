file_1 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\Weapons\\中转站_1.txt'
file_2 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\Weapons\\中转站_2.txt'

fh1 = open(file_1,'r',encoding='utf-8')
fh2 = open(file_2,'w',encoding='utf-8')

lines = fh1.readlines()

for i in range(132081):
    fh2.write(lines[i])

fh1.close()
fh2.close()