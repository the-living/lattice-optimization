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
        self.displacement = 0
        self.weight = 0

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

    def bakeResults(self, results):

        return None


def lines2graph(lines, defRadius, epsilon):

    graph = Graph()

    for line in lines:
        graph.addEdge(line, defRadius, epsilon)

    return graph

