# 在这里完成分词，句法分析等操作，用于后面的pattern的识别和记录

import os
from tqdm import tqdm
from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import Parser
from pyltp import NamedEntityRecognizer

LTP_DATA_DIR = 'D:\\LTP_model\\LTP_model\\ltp_data_v3.4.0\\ltp_data_v3.4.0'  # ltp模型目录的路径


class LTP:

    def __int__(self):
        self.splits = SentenceSplitter()

    #创建停用词表
    def stopwordslist(self,filepath):
        stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
        return stopwords


    # 分句
    def sent_split(self, txt):
        sents = SentenceSplitter().split(txt)  # 分句
        sents = list(sents)
        return sents

    # 分词
    def seg(self, sent):
        cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
        segseg = Segmentor()
        segseg.load(cws_model_path)  # 加载分词模型
        words = segseg.segment(sent)  # 分词
        segseg.release()  # 释放分词模型
        return str('/'.join(words))

    # 词性标注
    def pos(self, sent):
        pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
        cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
        segseg = Segmentor()
        segseg.load(cws_model_path)  # 加载分词模型
        words = segseg.segment(sent)  # 分词
        postagger = Postagger()  # 初始化词性标注函数实例
        postagger.load(pos_model_path)  # 加载词性标注模型
        postags = postagger.postag(words)  # 词性标注
        segseg.release()  # 释放分词模型
        postagger.release()  # 释放词性标注模型
        return str('/'.join(postags))

    # 依存句法分析
    def pars(self, sent):
        pars_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 句法分析模型路径，模型名称为`parser.model`
        parser = Parser()
        parser.load(pars_model_path)
        arcs = parser.parse(LTP.seg(self, sent).split('/'), LTP.pos(self, sent).split('/'))
        return ("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))

    # 命名实体识别
    def ner(self, sent):
        recognizer = NamedEntityRecognizer()  # 初始化实例
        ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')
        recognizer.load(ner_model_path)  # 加载模型
        netags = recognizer.recognize(LTP.seg(self, sent).split('/'), LTP.pos(self, sent).split('/'))
        # for word, ntag in zip(words, netags):
        #   print(word + '/' + ntag)
        recognizer.release()  # 释放模型
        return netags
