from text2graphapi.src.IntegratedSyntacticGraph import ISG
from prettytable import PrettyTable

import nltk
nltk.download('omw-1.4')

corpus_docs = [
        {'id': 1, 'doc': "The sun was shining, making the river look bright and happy."},
        {'id': 2, 'doc': "Even with the rain, the sun came out a bit, making the wet river shine."}
]

to_isg_graph = ISG(graph_type = 'DiGraph',  language = 'en', output_format = 'networkx')
to_isg_graph_transformed = to_isg_graph.transform(corpus_docs)

print("_"*100)
output_table = PrettyTable(to_isg_graph_transformed[0].keys())

for isg_graph_transformed in to_isg_graph_transformed:
    output_table.add_row(isg_graph_transformed.values())

print(output_table)