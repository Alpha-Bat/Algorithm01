def solution(progresses, speeds):
    answer = []
    lefts = []
    for progress in progresses :
        lefts.append(100-progress)
    days = []
    for idx, left in enumerate(lefts) :
        n = int(left/speeds[idx])
        if left%speeds[idx] != 0 :
            n += 1
        days.append(n)
    print(days)
    ans = 0
    day = days[0]
    for i in range(len(days)) :
        if day < days[i] :
            answer.append(ans)
            ans = 1
            day = days[i]
        else :
            ans += 1
    answer.append(ans)
    return answer
