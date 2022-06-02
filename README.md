# Stack-Queue
## Stack(스택)
> - LIFO(Last-in, First-out)
> - push, peek, pop
> ```python
> class Stack(list):
>     push = list.append
>     def peek(self):
>         return self[-1]
>     # pop은 list 내장함수로 이미 존재
> ```
## Queue(큐)
> - FIFO(First-in, First-out)
> - put, peek, get
> ```python
> class Queue(list):
>     put = list.append
>     def peek(self):
>         return self[0]
>     def get(self):
>         return self.pop(0)
> ```
## 문제
> 1. 주식가격 [문제](https://programmers.co.kr/learn/courses/30/lessons/42584) [풀이](https://github.com/Alpha-Bat/Stack-Queue/blob/main/stock_price.py)
> 2. 기능개발 [문제](https://programmers.co.kr/learn/courses/30/lessons/42586) [풀이](https://github.com/Alpha-Bat/Stack-Queue/blob/main/feature_development.py)
> 3. 다리를 지나는 트럭 [문제](https://programmers.co.kr/learn/courses/30/lessons/42583) [풀이](https://github.com/Alpha-Bat/Stack-Queue/blob/main/truck_bridge.py)
 
