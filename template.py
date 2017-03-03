terminated = False

''' GRAPH DATA STRUCTURE

graph = {
	"nodes": [
		"coords": [*x, *y, *z], 
	],
	"edges": {
		*node1_index: {
			*node2_index: {
				"stress": *stressValue
			}
		}
	}
}

'''


def lines2graph(lines):

	#
	graph = {}

	return graph


# function to translate graph design data to Nastran model
def graph2nas(graph):

	#
	model = []

	return model


# function to write Nastran results in graph
def nas2graph(graph, results):

	#

	return graph


# function to simulate model in Nastran
def computeMode(model):

	#

	return results

# function to mutate graph based on results
def computeGraph(graph):

	#

	return graph, termination


graph = lines2graph(linesInput)

step = 0

while not terminated:

	# 1. convert graph to Natran model
	model = graph2nas(graph)

	# 2. run simulation in nastran and return results
	results = computeModel(model)

	# 3. write Nastran results to graph
	graph = nas2graph(graph, results)

	graph, termination = compute(graph)

	step += 1

	#termination criteria
	if termination > 0.9 or step > 25:
		terminated = True