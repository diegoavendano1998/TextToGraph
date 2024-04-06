from text2graphapi.src.Cooccurrence import Cooccurrence
import nltk




nltk.download('omw-1.4')

input_file = "short_example.txt"
file = open("inputs/"+input_file, "r")
corpus_doc = {"id": 1, "doc": file.read()}

to_word_coocc_graph = Cooccurrence(graph_type = 'DiGraph', 
    language = 'en', 
    window_size = 3, output_format = 'adj_matrix')
to_word_coocc_graph_transformed = to_word_coocc_graph.transform([corpus_doc])
to_word_coocc_graph.plot_graph(to_word_coocc_graph_transformed[0]["graph"], "outputs/" + input_file.replace("txt","png"))