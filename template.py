import os, json

class Node:

	def __init__(self, coords, stress):
		self.coords = coords
		self.stress = stress

	def getCoords(self):
		return self.coords

	def getDist(self, p):
		p2 = self.getCoords()
		return ((p[0] - p2[0])**2 + (p[1] - p2[1])**2 + (p[2] - p2[2])**2) ** .5

class Edge:

	def __init__(self, node1, node2, stress, radius, active):
		self.stress = stress
		self.radius = radius
		self.active = active
		self.node1 = node1
		self.node2 = node2

	def getNodeCoords(self):
		return [self.node1.getCoords(), self.node2.getCoords()]

class Graph:

	def __init__(self):
		self.nodes = []
		self.edges = []

	def findClosestNode(self, p, epsilon):
		for node in self.nodes:
			if node.getDist(p) < epsilon:
				return node
		return None

	def addNode(self, p):
		newNode = Node(p, 0.0)
		self.nodes.append(newNode)
		return newNode

	def getNodes(self):
		nodes = []
		for node in self.nodes:
			nodes.append( node.getCoords() )
		return nodes

	def addEdge(self, line, radius, epsilon):
		nodes = []
		for i, p in enumerate(line):
			nodes.append(self.findClosestNode(p, epsilon))
			if nodes[-1] is None:
				nodes[-1] = self.addNode(p)

		newEdge = Edge(nodes[0], nodes[1], 0.0, radius, True)
		self.edges.append(newEdge)

	def getEdges(self):
		edges = []
		for edge in self.edges:
			edges.append( edge.getNodeCoords() )
		return edges

	def getNastranModel(self):

		model = []

		return model

	def bakeResults(self, results):

		return None

	def compute(self, target, minRadius, maxRadius, speed):
		# for node1 in graph["edges"].keys():
		# 		for node2 in graph["edges"][node1].keys():
		# 			edge = graph["edges"][node1][node1]

		# 			if not edge["active"]:
		# 				continue

		# 			edge["radius"] += speed * (edge["stress"] - target) * (maxRadius - minRadius)

		# 			edge["radius"] = min(edge["radius"], maxRadius)

		# 			if edge["radius"] < minRadius:
		# 				edge["active"] = False

		# 			if edge["radius"] > maxRadius:
		# 				continue
		# 				# add edge
		# 	termination = True
		return None



path = "\\".join(os.path.dirname(os.path.realpath(__file__)).split("\\")[:]) + "\\"

with open(path + "model.txt") as f:
	linesInput = json.loads(f.read())

# parameters for graph computation
target = 0.5
minRadius = 0.5
maxRadius = 3.0
speed = 0.1
epsilon = .01


def lines2graph(lines, defRadius, epsilon):

	graph = Graph()

	for line in lines:
		graph.addEdge(line, defRadius, epsilon)

	return graph


# function to simulate model in Nastran
def computeModel(model):

	#
	results = []

	return results


def optimize(graph, target, minRadius, maxRadius, speed):

	step = 0
	terminated = False

	while not terminated:

		# 1. convert graph to Natran model
		model = graph.getNastranModel()

		# 2. run simulation in nastran and return results
		results = computeModel(model)

		# 3. write Nastran results to graph
		graph.bakeResults(results)

		# 4. compute optimization step
		termination = graph.compute(target, minRadius, maxRadius, speed)

		step += 1

		#termination criteria
		if termination > 0.9 or step > 25:
			terminated = True



print("generating graph...")

defRadius = 1.0

graph = lines2graph(linesInput, defRadius, epsilon)

print("graph nodes:", len( graph.getNodes() ))
print("graph edges:", graph.getEdges())


graph = optimize(graph, target, minRadius, maxRadius, speed)