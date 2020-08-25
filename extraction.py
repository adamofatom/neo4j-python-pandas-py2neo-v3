import connection
import os
import pandas as pd
# import itertools

# 提取excel表格中数据，将其转换成date frame类型
os.chdir('c:\\kus\\neo4test')

invoice_data = pd.read_excel('./datas/Invoice_data_Demo.xls', header=0, encoding='utf8')


# def data_extraction(data=invoice_data, col='发票名称'):
#     """节点数据抽取"""
#
#     # 取出发票名称到list
#     node_list_key = data.loc[:, col].unique()
#
#     # 抽取除了作为节点的列外所有元素作为节点值
#     # 将临时 data_frame 全部转为 str 格式
#     node_list_value = data.iloc[:, 1:].applymap(str).values
#
#     # 再将 data_frame 转化为 set 去除重复值
#     node_list_value = list(set(itertools.chain.from_iterable(node_list_value)))
#
#     return node_list_key, node_list_value


def relation_extraction(data=invoice_data, col='发票名称'):
    """联系数据抽取"""

    df = pd.melt(data, id_vars=[col], value_vars=data.columns[1:],
                 var_name='relation', value_name='name2')
    df = df.applymap(str)
    df = df.rename(columns={col: 'name'})
    print(df)
    return df


# 实例化对象
# data_extraction()
# relation_extraction()
create_data = connection.DataToNeo4j()

# create_data.create_node(data_extraction()[0], data_extraction()[1])
create_data.create_relation(relation_extraction())
