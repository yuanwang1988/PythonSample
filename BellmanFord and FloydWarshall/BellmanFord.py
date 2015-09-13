from GraphClasses import Node, Edge, Graph, SparseMatrix

#This function takes a graph G, the id of the source vertex and the id of the destination vertex and computes the shortest path
#from the source vertex to every other vertex in the graph G using the Bellman-Ford algorithm
def BellmanFord(a_graph, src_vertex_id, dst_vertex_id):
	
	#initialize the subsolution for shortest path from the source vertex to every other vertex in the graph G where the path 
	#contains at most 0 edges
	subsol_0 = {}
	for vertex_id in a_graph.vertex_dic:
		if vertex_id == src_vertex_id:
			subsol_0[vertex_id] = [vertex_id, 0, vertex_id]
		else:
			subsol_0[vertex_id] = [vertex_id, float('inf'), None]

	subsol_k = subsol_0

	#Iteratively, using the subsolution of the shortest path from the source vertex to every other vertex in the graph G where the path contains
	#at most k-1 edges to compute the subsolution of the shortest path from the source vertex to every other vertex in the graph G where 
	#the path contains at most k edges
	for k in range(1, len(a_graph.vertex_dic)+1):
		subsol_kminus1 = subsol_k
		subsol_k = BellmanFord_itr(a_graph, src_vertex_id, dst_vertex_id, subsol_kminus1, k)
		
	#check for negative cycles (i.e if the subsol_n = subsol_n-1). If there is a negative cycle, return None. Otherwise, return the subsol_n-1
	for vertex_id in subsol_k:
		if subsol_k[vertex_id] < subsol_kminus1[vertex_id]:
			return None
		else:
			return subsol_kminus1


#This function computes one iteration of the Bellman Ford algorithm - it takes the subsolution from the previous iteration (k-1) 
#and computes the subsolution for the current iteration (k)
def BellmanFord_itr(a_graph, src_vertex_id, dst_vertex_id, subsol_kminus1 = 0, k = 0):
	subsol_k = {}
	
	#iterate through each vertex in the graph to determine the shortest path containing at most k edges
	for vertex_id, curr_vertex in a_graph.vertex_dic.items():

		potential_subsol = [[vertex_id, subsol_kminus1[vertex_id][1], subsol_kminus1[vertex_id][2]]]

		for in_edge_id, in_edge in curr_vertex.in_edge_dic.items():

			out_vertex_id = in_edge.out_vertex_id
			potential_subsol.append([out_vertex_id, subsol_kminus1[out_vertex_id][1]+in_edge.edge_cost, out_vertex_id])

		best_subsol = min(potential_subsol, key = lambda x: x[1])
		best_subsol[0] = vertex_id

		subsol_k[vertex_id] = best_subsol

	return subsol_k