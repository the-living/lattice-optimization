import os, json, math

''' GRAPH DATA STRUCTURE

graph = {
	"nodes": [
		"coords": [*x, *y, *z], 
		"ave_stress": *stressValue
	],
	"edges": {
		*node1_index: {
			*node2_index: {
				"stress": *stressValue,
				"radius": *radiusValue,
				"active": True
			}
		}, 
	}
}

'''

class Node:

	def __init__(self, coords, stress):
		self.coords = coords
		self.stress = stress

	def getCoords(self):
		return self.coords

class Edge:

	def __init__(self, node1, node2, stress, radius, active):
		self.stress = stress
		self.radius = radius
		self.active = active
		self.node1 = node1
		self.node2 = node2

	def getNodes(self):
		return [self.node1.getCoords(), self.node2.getCoords()]

class Graph:

	def __init__(self):
		self.nodes = []
		self.edges = []

	def findClosestNode(self, p, epsilon):
		for i, p2 in enumerate(self.nodes):
			if dist(p, p2.getCoords()) < epsilon:
				return p2
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
			edges.append( edge.getNodes() )
		return edges



path = "\\".join(os.path.dirname(os.path.realpath(__file__)).split("\\")[:]) + "\\"

with open(path + "model.txt") as f:
	linesInput = json.loads(f.read())

# parameters for graph computation
target = 0.5
minRadius = 0.5
maxRadius = 3.0
speed = 0.1
epsilon = .01


def dist(pt1, pt2):
	return math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2 + (pt1[2] - pt2[2])**2)

# def findClosest(p1, cloud):
# 	for i, p2 in enumerate(cloud):
# 		if dist(p1, p2) < epsilon:
# 			return i
# 	return None

def lines2graph(lines, defRadius, epsilon):

	# graph = {}
	graph = Graph()
	# graph["nodes"] = []
	# graph["edges"] = {}

	for line in lines:

		graph.addEdge(line, defRadius, epsilon)

		# pos = []

		# for i, p in enumerate(line):

			# pos.append(findClosest(p, graph["nodes"]))
			# if pos[-1] is None:
			# 	pos[-1] = len(graph["nodes"])
			# 	graph["nodes"].append(p)

		# for ps in pos:
		# 	if ps not in graph["edges"].keys():
		# 		graph["edges"][ps] = {}

		# if pos[1] in graph["edges"][pos[0]].keys():
		# 	print "found duplicate line, skipping..."
		# 	continue

		# graph["edges"][pos[0]][pos[1]] = {"stress": 0, "radius": defRadius, "active": True}
		# graph["edges"][pos[1]][pos[0]] = {"stress": 0, "radius": defRadius, "active": True}

	return graph


# function to translate graph design data to Nastran model
def graph2nas(graph):

	#
	model = []

	return model


# function to write Nastran results to graph
def nas2graph(graph, results):

	#

	return graph


# function to simulate model in Nastran
def computeModel(model):

	#
	results = []

	return results

# function to mutate graph based on results
def computeGraph(graph, target, minRadius, maxRadius, speed):

	for node1 in graph["edges"].keys():
		for node2 in graph["edges"][node1].keys():
			edge = graph["edges"][node1][node1]

			if not edge["active"]:
				continue

			edge["radius"] += speed * (edge["stress"] - target) * (maxRadius - minRadius)

			edge["radius"] = min(edge["radius"], maxRadius)

			if edge["radius"] < minRadius:
				edge["active"] = False

			if edge["radius"] > maxRadius:
				continue
				# add edge
	termination = True

	return graph, termination


print "generating graph..."

defRadius = 1.0

graph = lines2graph(linesInput, defRadius, epsilon)

# print len( graph.getNodes() )
# print graph.getEdges()

step = 0
terminated = False

# def runOptimization(graph, target, minRadius, maxRadius, speed, term ):


# while not terminated:

# 	# 1. convert graph to Natran model
# 	model = graph2nas(graph)

# 	# 2. run simulation in nastran and return results
# 	results = computeModel(model)

# 	# 3. write Nastran results to graph
# 	graph = nas2graph(graph, results)
# 	# graph = computeVertexStress(graph)

# 	graph, termination = computeGraph(graph, target, minRadius, maxRadius, speed)

# 	step += 1

# 	#termination criteria
# 	if termination > 0.9 or step > 25:
# 		terminated = True




