from py2neo import Node, Graph, Relationship


class DataToNeo4j:
    """将excel中数据存入neo4j"""

    def __init__(self):
        """建立连接"""
        self.graph = Graph('http://localhost:7474', username='neo4j', password='root')
        # 定义label
        self.invoice_name = '发票名称'
        self.invoice_value = '发票值'
        self.graph.delete_all()

    def create_node(self, node_list_key, node_list_value):
        """建立节点"""
        for k in node_list_key:
            name_node = Node(label=self.invoice_name, name=k)
            self.graph.create(name_node)

        for v in node_list_value:
            value_node = Node(label=self.invoice_value, name=v)
            self.graph.create(value_node)

    def create_relation(self, df_data):
        """建立联系"""
        tx = self.graph.begin()
        for i, row in df_data.iterrows():
            tx.evaluate('''
                   MERGE (a:发票名称 {property:$name})
                   MERGE (b:发票值 {property:$name2})
                   MERGE (a)-[r:R_TYPE{property:$p}]->(b)
                   ''', parameters={'name': row['name'],
                                    'name2': row['name2'],
                                    'p': row['relation']})

        tx.commit()

        # rel = Relationship(self.graph.nodes.match(label=self.invoice_name,
        #                                           property_key='name',
        #                                           property_value=df_data['name'][m]),
        #                    df_data['relation'][m],
        #                    self.graph.nodes.match(label=self.invoice_value,
        #                                           property_key='name2',
        #                                           property_value=df_data['name2'][m]))
        # print(rel, m)
        # self.graph.create(rel)
