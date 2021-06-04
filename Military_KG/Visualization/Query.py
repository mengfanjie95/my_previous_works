import time
from selenium import webdriver


virtuoso_url = 'http://localhost:8890/conductor/'
browser = webdriver.Chrome('/Users/mengfanjie/NLP_script/lib/python3.7/site-packages/selenium/chromedriver')
browser.get(virtuoso_url)

def virtuoso_query(query_sent):
    # 打开conductor页面并登陆
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
    Query_button = browser.find_element_by_xpath('//*[@id="RB"]/div[2]/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td/form/table/tbody/tr[3]/td/input[1]')
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

    return [result_1,result_2]

sent = 'select ?p ?o where {?p ?o  <http://www.semanticweb.org/mengfanjie/ontologies/2020/1/untitled-ontology-10#俄罗斯> }'
print(virtuoso_query(sent))
