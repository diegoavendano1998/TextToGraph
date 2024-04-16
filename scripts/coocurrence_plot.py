from text2graphapi.text2graphapi.src.Cooccurrence import Cooccurrence
import nltk




nltk.download('omw-1.4')

input_file = "long_example.txt"
file = open("inputs/"+input_file, "r")
corpus_doc = {"id": 1, "doc": file.read()}

to_word_coocc_graph = Cooccurrence(graph_type = 'DiGraph', 
    language = 'en', 
    window_size = 3, output_format = 'adj_matrix')
to_word_coocc_graph_transformed = to_word_coocc_graph.transform([corpus_doc])

nodes_colors = [degree[1] / 10 for degree in sorted(to_word_coocc_graph_transformed[0]["nx_graph"].degree(), key=lambda tup: tup[0])]
nodes_labels = {}

for node in sorted(to_word_coocc_graph_transformed[0].get("nodes",[]), key=lambda tup: tup[0]):
    nodes_labels[node[0]] = f"{node[0]}\n<{node[1].get('pos_tag')}>"

edge_labels = dict([((nodes_labels[edge_from], nodes_labels[edge_to]), f"freq={frequency.get('freq')}") for edge_from, edge_to, frequency in to_word_coocc_graph_transformed[0].get("edges",[])])
edge_colors = [int((edge_labels[(nodes_labels[edge_from], nodes_labels[edge_to])]).replace("freq=","")) / 10 for edge_from, edge_to in to_word_coocc_graph_transformed[0]["nx_graph"].edges()]
PLOT_OPTIONS = {
    "nodes_colors": nodes_colors,
    "nodes_labels": nodes_labels,
    "edge_labels": edge_labels,
    "edge_colors": edge_colors,
}

to_word_coocc_graph.plot_graph(to_word_coocc_graph_transformed[0]["nx_graph"], "outputs/" + input_file.replace("txt","png"), PLOT_OPTIONS)