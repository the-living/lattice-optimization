from latoptim.simulate import compute_nastran_model, get_nastran_model


def optimize(graph, target, min_radius, max_radius, speed):

    step = 0
    terminated = False

    while not terminated:

        print("starting step", step)

        # 1. convert graph to Natran model
        nas_model = get_nastran_model(graph)

        # 2. run simulation in nastran and return results
        results = compute_nastran_model(nas_model)

        results = [0.1] * 74

        # 3. write Nastran results to graph
        graph.set_stress_values(results)

        # 4. compute optimization step
        converged = compute(graph, target, min_radius, max_radius, speed)

        step += 1

        #termination criteria
        if converged or step > 25:
            terminated = True

    return graph


def compute(graph, target, min_radius, max_radius, speed):

    total_deviation = 0.0

    for edge in graph.get_edges():
        if not edge.get_active():
            continue

        deviation = edge.get_stress() - target

        radius = edge.get_radius() + (speed * deviation * (max_radius - min_radius))
        #clamp
        radius = max(min(radius, max_radius), min_radius)

        edge.set_radius(radius)
        
        #           if edge["radius"] < min_radius:
        #               edge["active"] = False

        #           if edge["radius"] > max_radius:
        #               continue
        #               # add edge

        total_deviation += abs(deviation)
    
    if total_deviation < 5.0:
        return True
    else:
        return False
