from text2graphapi.src.Cooccurrence import Cooccurrence
from prettytable import PrettyTable

import nltk
nltk.download('omw-1.4')

corpus_docs = [
    {'id': 1, 'doc': "The sun was shining, making the river look bright and happy."},
    {'id': 2, 'doc': "Even with the rain, the sun came out a bit, making the wet river shine."}
]

to_word_coocc_graph = Cooccurrence(graph_type = 'DiGraph', 
    language = 'en', 
    window_size = 3, output_format = 'adj_matrix')
to_word_coocc_graph_transformed = to_word_coocc_graph.transform(corpus_docs)

print("_"*100)
output_table = PrettyTable(to_word_coocc_graph_transformed[0].keys())

for word_coocc_graph_transformed in to_word_coocc_graph_transformed:
    output_table.add_row(word_coocc_graph_transformed.values())

print(output_table)