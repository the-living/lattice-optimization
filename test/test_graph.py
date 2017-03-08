from latoptim.graph import lines2graph
from latoptim.optimize import optimize

import os, json

path = "\\".join(os.path.dirname(os.path.realpath(__file__)).split("\\")[:]) + "\\"

with open(path + "model.txt") as f:
    linesInput = json.loads(f.read())

# parameters for graph computation
target = 0.5
minRadius = 0.5
maxRadius = 3.0
defRadius = 1.0
speed = 0.1
epsilon = .01


print("generating graph...")


graph = lines2graph(linesInput, defRadius, epsilon)

print("graph nodes:", len( graph.getNodes() ))
print("graph edges:", graph.getEdges())

graph = optimize(graph, target, minRadius, maxRadius, speed)

# validate graph