from smoothnlp import kg
rels = kg.extract(text = ["SmoothNLP在V0.3版本中正式推出知识抽取功能",
                          "SmoothNLP专注于可解释的NLP技术",
                          "SmoothNLP支持Python与Java",
                          "SmoothNLP将帮助工业界与学术界更加高效的构建知识图谱",
                          "SmoothNLP是上海文磨网络科技公司的开源项目"])  ## 调用SmoothNLP解析
g = kg.rel2graph(rels)  ## 依据文本解析结果, 生成networkx有向图
fig = kg.graph2fig(g,x=1000,y=1000)  ## 生成 matplotlib.figure.Figure 图片
fig.savefig("SmoothNLP_KG_Demo.png") ## 保存图片到PNG