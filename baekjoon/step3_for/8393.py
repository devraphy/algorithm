# 백준 단계별 풀이 3단계 
# https://www.acmicpc.net/problem/8393
import sys

n = int(sys.stdin.readline())
temp = 0

for data in range(1, n+1):
  temp += data

print(temp)
