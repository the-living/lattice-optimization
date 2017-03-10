from latoptim.graph import lines2graph
from latoptim.optimize import optimize
from latoptim.simulate import *

import os, json, time

path = "\\".join(os.path.dirname(os.path.realpath(__file__)).split("\\")[:]) + "\\"

start = time.time()

with open(path + "model_P.txt") as f:
    lines_input = json.loads(f.read())

# parameters for graph computation
target = 0.5
min_radius = 0.5
max_radius = 3.0
def_radius = 1.0
speed = 0.1
epsilon = .01


print("\n\ngenerating graph...\n\n")


graph = lines2graph(lines_input, def_radius, epsilon)
print("graph edges:", graph.get_edge_data()[:20], "\n\n")


nas_model = get_nastran_model(graph.get_edge_data())
print("new nastran written!\n")


results = compute_nastran_model()
# graph = optimize(graph, target, min_radius, max_radius, speed)

# validate graph
end = time.time()
print("\ni have used up {} seconds of your time simulate'n".format( round(end-start,3) ), "\n" )