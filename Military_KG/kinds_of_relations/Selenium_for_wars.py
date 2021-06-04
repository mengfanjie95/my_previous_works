# 从wars.txt中读取战争名称，并输入到百科的搜索框中进行搜索
# 对搜索结果中的infobox中的信息进行爬取并分别存储到对应的txt文件中
from selenium import webdriver
import os
import time
from tqdm import tqdm

browser = webdriver.Chrome()

# 读取战争的名称
war_names_file = 'wars.txt'
fh_1 = open(war_names_file,'r',encoding='UTF-8')
wars = fh_1.readlines()

# 打开存储战争信息的txt文件
fh_2 = open('wars_info.txt','a+',encoding='UTF-8')


# 对每个战役分别进行爬虫并存储到单独的文件中
for war in tqdm(wars):
    fh_2.write('#' + war.strip())
    fh_2.write('\n')
    browser.get("https://baike.baidu.com/")
    Query_box = '//*[@id="query"]'
    Find_query_box = browser.find_element_by_xpath(Query_box)
    Find_query_box.send_keys(war.strip())
    Click_button = '//*[@id="search"]'
    Start_search = browser.find_element_by_xpath(Click_button)
    Start_search.click()
    time.sleep(5)
    sreach_window = browser.current_window_handle
    infobox_length = len(browser.find_elements_by_class_name("basicInfo-item.name"))
    for i in range(infobox_length):
        fh_2.write('$' +browser.find_elements_by_class_name("basicInfo-item.name")[i].text.strip())
        fh_2.write('\n')
        fh_2.write(browser.find_elements_by_class_name("basicInfo-item.value")[i].text.strip())
        fh_2.write('\n')
        fh_2.write('\n')

    # print(browser.current_url)
    # print(len(browser.find_elements_by_class_name("basicInfo-item.name")))
    # print(browser.find_elements_by_class_name("basicInfo-item.name")[19].text)
fh_2.close()







