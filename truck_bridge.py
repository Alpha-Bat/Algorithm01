def solution(bridge_length, weight, truck_weights):
    s = len(truck_weights)
    answer = 0
    bridge = []
    tim = []
    goa = []
    while len(goa) != s :
        for idx in range(len(tim)) :
            tim[idx] -= 1
        if tim != [] :
            if tim[0] == 0 :
                tim.pop(0)
                g = bridge.pop(0)
                goa.append(g)
        if truck_weights != [] :
            if sum(bridge) + truck_weights[0] <= weight :
                truck = truck_weights.pop(0)
                bridge.append(truck)
                tim.append(bridge_length)
        answer += 1
    return answer
