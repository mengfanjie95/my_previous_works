from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm
import pandas as pd

browser = webdriver.Chrome()

text_file_path_1 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\news_scription.txt'
text_file_path_2 = 'D:\文件夹汇总\项目\军事知识图谱\爬虫\环球军事网\huanqiu_1\\news.txt'
file_1 = open(text_file_path_1, 'r', encoding='UTF-8')
file_2 = open(text_file_path_2, 'a+', encoding='UTF-8')
lines = file_1.readlines()
# df = pd.read_excel(excel_file_path).astype(str)
n = int(len(lines) / 4) - 1
print(n)
for i in tqdm(range(n)):
    try:
        title = lines[4 * i].strip()
        link = lines[4 * i + 1].strip()
        summary = lines[4 * i + 2].strip()
        browser.get(link)
        paper = browser.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[1]/div[1]/article/section')
        content = paper.text.strip()
        file_2.write(title)
        file_2.write('\n')
        file_2.write(link)
        file_2.write('\n')
        file_2.write(summary)
        file_2.write('\n')
        file_2.write(content)
        file_2.write('\n')
        file_2.write('\n')
    except:
        print(title)

    time.sleep(5)
