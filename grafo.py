from queue import Queue
class Graph:
	def __init__(self, connected=False):
		self.nodes = set()		#coleção com os nós
		self.edges = list()		#lista com todas as arestas
		self.distances = {}		#distancia entre os nós
		self.directed = is_directed

	def add_node(self, node):
		self.nodes.add(node)	#cria e adiciona o nó
		self.edges.append([])   #cria a lista de aresta(relacionamentos do nó)

	#adição de uma aresta/relacionamento com distancia/peso
	def add_edge(self, from_node, to_node, distance):
		self.edges[from_node].append(to_node)	#adiciona o nó'to_node', nos relacionamentos d nó 'from_node'
		self.distance[(from_node,to_node)] = distance #adiciona a distancia entre os nós

		#se ele for não for direcionado
		#o processo tem que ser realizado também se partindo do nó 'to_node'
		if(self.is_directed=False):
			self.edges[to_node].append(from_node)
			self.distances[(to_node,from_node)] = distance

	#adição de uma aresta/relacionamento sem distancia/peso
	def add_edge(se,from_node, to_node):
		self.edges[from_node].append(to_node)	#adiciona o nó'to_node', nos relacionamentos d nó 'from_node'

		#se ele for não for direcionado
		#o processo tem que ser realizado também se partindo do nó 'to_node'
		if(self.is_directed=False):
			self.edges[to_node].append(from_node)
			self.distances[(to_node,from_node)] = distance

	def bfs(self,root):
		visited = set() #coleção com os nós visitados
		queue = Queue()	#fila dos nós a serem percorridos
		tree = list()	#arvore

		#root é o nó raiz, o primeiro a ser visitado
		visited.add(root)		#insere na coleção de visitados o primeiro nó
		queue.put(root)			#insere na lista dos nós a serem percorridos o primeiro nó
		tree.append((root,0))	#se insere na arvore o root, junto com seu grau, que é zero

		degree = 1     #contador para auxiliar na contagem do grau de cada nó 

		#o while permanecerá até que a fila de nós a serem percorridos tenha acabado
		while (queue.empty() == False):
			current = queue.get()  #current recebe o primeiro valor da fila de nós a serem percorridos
			#nesse laço, será percorrido todos os nós adjacentes a current
			for i in self.edges[current]:
				#se i não tiver sido visitado ainda, será inserido em visited, queue e tree
				if(not i in visited):	 
					visited.add(i)		
					queue.put(i)
					tree.append((i,degree))     #em tree, ele é inserido com seu grau
			degree+=1	   #assim que muda de current, o grau irá aumentar
		return tree	

