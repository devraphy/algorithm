# 백준 단계별 풀이 8단계
# https://www.acmicpc.net/problem/1193

# 1) 그룹 찾기 
# 대각선 방향대로 그룹을 만들면 n번 그룹은 n개의 요소를 갖는다.
# ex) 1번 그룹 = 1/1 ==> 1개 요소
# ex) 2번 그룹 = 2/1, 1/2 ==> 2개 요소
# 즉, x번째 요소의 그룹은 1 + 2 + 3 + ... + n의 합이 x 보다 커졌을 때,
# x번째 요소는 n번째 그룹에 속해있는 것이다. 
# ex) 12 번째 요소 = 1 + 2 + 3 + 4 + 5 ==> 5번째 그룹, 총 15개의 요소 

# 2) 방향 찾기 
# 짝수번째 그룹은 분자가 증가(1,2,3,4) 분모가 감소(4,3,2,1)
# 홀수번째 그룹은 분자가 감소(4,3,2,1) 분모가 증가(1,2,3,4) 

# 3) x번째 요소 찾기 
# n번째 그룹까지 1 + 2 + 3 + ~ + n개를 해서 총 요소의 갯수 m를 구한다 
# m - x를 하여 차이를 구한다. 
# 방향에 따라 차이만큼 증가 또는 감소하면 된다. 
# ex) 12번째 요소 찾기 ==> 1 + 2 + 3 + 4 + 5 ==> 5번째 그룹, 총 15개의 요소 
# ==> 15 - 12 = 3 ==> 5번째 그룹, 홀수 ==> 분자 = (1+3), 분모 = (5-3) ==> 4/2

n = int(input())
element = 1
group = 1

while n > element:
  group += 1
  element += group

if group % 2 == 0:
  top = group - (element - n)
  bottom = 1 + element - n
else:
  top = 1 + element - n
  bottom = group - (element - n)

print(top, '/', bottom, sep='')