''' GRAPH DATA STRUCTURE

graph = {
	"nodes": [
		"coords": [*x, *y, *z], 
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

# parameters for graph computation
param = 0.5
minRadius = 0.5
maxRadius = 3.0
alpha = 0.1

def lines2graph(lines):

	#
	graph = {}

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

	return results

# function to mutate graph based on results
def computeGraph(graph, param, minRadius, maxRadius, alpha):

	for node1 in graph["edges"].keys():
		for node2 in graph["edges"][node1].keys():
			edge = graph["edges"][node1][node1]

			if not edge["active"]:
				continue

			if edge["stress"] < param:
				edge["radius"] -= alpha * (abs(edge["stress"] - param))
			else:
				edge["radius"] += alpha * (abs(edge["stress"] - param))

			if edge["radius"] < minRadius:
				edge["active"] = False

			if edge["radius"] > maxRadius:
				# add edge

	return graph, termination


graph = lines2graph(linesInput)

step = 0
terminated = False
while not terminated:

	# 1. convert graph to Natran model
	model = graph2nas(graph)

	# 2. run simulation in nastran and return results
	results = computeModel(model)

	# 3. write Nastran results to graph
	graph = nas2graph(graph, results)

	graph, termination = computeGraph(graph, param, minRadius, maxRadius, alpha)

	step += 1

	#termination criteria
	if termination > 0.9 or step > 25:
		terminated = True