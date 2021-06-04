# 根据种子库中的数据获得的pattern ： 国家+ 职位 + 人名

from tqdm import tqdm
from LTP_operation import LTP

ltp = LTP()
file_1 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\news_mixed.txt'
file_2 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\HasJobTitle\\seed_triple.txt'
file_3 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\HasJobTitle\\seed_sent.txt'
file_4 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\HasJobTitle\\pattern.txt'

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

sents_len = len(sents)


# 将句子中的不必要信息删除
for i in tqdm(range(sents_len)):
    if '】' in sents[i]:
        left = int(sents[i].index('】'))
        length = len(sents[i])
        # print(left, length)
        # print(sent)
        sents[i] = sents[i][int(left + 1):]

Nation_list = ('中国 中 丹麦 乌克兰 以色列 伊拉克 伊朗 俄罗斯 俄 保加利亚 利比亚 加拿大 加 卡塔尔 印度 印 印度尼西亚 印尼 '+
               '叙利亚 古巴 哥伦比亚 土耳其 委内瑞拉 巴基斯坦 巴勒斯坦 巴西 希腊 德国 意大利 挪威 新西兰 日本 日 朝鲜 柬埔寨 '+
               '比利时 沙特阿拉伯 法国 波兰 泰国 澳大利亚 瑞士 科威特 秘鲁 缅甸 罗马尼亚 美国 美 老挝 英国 荷兰 菲律宾 葡萄牙 '+
               '蒙古 西班牙 越南 阿富汗 阿根廷 韩国 韩 马来西亚 黎巴嫩').split()
print(Nation_list)
for i in tqdm(range(15001,sents_len)):
    sent = sents[i]
    Nation_pos = []
    Name_pos = []
    JobTitle = []
    segs = ltp.seg(sent).split('/')
    poss = ltp.pos(sent).split('/')
    ners = list(ltp.ner(sent))
    #print(ners)
    # 统计sentence中国家和人名的位置信息
    for j in range(len(ners)):
        if ners[j] == 'S-Ns' and segs[j] in Nation_list:
            Nation_pos.append(j)
        if ners[j] == 'S-Nh':
            Name_pos.append(j)
    # 判断哪些组合可能产生Jobtitle
    # print(Nation_pos)
    # print(Name_pos)
    for nation_pos in Nation_pos:
        for name_pos in Name_pos:
            if nation_pos < name_pos and (name_pos - nation_pos) <= 4:
                JobTitle.append([nation_pos,name_pos])
    if len(JobTitle) > 0:
        for jobtitle in JobTitle:
            #print(segs[jobtitle[0]:jobtitle[1]+1])
            job = segs[jobtitle[0]:jobtitle[1]]
            jobname = ''
            for word in job:
                jobname = jobname + word
            name = segs[jobtitle[1]]
            #print(jobname,name)
            fh_3.write(jobname)
            fh_3.write('  ')
            fh_3.write(name)
            fh_3.write('  ')
            fh_3.write(sent)
            fh_3.write('\n')
    if i == 30000:
        fh_3.close()
        break








