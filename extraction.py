import connection
import os
import pandas as pd

# 提取excel表格中数据，将其转换成date frame类型
os.chdir(r'c:\kus\neo4j-python-pandas-py2neo-v3')
invoice_data = pd.read_excel('./data/Invoice_data_Demo.xls', header=0, encoding='utf8')


def relation_extraction(data=invoice_data, col='发票名称'):
    """联系数据抽取"""

    df = pd.melt(data, id_vars=[col], value_vars=data.columns[1:],
                 var_name='relation', value_name='name2')
    df = df.applymap(str)
    df = df.rename(columns={col: 'name'})
    print(df)
    return df


create_data = connection.DataToNeo4j()
create_data.create_relation(relation_extraction())
