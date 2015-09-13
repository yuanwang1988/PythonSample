from GraphClasses import Node, Edge, Graph, SparseMatrix, DenseMatrix

def FloydWarshall(a_graph):
	num_of_vertices = a_graph.num_vertices
	subsol_0 = DenseMatrix(num_of_vertices, num_of_vertices)

	for vertex_a_id in a_graph.vertex_dic:
		for vertex_b_id in a_graph.vertex_dic:
			if vertex_a_id == vertex_b_id:
				subsol_0.set_val(vertex_a_id, vertex_b_id, 0)
			else: 
				edge_ab = a_graph.find_edge(vertex_a_id, vertex_b_id)
				if edge_ab != None:
					subsol_0.set_val(vertex_a_id, vertex_b_id, edge_ab.edge_cost)
				else: 
					subsol_0.set_val(vertex_a_id, vertex_b_id, float('inf'))


	subsol_k = subsol_0

	for k in range(1, len(a_graph.vertex_dic)):
		subsol_kminus1 = subsol_k
		subsol_k = FloydWarshall_itr(a_graph, k, subsol_kminus1)
		print(k)

	return subsol_k


def FloydWarshall_itr(a_graph, k, subsol_kminus1):
	num_of_vertices = a_graph.num_vertices
	subsol_k = DenseMatrix(num_of_vertices, num_of_vertices)

	for vertex_a_id in a_graph.vertex_dic:
		for vertex_b_id in a_graph.vertex_dic:
			path_ab_kminus1_cost = subsol_kminus1.read_val(vertex_a_id, vertex_b_id)
			path_akb_cost = subsol_kminus1.read_val(vertex_a_id, k) + subsol_kminus1.read_val(k, vertex_b_id)

			path_ab_k_cost = min(path_ab_kminus1_cost, path_akb_cost)

			subsol_k.set_val(vertex_a_id, vertex_b_id, path_ab_k_cost)

	return subsol_k








