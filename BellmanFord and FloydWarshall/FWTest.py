from GraphClasses import Node, Edge, edge_id_builder, Graph
from BellmanFord import BellmanFord
from FloydWarshall import FloydWarshall
import cProfile

#open text file storing the graph structure
f = open('g3.txt', 'r')

#the first line of the text file contains information about the size of the graph
graph_size_info = f.readline()

#construct a graph by reading the edge information from the text file. Each edge (v1, v2, edge cost) is represented by 1 line on the text file
graph_a = Graph()

for line in f:
	new_edge_info = line.split(" ")
	new_edge_out_vertex_id = int(new_edge_info[0])
	new_edge_in_vertex_id = int(new_edge_info[1])
	new_edge_cost = int(new_edge_info[2])

	graph_a.add_edge(new_edge_out_vertex_id, new_edge_in_vertex_id, new_edge_cost)

#run Bellman-Ford Algorithm on the graph
cProfile.run('result = FloydWarshall(graph_a)')

print(min(result.data))

