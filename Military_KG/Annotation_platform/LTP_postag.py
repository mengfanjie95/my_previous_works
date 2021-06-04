# 利用LTP对语料进行词性标注

import os
from tqdm import tqdm
from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger

txt_path_1 = "D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\news_mixed.txt"
txt_path_2 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\news_annotation.txt'
txt = ''
fh_1 = open(txt_path_1,'r',encoding='UTF-8')
fh_2 = open(txt_path_2,'w',encoding='UTF-8')
lines = fh_1.readlines()
for line in tqdm(lines):
    txt = txt + line.strip()

LTP_DATA_DIR = 'D:\\LTP_model\\LTP_model\\ltp_data_v3.4.0\\ltp_data_v3.4.0'  # ltp模型目录的路径

# 分句
sents = SentenceSplitter.split(txt)  # 分句
sents = list(sents)

# 分词和词性标注
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`

segmentor = Segmentor()  # 初始化分词函数实例
postagger = Postagger()  # 初始化词性标注函数实例
segmentor.load(cws_model_path)  # 加载分词模型
postagger.load(pos_model_path)  # 加载词性标注模型

for sent in tqdm(sents):
    #print(sent)
    words = segmentor.segment(sent)  # 分词
    #print('/'.join(words))
    fh_2.write('/'.join(words))
    fh_2.write('\n')
    postags = postagger.postag(words)  # 词性标注
    #print('/'.join(postags))
    fh_2.write('/'.join(postags))
    fh_2.write('\n')
segmentor.release()  # 释放分词模型
postagger.release()  # 释放词性标注模型




