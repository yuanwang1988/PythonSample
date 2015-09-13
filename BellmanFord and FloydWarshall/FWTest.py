from GraphClasses import Node, Edge, edge_id_builder, Graph
from BellmanFord import BellmanFord
from FloydWarshall import FloydWarshall
import cProfile

f = open('g3.txt', 'r')

graph_a = Graph()

graph_size_info = f.readline()

stop_counter = 0
stop_limit = 1000
for line in f:
	new_edge_info = line.split(" ")
	new_edge_out_vertex_id = int(new_edge_info[0])
	new_edge_in_vertex_id = int(new_edge_info[1])
	new_edge_cost = int(new_edge_info[2])

	graph_a.add_edge(new_edge_out_vertex_id, new_edge_in_vertex_id, new_edge_cost)

	# stop_counter += 1
	# if stop_counter > stop_limit:
	# 	break

print(graph_size_info)
print([graph_a.num_vertices, graph_a.num_edges])
print([len(graph_a.vertex_dic), len(graph_a.edge_dic)])

# a_edge = graph_a.find_edge(101, 550)

# print([a_edge.out_vertex_id, a_edge.in_vertex_id, a_edge.edge_cost])

# a_node = graph_a.find_vertex(101)
# print([a_node.index, len(a_node.out_edge_dic), len(a_node.in_edge_dic)])
# print(a_node.find_edge_to(550) == a_edge)

# b_node = graph_a.find_vertex(550)
# print([b_node.index, len(b_node.out_edge_dic), len(b_node.in_edge_dic)])
# print(b_node.find_edge_from(101) == a_edge)


cProfile.run('result = FloydWarshall(graph_a)')

print(min(result.data))

# print(graph_a.vertex_dic[2].in_edge_dic)

# shortest_paths_costs = []

# for i in graph_a.vertex_dic:
# 	shortest_paths_from_i_dic = BellmanFord(graph_a, i, 1)
# 	dist_from_i = []
# 	for j in shortest_paths_from_i_dic:
# 		dist_from_i.append(shortest_paths_from_i_dic[j])

# 	shortest_paths_costs.append(min(dist_from_i, key = lambda x: x[1]))





# print(min(shortest_paths_costs, key = lambda x: x[1]))