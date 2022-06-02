def solution(prices):
    answer = []
    for idx, price in enumerate(prices) :
        n = 0
        for i in range(idx+1, len(prices)) : # 현재 price의 다음 인덱스부터 조사
            if price <= prices[i] : # price보다 가격이 떨어지지 않았다면
                n += 1
            else :
                n += 1 # 가격이 떨어지는 1초간에도 가격이 떨이지지 않은것으로 보기때문에 한번더 더해준다.
                break
        answer.append(n) # n이 idx 인덱스의 price의 가격이 떨어지지 않은 기간이므로 결과값에 append해준다.
    return answer
