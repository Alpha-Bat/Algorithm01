def solution(prices):
    answer = []
    prices.pop()
    for idx, price in enumerate(prices) :
        n = 1
        for i in range(idx+1, len(prices)) :
            if price <= prices[i] :
                n += 1
            else :
                break
        answer.append(n)
    answer.append(0)
    return answer
