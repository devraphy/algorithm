# 백준 단계별 풀이 4단계
# https://www.acmicpc.net/problem/1110

n = int(input())
goal = n
ten = n // 10
one = n % 10 
count = 0

while (True):
  plus = ten + one
  next = (one * 10) + (plus % 10)
  count += 1
  if(goal == next):
    print(count)
    break
  else:
    ten = next // 10
    one = next % 10 