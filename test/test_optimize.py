import os, json, time

from latoptim.graph import lines2graph
from latoptim.optimize import optimize

start = time.time()

path = "\\".join(os.path.dirname(os.path.realpath(__file__)).split("\\")[:]) + "\\"

# input_txt = "model_P.txt"			# full model
# input_txt = "model.txt"            # sample truss
input_txt = "model_T.json"            # mini truss


with open(path + input_txt) as f:
    lines_input = json.loads(f.read())

# parameters for graph computation
target = 2000
min_radius = 0.5
max_radius = 3.0
start_radius = 1.0
speed = 0.0001
epsilon = .01
maxSteps = 25


print("generating graph...")


graph = lines2graph(lines_input, start_radius, epsilon)

print("graph nodes:", len( graph.get_nodes() ))
print("graph edges:", len( graph.get_edges() ))

graph = optimize(graph, target, min_radius, max_radius, speed, maxSteps)

print(graph.get_edge_data())



end = time.time()
print("\ni have used up {} seconds of your time optimize'n".format( round(end-start,3) ), "\n" )