import os, json


class Node:

    def __init__(self, coords, stress):
        self.coords = coords
        self.stress = stress

    def get_coords(self):
        return self.coords

    def get_dist(self, p):
        p2 = self.get_coords()
        return ((p[0] - p2[0])**2 + (p[1] - p2[1])**2 + (p[2] - p2[2])**2) ** .5


class Edge:

    def __init__(self, node1, node2, stress, radius, active):
        self.stress = stress
        self.radius = radius
        self.active = active
        self.node1 = node1
        self.node2 = node2

    def get_node_coords(self):
        return [self.node1.get_coords(), self.node2.get_coords()]

    def get_nodes(self):
        return [self.node1, self.node2]

    def set_stress(self, stress):
        self.stress = stress

    def get_stress(self):
        return self.stress

    def set_active(self, active):
        self.active = active

    def get_active(self):
        return self.active

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius


class Graph:

    def __init__(self):
        self.nodes = []
        self.edges = []
        self.displacement = 0
        self.weight = 0

    def find_closest_node(self, p, epsilon):
        for node in self.nodes:
            if node.get_dist(p) < epsilon:
                return node
        return None

    def add_node(self, p):
        new_node = Node(p, 0.0)
        self.nodes.append(new_node)
        return new_node

    def get_nodes(self):
        return self.nodes

    def add_edge(self, line, radius, epsilon):
        nodes = []
        for i, p in enumerate(line):
            nodes.append(self.find_closest_node(p, epsilon))
            if nodes[-1] is None:
                nodes[-1] = self.add_node(p)

        newEdge = Edge(nodes[0], nodes[1], 0.0, radius, True)
        self.edges.append(newEdge)

    def get_edges(self):
        return self.edges

    def set_stress_values(self, results, indx):
        edges = self.get_edges()
        for i, index in enumerate(indx):
            edges[index].set_stress(results[i])
        # for i, edge in enumerate(self.edges):
        #     edge.set_stress(results[i])

    def get_edge_data(self):
        output = []
        indx = []
        for i, edge in enumerate(self.get_edges()):
            if edge.get_active():
                output.append([node.get_coords() for node in edge.get_nodes()] + [edge.get_radius()])
                indx.append(i)
        return output, indx


def lines2graph(lines, def_radius, epsilon):

    graph = Graph()

    for line in lines:
        graph.add_edge(line, def_radius, epsilon)

    return graph
