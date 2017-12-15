




# classe para armazenar os dados do arquivo csv
class csv_dados():
    def __init__(self,classifier):
        self.rows = []
        self.atributes = []
        self.atribute_types = []
        self classifier = classifier
        self.class_col_index = None

#classe que constroi a arvore de decisao
class decisionTreeNode():

    def __init__(self, is_leaf_node, classification, attribute_split_index,attribute_split_value, parent, left_child, right_child, height):
        self.classification = None
        self.attribute_split = None
        self.attribute_split_index = None
        self.attribute_split_value