import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gml("lesmiserables.gml")

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='lightgray', linewidths=5, font_size=10)
plt.show()

nx.write_graphml(G, "lesmiserables.graphml")
print("Граф збережено у файл 'lesmiserables.graphml'")