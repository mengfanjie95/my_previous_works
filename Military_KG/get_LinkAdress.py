# 首先获得每篇新闻的标题，summary和链接
import json
from urllib.request import Request, urlopen
from tqdm import tqdm
import time

url_1 = 'https://mil.huanqiu.com/api/list2?node=/e3pmh1dm8/e3pmt7hva&offset='
url_2 = '&limit=20'
chrome_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
fh = open('D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\\huanqiu_1\\news_scription.txt','a+',encoding='UTF-8')
for i in tqdm(range(227,500)):
    url = url_1 + str(20 * i) + url_2
    #print(url)
    request = Request(url,headers=chrome_headers)
    html = urlopen(request)
    # print(html)
    data = html.read().decode()
    # #print(data)
    # #print(strs)
    # # strs_for_json = strs[4:]
    # # strs_for_json = strs_for_json[:-2]
    # # #json_obj = demjson(strs_for_json)
    # # # print(strs_for_json)
    # # data = strs_for_json
    # json_data = json.dumps(data,ensure_ascii=False)
    # # data_json = json.loads(strs)
    # # print(data_json['datas'][0]['aid'])
    # #print(datas)
    # #print(type(datas))
    python_data = json.loads(data)
    for j in range(20):
        fh.write(python_data['list'][j]['title'])
        fh.write('\n')
        fh.write('https://mil.huanqiu.com/article/' + python_data['list'][j]['aid'])
        fh.write('\n')
        fh.write(python_data['list'][j]['summary'])
        fh.write('\n')
        fh.write('\n')
        print(i,j)
        time.sleep(1)
    time.sleep(5)

fh.close()




