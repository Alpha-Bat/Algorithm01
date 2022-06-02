def solution(progresses, speeds):
    answer = []
    # 우선 남은 작업일수를 리스트로 만들어준다. (days)
    lefts = []
    for progress in progresses :
        lefts.append(100-progress) # lefts에 남은 작업량을 append
    days = []
    for idx, left in enumerate(lefts) :
        n = int(left/speeds[idx]) # 남은 작업량에 작업속도를 나눈다
        if left%speeds[idx] != 0 : # 정확히 나눠지지 않은 값은 int로 버림했기 때문에 작업일을 하루 더해준다.
            n += 1
        days.append(n) # 결과 n이 남은 작업일수를 뜻하므로 days에 append 해준다
    # days를 스택으로 활용
    day = days.pop(0) # 우선 첫번째 기능이 필요한 작업일수를 pop을 이용해 day로 꺼내준다.
    n = 1 # 첫번째 기능은 무조건적으로 day일후 배포가능하므로 우선 1을 넣어준다.
    while days : # days를 모두 사용할때까지 반복   
        if day >= days[0] : # 현재 기준인 기능(day)보다 다음 기능(days[0])이 먼저 완성됐다면
            n += 1 # 같이 배포될 기능의 개수를 하나 올려주고
            days.pop(0) # 그 기능을 제거 (day에 저장하지 않음)
        else : # 현재 기준인 기능(day)보다 다음 기능(days[0])이 이후에 완성된다면
            answer.append(n) # 배포될 기능의 개수인 n을 answer에 append 해준다.
            day = days.pop(0) # 다음 기능이 필요한 작업일수를 pop을 이용해 day로 꺼내준다.
            n = 1 # 이 기능도 day일후 배포가능하므로 우선 1을 넣어준다.
    answer.append(n) # 마지막으로 배포될 기능의 개수 n을 append 해준다.
    return answer
