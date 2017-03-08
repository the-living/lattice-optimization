from latoptim.simulate import compute_nastran_model, get_nastran_model


def optimize(graph, target, min_radius, max_radius, speed):

    step = 0
    terminated = False

    while not terminated:

        # 1. convert graph to Natran model
        nas_model = get_nastran_model(graph)

        # 2. run simulation in nastran and return results
        results = compute_nastran_model(nas_model)

        # 3. write Nastran results to graph
        graph.set_stress_values(results)

        # 4. compute optimization step
        converged = compute(graph, target, min_radius, max_radius, speed)

        step += 1

        #termination criteria
        if converged or step > 25:
            terminated = True

    return graph


def compute(self, target, min_radius, max_radius, speed):
        # for node1 in graph["edges"].keys():
        #       for node2 in graph["edges"][node1].keys():
        #           edge = graph["edges"][node1][node1]

        #           if not edge["active"]:
        #               continue

        #           edge["radius"] += speed * (edge["stress"] - target) * (max_radius - min_radius)

        #           edge["radius"] = min(edge["radius"], max_radius)

        #           if edge["radius"] < min_radius:
        #               edge["active"] = False

        #           if edge["radius"] > max_radius:
        #               continue
        #               # add edge
        #   termination = True
        return True
