# this script is NOT to be sent or run in Rhino.

from compas.datastructures import Network

import compas
from compas_plotters import NetworkPlotter

network = Network.from_json("C:\\Users\\uk083720\\Documents\\dliu\\04_Code\\\\CompasCEM\\compas_cem\\src\\compas_cem\\ghpython\\WIP\\network.json")



plotter = NetworkPlotter(network)
plotter.draw_nodes(
    text='key',
    facecolor={key: '#ff0000' for key in network.leaves()},
    radius=.2
)
plotter.draw_edges(text='key')
plotter.show()

print(network.to_data())
network.count_crossings()

# keys are mutable
network.edge_length(1, 2)
network.edge_length(2, 1)

# define constraints and loads (are loads necessary??)
print(network.node_attributes())

print(network.adjacency)
print(network.adjacency_matrix())
print(network.connectivity_matrix())

print(network.degree_matrix())
network.add_edge(2, 0)
network.add_edge(1, 3)

print(network.degree_matrix())
network.delete_edge(1, 3)


