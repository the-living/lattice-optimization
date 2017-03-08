from latoptim.graph import lines2graph
from latoptim.optimize import optimize

import os, json


path = "\\".join(os.path.dirname(os.path.realpath(__file__)).split("\\")[:]) + "\\"

with open(path + "model.txt") as f:
    lines_input = json.loads(f.read())

# parameters for graph computation
target = 0.5
min_radius = 0.5
max_radius = 3.0
def_radius = 1.0
speed = 0.1
epsilon = .01


print("generating graph...")


graph = lines2graph(lines_input, def_radius, epsilon)

print("graph nodes:", len( graph.get_nodes() ))
print("graph edges:", graph.get_edges())

graph = optimize(graph, target, min_radius, max_radius, speed)

# validate graph
