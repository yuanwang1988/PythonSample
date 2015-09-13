#Class Node is a class representing the nodes/vertices in a graph.

class Node:
	def __init__(self, index):
		self.index = index #integer indicating the index of the vertex
		self.out_edge_dic = {} #dictionary of pointers to out_edges, indexed by the string "out:out_vertex_index, in:in_vertex_index"
		self.in_edge_dic = {} #dictionary of pointers to in_edges, indexed by the string "out:out_vertex_index, in:in_vertex_index"

	def add_in_edge(self, an_edge): #add the edge pointer to in_edge_dic
		edge_id_str = edge_id_builder(an_edge.out_vertex_id, an_edge.in_vertex_id)
		self.in_edge_dic[edge_id_str] = an_edge

	def add_out_edge(self, an_edge): #add the edge pointer to out_edge_dic
		edge_id_str = edge_id_builder(an_edge.out_vertex_id, an_edge.in_vertex_id)
		self.out_edge_dic[edge_id_str] = an_edge

	def find_edge_to(self, in_vertex_id): # returns pointer to an edge
		search_str = edge_id_builder(self.index, in_vertex_id)
		try:
			return self.out_edge_dic[search_str]
		except:
			return None

	def find_edge_from(self, out_vertex_id): # returns pointer to an edge
		search_str = edge_id_builder(out_vertex_id, self.index)
		try:
			return self.in_edge_dic[search_str]
		except:
			return None		


#Class Node is a class representing the edges in a graph. 

class Edge:
	def __init__(self, out_vertex_id, in_vertex_id, edge_cost = None):
		self.out_vertex_id = out_vertex_id
		self.in_vertex_id = in_vertex_id
		self.edge_cost = edge_cost

	def get_out_vertex_id(self): #return the index of the out_vertex
		return self.out_vertex_id

	def get_in_vertex_id(self): #return the index of the in_vertex
		return self.in_vertex_id

	def get_edge_cost(self): #return the edge_cost
		return self.edge_cost

	def set_edge_cost(self, new_edge_cost): #set the edge_cost
		self.edge_cost = new_edge_cost


def edge_id_builder(out_vertex_id, in_vertex_id):
	edge_id_str = "out:"+str(out_vertex_id)+",in:"+str(in_vertex_id)
	return edge_id_str


class Graph:
	def __init__(self):
		self.vertex_dic = {} #dictionary with pointers to vertex objects
		self.edge_dic = {} #dictionary with pointers to edge objects
		self.num_vertices = 0
		self.num_edges = 0

	def add_vertex(self, vertex_id): #create a new node object and add a pointer to the object ot vertex_dic
		new_vertex = Node(vertex_id)
		self.vertex_dic[vertex_id] = new_vertex
		self.num_vertices += 1

	def add_edge(self, out_vertex_id, in_vertex_id, edge_cost = None): #update the graph object to add an edge and any new vertices
		new_edge = Edge(out_vertex_id, in_vertex_id, edge_cost)
		new_edge_id_str = edge_id_builder(out_vertex_id, in_vertex_id)
		self.edge_dic[new_edge_id_str] = new_edge
		self.num_edges += 1

		if out_vertex_id not in self.vertex_dic:
			self.add_vertex(out_vertex_id)

		if in_vertex_id not in self.vertex_dic:
			self.add_vertex(in_vertex_id)

		out_vertex_obj = self.vertex_dic[out_vertex_id]
		out_vertex_obj.add_out_edge(new_edge)


		in_vertex_obj = self.vertex_dic[in_vertex_id]
		in_vertex_obj.add_in_edge(new_edge)


	def find_vertex(self, vertex_id): #return pointer to a vertex object
		try:
			return self.vertex_dic[vertex_id]
		except:
			return None

	def find_edge(self, out_vertex_id, in_vertex_id): #return pointer to a edge object
		edge_id_str = edge_id_builder(out_vertex_id, in_vertex_id)
		try:
			return self.edge_dic [edge_id_str]
		except:
			return None

	def build_graph_from_edges(self, list_of_edges): #build graph from a list of edge objects
		for an_edge in list_of_edges:
			self.add_edge(an_edge.out_vertex_id, edge.in_vertex_id, edge.edge_cost)

		print("Graph Built. " + "Number of vertices:" + str(len(self.vertex_dic))+ "; Number of edges:" + str(len(self.edge_dic)))


#SparseMatrix which stores the entries in a matrix in a hashmap;
#This is expected to be more efficient than the DenseMatrix implementation for sparse matrices.
class SparseMatrix:
	def __init__(self):
		self.data = {}

	def set_val(self, **kwargs):
		#the key word argument contains the index (i, j, k, l, ...) and the val
		index_str = self.index_str_builder(kwargs)
		self.data[index_str] = kwargs['val']


	def read_val(self, **kwargs):
		#the key word argument contains the index (i, j, k, l, ...)
		index_str = self.index_str_builder(kwargs)
		
		return self.data[index_str]

	def index_str_builder(self, index_and_val_dic):
		index_str = ""
		index_str_array = []
		for index_name, index_val in index_and_val_dic.items():
			if index_name != 'val':
				index_str_array.append(str(index_name) + ":"+str(index_val))

			index_str = '-'.join(index_str_array)

		return index_str

#DenseMatrix which stores the entries in a matrix in an array; 
#This is expected to be more efficient than the SparseMatrix implementation for dense matrices.
class DenseMatrix:
	def __init__(self, i_size, j_size):
		self.i_size = i_size
		self.j_size = j_size
		self.data = (i_size)*(j_size)*[None]


	def set_val(self, i, j, val):
		self.data[(i-1)*self.j_size+j-1] = val

	def read_val(self, i, j):
		return self.data[(i-1)*self.j_size+j-1]

