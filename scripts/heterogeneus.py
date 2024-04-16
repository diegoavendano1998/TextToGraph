from text2graphapi.text2graphapi.src.Heterogeneous import Heterogeneous
from prettytable import PrettyTable

import nltk
nltk.download('omw-1.4')

corpus_docs = [
    {'id': 1, 'doc': "The sun was shining, making the river look bright and happy."},
    {'id': 2, 'doc': "Even with the rain, the sun came out a bit, making the wet river shine."}
]

to_hetero_graph = Heterogeneous(graph_type = 'Graph', 
    window_size = 20,
    language = 'en', output_format = 'networkx')
to_hetero_graph_transformed = to_hetero_graph.transform(corpus_docs)

print("_"*100)
output_table = PrettyTable(to_hetero_graph_transformed[0].keys())

for hetero_graph_transformed in to_hetero_graph_transformed:
    output_table.add_row(hetero_graph_transformed.values())

print(output_table)