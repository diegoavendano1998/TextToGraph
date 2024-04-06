import networkx as nx
import matplotlib.pyplot as plt

er = nx.erdos_renyi_graph(30, 0.3)
nx.draw(er)
plt.savefig('nxviz_example.png')


from nxviz.plots import MatrixPlot

m = MatrixPlot(er)
m.draw()
plt.savefig('nxviz_example_matrix.png')


from nxviz.plots import ArcPlot

a = ArcPlot(er)
a.draw()
plt.savefig('nxviz_example_arc.png')



from nxviz.plots import CircosPlot

c = CircosPlot(er)
c.draw()
plt.savefig('nxviz_example_circos.png')
