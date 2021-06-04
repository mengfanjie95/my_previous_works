# 将处理过的武器的各种dataproperty通过代码的方式写入到owl文件中
# 即生成owl格式的代码，可以直接复制到owl中(先写道txt中，再复制到owl中)
# 需要生成的是owl中关于datapropery的定义以及其domain，range
# individual的添加，三元组的添加

import os
import pandas as pd
from tqdm import tqdm


txt_file_1 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\Weapons\\txts\\Dataproperty_declaration.txt'
txt_file_2 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\Weapons\\txts\\Individual_declaration.txt'
txt_file_3 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\Weapons\\txts\\Class_assertion.txt'
txt_file_4 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\Weapons\\txts\\Objectproperty_assertion.txt'
txt_file_5 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\Weapons\\txts\\Dataproperty_domain.txt'
txt_file_6 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\Weapons\\txts\\Dataproperty_range.txt'
txt_file_7 = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\Weapons\\txts\\Dataproperty_assertion.txt'



Dataproperty_declaration = open(txt_file_1,'w',encoding='utf-8')
Individual_declaration = open(txt_file_2,'w',encoding='utf-8')
Class_assertion = open(txt_file_3,'w',encoding='utf-8')
Objectproperty_assertion = open(txt_file_4,'w',encoding='utf-8')
Dataproperty_domain = open(txt_file_5,'w',encoding='utf-8')
Dataproperty_range = open(txt_file_6,'w',encoding='utf-8')
Dataproperty_assertion = open(txt_file_7,'w',encoding='utf-8')





nations = ('中国 中 丹麦 乌克兰 以色列 伊拉克 伊朗 俄罗斯 俄 保加利亚 利比亚 加拿大 加 卡塔尔 印度 印 印度尼西亚 印尼 '+
           '叙利亚 古巴 哥伦比亚 土耳其 委内瑞拉 巴基斯坦 巴勒斯坦 巴西 希腊 德国 意大利 挪威 新西兰 日本 日 朝鲜 柬埔寨 '+
           '比利时 沙特阿拉伯 法国 波兰 泰国 澳大利亚 瑞士 科威特 秘鲁 缅甸 罗马尼亚 美国 美 老挝 英国 荷兰 菲律宾 葡萄牙 '+
           '蒙古 西班牙 越南 阿富汗 阿根廷 韩国 韩 马来西亚 黎巴嫩').split()

files_directory = 'D:\文件夹汇总\项目\军事知识图谱\\bootstraping_extraction\Weapons\\types'
files = os.listdir(files_directory)

for file in tqdm(files):
    print(file)
    excel_path = files_directory + '\\' + file.strip()
    df = pd.read_excel(excel_path).astype(str)
    length = len(df)
    columns = list(df.columns)
    columns_num = len(columns)

    # 完成对dataproperty的定义以及domain，range的限定
    for i in range(columns_num):
        column_name = df.iat[0,i]
        if column_name not in ['Height','Length','Weight','Width','Country_of_origin','Name']:
            Dataproperty_declaration.write('    <Declaration>')
            Dataproperty_declaration.write('\n')
            Dataproperty_declaration.write('       <DataProperty IRI="#' + column_name + '"/>')
            Dataproperty_declaration.write('\n')
            Dataproperty_declaration.write('    </Declaration>')
            Dataproperty_declaration.write('\n')
            Dataproperty_declaration.write('\n')
            Dataproperty_domain.write('    <DataPropertyDomain>')
            Dataproperty_domain.write('\n')
            Dataproperty_domain.write('        <DataProperty IRI="#' + column_name + '"/>')
            Dataproperty_domain.write('\n')
            Dataproperty_domain.write('        <Class IRI="#' + file[:-5] + '"/>')
            Dataproperty_domain.write('\n')
            Dataproperty_domain.write('    </DataPropertyDomain>')
            Dataproperty_domain.write('\n')
            Dataproperty_domain.write('\n')
            Dataproperty_range.write('    <DataPropertyRange>')
            Dataproperty_range.write('\n')
            Dataproperty_range.write('        <DataProperty IRI="#' + column_name + '"/>')
            Dataproperty_range.write('\n')
            Dataproperty_range.write('        <Datatype abbreviatedIRI="xsd:string"/>')
            Dataproperty_range.write('\n')
            Dataproperty_range.write('    </DataPropertyRange>')
            Dataproperty_range.write('\n')
            Dataproperty_range.write('\n')
        # else:
        #     if column_name not in ['Country_of_origin','Name']:
        #         fh2.write('    <DataPropertyDomain>')
        #         fh2.write('\n')
        #         fh2.write('        <DataProperty IRI="#' + column_name + '"/>')
        #         fh2.write('\n')
        #         fh2.write('        <Class IRI="#武器/设备"/>')
        #         fh2.write('\n')
        #         fh2.write('    </DataPropertyDomain>')
        #         fh2.write('\n')
        #         fh2.write('\n')
        #         fh2.write('    <DataPropertyRange>')
        #         fh2.write('\n')
        #         fh2.write('        <DataProperty IRI="#' + column_name + '"/>')
        #         fh2.write('\n')
        #         fh2.write('        <Datatype abbreviatedIRI="xsd:string"/>')
        #         fh2.write('\n')
        #         fh2.write('    </DataPropertyRange>')
        #         fh2.write('\n')
        #         fh2.write('\n')




    # 完成对individual的declaration，两类property的assertion，class和individual的assertion
    for j in range(1,length):
        for k in range(columns_num):
            if df.iat[0,k] == 'Name':
                Individual_declaration.write('    <Declaration>')
                Individual_declaration.write('\n')
                Individual_declaration.write('        <NamedIndividual IRI="#' + df.iat[j,k] + '"/>')
                Individual_declaration.write('\n')
                Individual_declaration.write('    </Declaration>')
                Individual_declaration.write('\n')
                Individual_declaration.write('\n')
                Class_assertion.write('    <ClassAssertion>')
                Class_assertion.write('\n')
                Class_assertion.write('        <Class IRI="#' + file[:-5] + '"/>')
                Class_assertion.write('\n')
                Class_assertion.write('        <NamedIndividual IRI="#' + df.iat[j,k] + '"/>')
                Class_assertion.write('\n')
                Class_assertion.write('    </ClassAssertion>')
                Class_assertion.write('\n')
                Class_assertion.write('\n')

            # 完成对武器类的objectproperty的assertion
            if df.iat[0,k] == 'Country_of_origin':
                if df.iat[j,k] not in nations:
                    Individual_declaration.write('    <Declaration>')
                    Individual_declaration.write('\n')
                    Individual_declaration.write('        <NamedIndividual IRI="#' + df.iat[j,k] + '"/>')
                    Individual_declaration.write('\n')
                    Individual_declaration.write('    </Declaration>')
                    Individual_declaration.write('\n')
                    Individual_declaration.write('\n')
                    Class_assertion.write('    <ClassAssertion>')
                    Class_assertion.write('\n')
                    Class_assertion.write('        <Class IRI="#国家/地区"/>')
                    Class_assertion.write('\n')
                    Class_assertion.write('        <NamedIndividual IRI="#' + df.iat[j,k] + '"/>')
                    Class_assertion.write('\n')
                    Class_assertion.write('    </ClassAssertion>')
                    Class_assertion.write('\n')
                    Class_assertion.write('\n')

                    Objectproperty_assertion.write('    <ObjectPropertyAssertion>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('        <ObjectProperty IRI="#Produce"/>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('        <NamedIndividual IRI="#' + df.iat[j,k] + '"/>')
                    Objectproperty_assertion.write('\n')
                    name_index = df.columns.get_loc('名称')
                    Objectproperty_assertion.write('        <NamedIndividual IRI="#' + df.iat[j,name_index] + '"/>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('    </ObjectPropertyAssertion>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('\n')

                    Objectproperty_assertion.write('    <ObjectPropertyAssertion>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('        <ObjectProperty IRI="#HasCountryOfOrigin"/>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('        <NamedIndividual IRI="#' + df.iat[j,name_index] + '"/>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('        <NamedIndividual IRI="#' + df.iat[j,k] + '"/>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('    </ObjectPropertyAssertion>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('\n')


                else:
                    Objectproperty_assertion.write('    <ObjectPropertyAssertion>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('        <ObjectProperty IRI="#Produce"/>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('        <NamedIndividual IRI="#' + df.iat[j,k] + '"/>')
                    Objectproperty_assertion.write('\n')
                    name_index = df.columns.get_loc('名称')
                    Objectproperty_assertion.write('        <NamedIndividual IRI="#' + df.iat[j,name_index] + '"/>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('    </ObjectPropertyAssertion>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('\n')

                    Objectproperty_assertion.write('    <ObjectPropertyAssertion>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('        <ObjectProperty IRI="#HasCountryOfOrigin"/>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('        <NamedIndividual IRI="#' + df.iat[j,name_index] + '"/>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('        <NamedIndividual IRI="#' + df.iat[j,k] + '"/>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('    </ObjectPropertyAssertion>')
                    Objectproperty_assertion.write('\n')
                    Objectproperty_assertion.write('\n')

            # 完成对dataproperty中的具体值的添加
            else:
                if df.iat[j,k] != 'nan':
                    Dataproperty_assertion.write('    <DataPropertyAssertion>')
                    Dataproperty_assertion.write('\n')
                    Dataproperty_assertion.write('        <DataProperty IRI="#' + df.iat[0 ,k] + '"/>')
                    Dataproperty_assertion.write('\n')
                    name_index = df.columns.get_loc('名称')
                    Dataproperty_assertion.write('        <NamedIndividual IRI="#' + df.iat[j,name_index] + '"/>')
                    Dataproperty_assertion.write('\n')
                    Dataproperty_assertion.write('        <Literal>' + df.iat[j,k] + '</Literal>')
                    Dataproperty_assertion.write('\n')
                    Dataproperty_assertion.write('    </DataPropertyAssertion>')
                    Dataproperty_assertion.write('\n')
                    Dataproperty_assertion.write('\n')


Dataproperty_declaration.close()
Individual_declaration.close()
Class_assertion.close()
Objectproperty_assertion.close()
Dataproperty_domain.close()
Dataproperty_range.close()
Dataproperty_assertion.close()





