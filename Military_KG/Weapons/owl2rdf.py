import os
from tqdm import tqdm
file_path_1 = '/Users/mengfanjie/项目/军事知识图谱/bootstraping_extraction/Weapons/txts1/'
file_path_2 = '/Users/mengfanjie/项目/军事知识图谱/bootstraping_extraction/Weapons/txts2/'

txts = os.listdir(file_path_1)


# classassertion + individual declaration + objectpropertyassertion
# + datapropertyassertion== individual

# dataproperty declaration + data domain + data range == data property

# 打开需要用到的文件
fh_dataproperty_declaration = open(file_path_1 + 'Dataproperty_declaration.txt', 'r', encoding='UTF-8')
fh_dataproperty_domain = open(file_path_1 + 'Dataproperty_domain.txt', 'r', encoding='UTF-8')
fh_dataproperty_range = open(file_path_1 + 'Dataproperty_range.txt', 'r', encoding='UTF-8')

fh_individual = open(file_path_1 + 'Individual_declaration.txt', 'r', encoding='UTF-8')
fh_class_assertion = open(file_path_1 + 'Class_assertion.txt', 'r', encoding='UTF-8')
fh_dataproperty_assertion = open(file_path_1 + 'Dataproperty_assertion.txt', 'r', encoding='UTF-8')
fh_objectproperty_assertion = open(file_path_1 + 'Objectproperty_assertion.txt', 'r', encoding='UTF-8')

# 读取文件
lines_dataproperty_declaration = fh_dataproperty_declaration.readlines()
lines_dataproperty_domain = fh_dataproperty_domain.readlines()
lines_dataproperty_range = fh_dataproperty_range.readlines()

lines_individual = fh_individual.readlines()
lines_class_assertion = fh_class_assertion.readlines()
lines_dataproperty_assertion = fh_dataproperty_assertion.readlines()
lines_objectproperty_assertion = fh_objectproperty_assertion.readlines()

# 打开新的文件
fh_new_dataproperty = open(file_path_2 + 'data_property.txt', 'w', encoding="UTF-8")
fh_new_individual = open(file_path_2 + 'individual.txt', 'w', encoding="UTF-8")

# 先进行dataproperty的部分
data_propertys = []
declaration_length = int(len(lines_dataproperty_declaration) / 4) - 1
domain_length = int(len(lines_dataproperty_domain) / 5) - 1

# 存储所有的dataproperty
for i in range(declaration_length):
    data_property = lines_dataproperty_declaration[4 * i + 1].strip().split('"')[1][1:]
    if data_property not in data_propertys:
        data_propertys.append(data_property)
# print(data_propertys, len(data_propertys))

# 对每个dataproperty进行domain和range的遍历
for i in range(len(data_propertys)):
    domains = []  # data_property_domain
    ranges = []  # data_property_range
    data_property = data_propertys[i]
    for k in range(domain_length):
        if lines_dataproperty_domain[5 * k + 1].strip().split('"')[1][1:] == data_property:
            data_domain = lines_dataproperty_domain[5 * k + 2].strip().split('"')[1][1:]
            if data_domain not in domains:
                domains.append(data_domain)
        if lines_dataproperty_range[5 * k + 1].strip().split('"')[1][1:] == data_property:
            data_range = lines_dataproperty_range[5 * k + 2].strip().split('"')[1][4:]
            if data_range not in ranges:
                ranges.append(data_range)
    # 将语句写到文件中
    fh_new_dataproperty.write(
        '    <!-- http://www.semanticweb.org/mengfanjie/ontologies/2020/1/untitled-ontology-10#' + data_property + ' -->')
    fh_new_dataproperty.write('\n')
    fh_new_dataproperty.write('\n')
    fh_new_dataproperty.write(
        '    <owl:DatatypeProperty rdf:about="http://www.semanticweb.org/mengfanjie/ontologies/2020/1/untitled-ontology-10#')
    fh_new_dataproperty.write(data_property + 'Gender">')
    fh_new_dataproperty.write('\n')
    for item in domains:
        fh_new_dataproperty.write(
            '        <rdfs:domain rdf:resource="http://www.semanticweb.org/mengfanjie/ontologies/2020/1/untitled-ontology-10#')
        fh_new_dataproperty.write(item + '"/>')
        fh_new_dataproperty.write('\n')
    for item in ranges:
        fh_new_dataproperty.write('        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#')
        fh_new_dataproperty.write(item + '"/>')
        fh_new_dataproperty.write('\n')
    fh_new_dataproperty.write('    </owl:DatatypeProperty>')
    fh_new_dataproperty.write('\n')
    fh_new_dataproperty.write('\n')
    fh_new_dataproperty.write('\n')
    fh_new_dataproperty.write('\n')
fh_new_dataproperty.close()

# 再进行individual的部分
individuals = []
individual_length = int(len(lines_individual) / 4) - 1
class_length = int(len(lines_class_assertion) / 5) - 1
object_length = int(len(lines_objectproperty_assertion) / 6) - 1
data_length = int(len(lines_dataproperty_assertion) / 6) - 1

# 获取所有的individual
for i in range(individual_length):
    individual = lines_individual[4 * i + 1].strip().split('"')[1][1:]
    if individual not in individuals:
        individuals.append(individual)

# 对每个individual在每个项目里进行遍历
for individual in tqdm(individuals):
    class_name = ''  # class_assertion
    object_name = ''  # object_property
    tail_entity = ''  # tail_entity
    datas = []  # data_property
    contents = [] # data_property_contents

    # 处理class_assertion
    for k in range(class_length):
        # if len(lines_class_assertion[5 * k + 2].strip().split('"')) == 1:
        #     print(lines_class_assertion[5 * k + 2],k)
        if lines_class_assertion[5 * k + 2].strip().split('"')[1][1:] == individual:
            if lines_class_assertion[5 * k + 1].strip().split('"')[1][1:] != '国家/地区':
                class_name = lines_class_assertion[5 * k + 1].strip().split('"')[1][1:]


    # 处理objectproperty_assertion
    for k in range(object_length):
        if lines_objectproperty_assertion[6 * k + 3].strip().split('"')[1][1:] == individual:
            object_name = lines_objectproperty_assertion[6 * k + 1].strip().split('"')[1][1:]
            tail_entity = lines_objectproperty_assertion[6 * k + 2].strip().split('"')[1][1:]


    # 处理dataproperty_assertion
    for k in range(data_length):
        if lines_dataproperty_assertion[6 * k + 2].strip().split('"')[1][1:] == individual:
            data = lines_dataproperty_assertion[6 * k + 1].strip().split('"')[1][1:]
            content = lines_dataproperty_assertion[6 * k + 3].strip().split('<')[1].split('>')[1]
        if data not in datas:
            datas.append(data)
            contents.append(content)

    # 将语句写到文件中
    fh_new_individual.write('    <!-- http://www.semanticweb.org/mengfanjie/ontologies/2020/1/untitled-ontology-10#')
    fh_new_individual.write(individual + ' -->')
    fh_new_individual.write('\n')
    fh_new_individual.write('\n')
    fh_new_individual.write('    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mengfanjie/ontologies/2020/1/untitled-ontology-10#')
    fh_new_individual.write(individual + '">')
    fh_new_individual.write('\n')
    fh_new_individual.write('        <rdf:type rdf:resource="http://www.semanticweb.org/mengfanjie/ontologies/2020/1/untitled-ontology-10#')
    fh_new_individual.write(class_name + '"/>')
    fh_new_individual.write('\n')
    fh_new_individual.write('        <untitled-ontology-10:HasCountryOfOrigin rdf:resource="http://www.semanticweb.org/mengfanjie/ontologies/2020/1/untitled-ontology-10#')
    fh_new_individual.write(tail_entity + '"/>')
    fh_new_individual.write('\n')
    for k in range(len(datas)):
        fh_new_individual.write('        <untitled-ontology-10:')
        fh_new_individual.write(datas[k] + '>' + contents[k] + '</untitled-ontology-10:' + datas[k] + '>')
        fh_new_individual.write('\n')
    fh_new_individual.write('    </owl:NamedIndividual>')
    fh_new_individual.write('\n')
    fh_new_individual.write('\n')
    fh_new_individual.write('\n')
    fh_new_individual.write('\n')

fh_new_individual.close()
