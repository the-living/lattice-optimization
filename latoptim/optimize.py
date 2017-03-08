from latoptim.simulate import computeModel, getNastranModel

def optimize(graph, target, minRadius, maxRadius, speed):

    step = 0
    terminated = False

    while not terminated:

        # 1. convert graph to Natran model
        nas_model = getNastranModel(graph)

        # 2. run simulation in nastran and return results
        results = computeModel(nas_model)

        # 3. write Nastran results to graph
        graph.set_stress_values(results)

        # 4. compute optimization step
        converged = compute(graph, target, minRadius, maxRadius, speed)

        step += 1

        #termination criteria
        if converged or step > 25:
            terminated = True

    return graph

def compute(self, target, minRadius, maxRadius, speed):
        # for node1 in graph["edges"].keys():
        #       for node2 in graph["edges"][node1].keys():
        #           edge = graph["edges"][node1][node1]

        #           if not edge["active"]:
        #               continue

        #           edge["radius"] += speed * (edge["stress"] - target) * (maxRadius - minRadius)

        #           edge["radius"] = min(edge["radius"], maxRadius)

        #           if edge["radius"] < minRadius:
        #               edge["active"] = False

        #           if edge["radius"] > maxRadius:
        #               continue
        #               # add edge
        #   termination = True
        return True