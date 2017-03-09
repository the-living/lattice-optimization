import os, json

from latoptim.graph import lines2graph
from latoptim.optimize import optimize


path = "\\".join(os.path.dirname(os.path.realpath(__file__)).split("\\")[:]) + "\\"
fp_new_nas = os.path.join(os.curdir, 'nastran', 'truss_100.nas')

with open(path + "model.txt") as f:
    lines_input = json.loads(f.read())

# parameters for graph computation
target = 435
min_radius = 0.5
max_radius = 2.9
def_radius = 1.0
speed = 0.0001
epsilon = .01
maxSteps = 5


print("generating graph...")


graph = lines2graph(lines_input, def_radius, epsilon)

print("graph nodes:", len( graph.get_nodes() ))
print("graph edges:", len( graph.get_edges() ))

graph = optimize(graph, target, min_radius, max_radius, speed, maxSteps, fp_new_nas)

print(graph.get_edge_data())
