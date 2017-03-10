from latoptim.simulate import compute_nastran_model, get_nastran_model


def optimize(graph, target, min_radius, max_radius, speed, maxSteps, fp_new_nas):

    step = 0
    terminated = False

    while not terminated:

        print("starting step", step)

        # 1. convert graph to Natran model
        nas_model = get_nastran_model(graph.get_edge_data())

        # 2. run simulation in nastran and return results
        results = compute_nastran_model()
        results = [x[1] for x in results]

        # 3. write Nastran results to graph
        graph.set_stress_values(results)

        # 4. compute optimization step
        converged = compute(graph, target, min_radius, max_radius, speed)

        step += 1

        #termination criteria
        if converged or step == maxSteps:
            terminated = True

    return graph


def compute(graph, target, min_radius, max_radius, speed):

    total_deviation = 0.0

    for edge in graph.get_edges():
        if not edge.get_active():
            continue

        print ("-----")

        print ("start radius", edge.get_radius())

        print ("stress", edge.get_stress())

        deviation = edge.get_stress() - target
        print ("deviation", deviation)

        adjustment = speed * deviation * (max_radius - min_radius)

        print ("adjustment", adjustment)

        radius = edge.get_radius() + adjustment
        #clamp
        radius = max(min(radius, max_radius), min_radius)
        radius = int(radius * 10) / 10.0

        print ("radius", radius)

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
