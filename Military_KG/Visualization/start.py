import eel
import time

from selenium import webdriver
import time

eel.init('web')

# 用来存储查询的内容
query_item = ''


# 定义selenium爬虫函数
def virtuoso_query(query_sent):
    # 打开conductor页面并登陆
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome('/Users/mengfanjie/opt/anaconda3/envs/py3.7/lib/python3.7/site-packages/selenium/chromedriver',chrome_options = option)
    virtuoso_url = 'http://localhost:8890/conductor/'
    browser.get(virtuoso_url)
    account = browser.find_element_by_xpath('//*[@id="t_login_usr"]')
    account.send_keys('dba')
    password = browser.find_element_by_xpath('//*[@id="t_login_pwd"]')
    password.send_keys('dba')
    login_button = browser.find_element_by_xpath('//*[@id="login_btn"]')
    login_button.click()

    # 点击进入查询界面
    linked_data = browser.find_element_by_xpath('//*[@id="nav_bar"]/tbody/tr/td[8]/a')
    linked_data_url = linked_data.get_attribute('href')
    browser.get(linked_data_url)

    # 找到IRI输入框，查询语句输入框和查询按钮，并输入数据的IRI，sparql语句，进行查询
    IRI_input = browser.find_element_by_xpath('//*[@id="default_graph"]')
    IRI_input.send_keys('http://localhost:8890/Military_weapon')
    Query_input = browser.find_element_by_xpath('//*[@id="qr"]')

    # 此处的查询语句只是例子，实际查询语句需要通过用户的输入来生成
    Query_input.send_keys(query_sent)
    Query_button = browser.find_element_by_xpath(
        '//*[@id="RB"]/div[2]/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td/form/table/tbody/tr[3]/td/input[1]')
    Query_button.click()
    time.sleep(0.5)

    trs = browser.find_element_by_css_selector('#rdf_result > table > tbody')
    tr_items = trs.find_elements_by_tag_name('tr')
    tr_length = len(tr_items)
    result_1 = []
    result_2 = []

    # 定义一个函数用来从网页爬取的结果抽取出想要的内容
    def str2item(str):
        if '#' in str:
            return str.split('#')[1]
        else:
            return str.split('"')[1]

    for i in range(2, tr_length + 1):
        item_1 = browser.find_element_by_xpath('//*[@id="rdf_result"]/table/tbody/tr[' + str(i) + ']/td[1]')
        item_2 = browser.find_element_by_xpath('//*[@id="rdf_result"]/table/tbody/tr[' + str(i) + ']/td[2]')
        result_1.append(str2item(item_1.text))
        result_2.append(str2item(item_2.text))

    return [result_1, result_2]



# 定义函数来将抽取内容转换为json格式
# def res2json():



# 定义一个查询函数，调用virtuoso_query函数从virtuoso数据库中查询
# 暴露给js
@eel.expose
def Query(entity):
    print(1)
    item = ''
    item = entity

    # 定义一个函数用来将网页查询的内容转换成sparql语句
    def str2sparql(strs):
        # 初步只支持实体查询，后续添加对话内容
        strs = str(strs)
        sents = []
        # query_sent_1 = 'select ?p ?o where{<http://www.semanticweb.org/mengfanjie/ontologies/2020/1/untitled-ontology-10#' + strs + '> ?p ?o}'
        query_sent_2 = 'select ?s ?p where{?s ?p <http://www.semanticweb.org/mengfanjie/ontologies/2020/1/untitled-ontology-10#' + strs + '>}'
        # sents.append(query_sent_1)
        sents.append(query_sent_2)
        return query_sent_2

    print(str2sparql(entity))

    sparql_sents = str2sparql(entity)
    # res_1 = virtuoso_query(sparql_sents[0]) # 第一个查询语句，entity是头实体
    res_2 = virtuoso_query(sparql_sents)  # 第二个查询语句，entity是尾实体
    # 定义一个函数用来读取要查询的内容
    # def return_query(entity):
    #     # 读取查询内容
    #     query_item = entity
    # return_query(entity)
    # 打印查询语句和查询结果
    print(item)
    print(res_2)
    # 定义一个将查询结果转换成echarts data结构的数据
    def result2echarts(sparql_sent):
        # 先将中心节点写进去
        fh = open('/Users/mengfanjie/PycharmProjects/PycharmProjects/Military_KG/Visualization/web/items.json','w',encoding='UTF-8')
        fh.write("{")
        fh.write('\n')
        fh.write('  "nodes": [')
        fh.write('\n')
        fh.write('    {')
        fh.write('\n')
        fh.write('      "name": "' + item +'",')
        fh.write('\n')
        fh.write('      "des": "node_0",')
        fh.write('\n')
        fh.write('      "symbolSize": 60,')
        fh.write('\n')
        fh.write('      "category": 0')
        fh.write('\n')
        fh.write('    },')
        fh.write('\n')


        result_len = len(res_2[0])
        if result_len > 100:
            result_len = 80
        # 接着写入所有查询出的实体节点
        for i in range(result_len):
            fh.write('    {')
            fh.write('\n')
            fh.write('      "name": "' + res_2[0][i] + '",')
            fh.write('\n')
            fh.write('      "des": "node_' + str(i+1) + '",')
            fh.write('\n')
            fh.write('      "symbolSize": 40,')
            fh.write('\n')
            fh.write('      "category": 1')
            fh.write('\n')
            if i != result_len - 1:
                fh.write('    },')
            else:
                fh.write('    }')
        fh.write('\n')
        fh.write('  ],')
        fh.write('\n')
        fh.write('\n')
        fh.write('    "links": [')
        fh.write('\n')
        # 接着写入所有的边
        for j in range(result_len):
            fh.write('    {')
            fh.write('\n')
            fh.write('        "source": "' + item + '",')
            fh.write('\n')
            fh.write('        "target": "' + res_2[0][j] + '",')
            fh.write('\n')
            fh.write('        "name": "' + res_2[1][j] + '",')
            fh.write('\n')
            fh.write('        "des": "link_' + str(j + 1) + '"')
            fh.write('\n')
            if j != result_len - 1:
                fh.write('    },')
            else:
                fh.write('    }')
            fh.write('\n')
        fh.write('    ]')
        fh.write('\n')
        fh.write('}')
        fh.write('\n')
        fh.close()

    result2echarts(sparql_sents)
    eel.reload_html()



@eel.expose
def python_test():
    print(1)


entity = eel.read_str()()
# Query(entity)


eel.start('echarts_visual.html')
