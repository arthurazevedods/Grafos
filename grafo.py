from queue import Queue
class Graph:
	def __init__(self, is_directed=False):
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
		if(self.directed == False):
			self.edges[to_node].append(from_node)
			self.distances[(to_node,from_node)] = distance

	#adição de uma aresta/relacionamento sem distancia/peso
	def add_edge(self,from_node, to_node):
		self.edges[from_node].append(to_node)	#adiciona o nó'to_node', nos relacionamentos d nó 'from_node'

		#se ele for não for direcionado
		#o processo tem que ser realizado também se partindo do nó 'to_node'
		if(self.directed == False):
			self.edges[to_node].append(from_node)

	#busca em largura
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
				degree = tree[current][1]+1	#ver qual o grau do nó pai e soma +1 para saber qual o grau atual
				#se i não tiver sido visitado ainda, será inserido em visited, queue e tree
				if(not i in visited):	 
					visited.add(i)		
					queue.put(i)
					tree.append((i,degree))     #em tree, ele é inserido com seu grau
		return tree	

	

	#busca em profundidade
	def visit_dfs(self, visited, stack, tree,degree):
		#o laço se repetirá até a pilha de nós acabar
		while len(stack)!=0:
			current = stack.pop() #current recebe o nó de cima da pilha
			for i in self.edges[current]: #pecorre as arestas do nó corrente
				#se o nó i não tiver sido visitado ainda
				#ele será inserido em visited,stack e tree
				if(not i in visited):
					visited.add(i)
					stack.append(i)
					tree.append((i,(degree)))
				#função recursiva
				t = self.visit_dfs(visited, stack, tree,degree+1)
		return tree

	def dfs(self, root):
		visited = set()	#coleção com os nós visitados
		stack = list()	#pilha com os nós a serem percorridos
		tree = list()	#arvore de busca

		#o nó root(raiz) é inserido na coleção e nas listas
		visited.add(root)
		stack.append(root)
		tree.append((root,0))	#na arvore é inserido o nó e o seu grau
		

		#para percorrer o grafo se usará uma função recursiva
		tree = self.visit_dfs(visited, stack, tree, 1) 
		return tree

	
	#imprimir na tela a busca em profundidade
	def show_bfs(self,root):
		tree = self.bfs(root)
		print('\nBUSCA EM LARGURA:\n')
		for i in tree:
			print('\t> Nó: {}  > Grau:{}'.format(i[0],i[1]))

	#imprimir na tela a busca em profundidade
	def show_dfs(self,root):
		tree = self.dfs(root)
		print('\nBUSCA EM PROFUNDIDADE:\n')
		for i in tree:
			print('\t> Nó: {}  > Grau:{}'.format(i[0],i[1]))

def main():

	vertices, arestas  = input().split()
	grafo = Graph()
	for i in range(int(vertices)):
		grafo.add_node(i)
	for i in range(int(arestas)):
		node, edge = input().split()
		grafo.add_edge(int(node), int(edge))

	grafo.show_bfs(0)	#busca em largura
	grafo.show_dfs(0)	#busca em profundidade
	

main()