def solution(bridge_length, weight, truck_weights):
    s = len(truck_weights) # 트럭의 수
    answer = 0
    bridge = [] # 다리에 있는 트럭 (Queue 방식)
    tim = [] # 다리에 있는 트럭이 지나갈때까지 남은 시간 (Queue 방식)
    goa = [] # 도착한 트럭
    while len(goa) != s : # 도착한 트럭의 수가 모든 트럭이 아닌동안 계속 반복
        for idx in range(len(tim)) :
            tim[idx] -= 1 # 트럭이 도착하는 시간 -1
        if tim != [] and tim[0] == 0 : # 남은 시간이 0인 트럭이 존재한다면
            tim.pop(0) # 0인 시간(트럭이 도착했다는 의미)을 빼주고 (get)
            g = bridge.pop(0) # 도착한 트럭을 다리에서 빼주고 (get)
            goa.append(g) # 도착한 트럭 리스트에 추가해준다.
        if truck_weights != [] and sum(bridge) + truck_weights[0] <= weight : # 출발할 트럭이 있고 트럭을 추가해도 제한무게 이하라면
            truck = truck_weights.pop(0) # 큐 방식으로 트럭을 빼주고 (get)
            bridge.append(truck) # 그 트럭을 다리위에 올리고 (put)
            tim.append(bridge_length) # 트럭이 다리를 건너는 시간(다리길이)도 추가해준다. (put)
        answer += 1
#         print(answer, truck_weights, bridge, tim, goa) # 같이 실행하면 시간별 현황을 print해서 볼수 있다.
    return answer
