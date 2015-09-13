from GraphClasses import Node, Edge, Graph, SparseMatrix

#This function computes one iteration of the Bellman Ford algorithm - it takes the subsolution from the previous iteration (k-1) and computes the subsolution for the current iteration (k)
def BellmanFord_itr(a_graph, src_vertex_id, dst_vertex_id, subsol_kminus1 = 0, k = 0):
	subsol_k = {}
	#iterate through each vertex in the graph
	for vertex_id, curr_vertex in a_graph.vertex_dic.items():

		potential_subsol = [[vertex_id, subsol_kminus1[vertex_id][1], subsol_kminus1[vertex_id][2]]]

		for in_edge_id, in_edge in curr_vertex.in_edge_dic.items():

			out_vertex_id = in_edge.out_vertex_id
			potential_subsol.append([out_vertex_id, subsol_kminus1[out_vertex_id][1]+in_edge.edge_cost, out_vertex_id])

		best_subsol = min(potential_subsol, key = lambda x: x[1])
		best_subsol[0] = vertex_id

		subsol_k[vertex_id] = best_subsol

	return subsol_k

def BellmanFord(a_graph, src_vertex_id, dst_vertex_id):
	subsol_0 = {}
	for vertex_id in a_graph.vertex_dic:
		if vertex_id == src_vertex_id:
			subsol_0[vertex_id] = [vertex_id, 0, vertex_id]
		else:
			subsol_0[vertex_id] = [vertex_id, float('inf'), None]

	subsol_k = subsol_0

	for k in range(1, len(a_graph.vertex_dic)+1):
		subsol_kminus1 = subsol_k
		subsol_k = BellmanFord_itr(a_graph, src_vertex_id, dst_vertex_id, subsol_kminus1, k)

		if k%100 == 1:
			print(k)
		
	#check for negative cycles
	for vertex_id in subsol_k:
		if subsol_k[vertex_id] < subsol_kminus1[vertex_id]:
			return None

	return subsol_kminus1