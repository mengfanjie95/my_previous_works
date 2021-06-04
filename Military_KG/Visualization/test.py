import time
from selenium import webdriver


browser = webdriver.Chrome('/Users/mengfanjie/NLP_script/lib/python3.7/site-packages/selenium/chromedriver')
virtuoso_url = 'http://localhost:8890/conductor/'
browser.get(virtuoso_url)

# time.sleep(1)
# windows = browser.window_handles
# print(windows)

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
Query_input.send_keys('select count(*) where {?s ?p ?o}')
Query_button = browser.find_element_by_xpath('//*[@id="RB"]/div[2]/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td/form/table/tbody/tr[3]/td/input[1]')
Query_button.click()
result = browser.find_element_by_xpath('//*[@id="rdf_result"]/table/tbody/tr[2]/td/pre')
print(result.text)