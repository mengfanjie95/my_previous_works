import xmltodict
import json
xml_path = '/Users/mengfanjie/Desktop/毕业/wiki/zhwiki-latest-pages-articles.xml'
json_path = '/Users/mengfanjie/Desktop/毕业/wiki/zhwiki-latest-pages-articles.json'
xml_file = open(xml_path,'r')
json_file = open(json_path,'w')
xml_str = xml_file.read()
xml2json = xmltodict.parse(xml_str,encoding='UTF-8')
json_str = json.dumps(xml2json)

json_file.write(json_str)