# 1) Back Tracking 알고리즘이란?
# - 완전탐색 알고리즘 중 하나
# - 완전탐색 수행 중, 현재의 탐색이 무의미하다고 판단되면 뒤로 돌아가는 알고리즘
# - 그러므로 퇴각검색이라 부르기도 한다. 

# 2) 완전탐색이란?
# - 완전탐색은 모든 경우의 수를 일일히 나열하며 답을 찾는 방법이다.
# - 모든 경우의 수를 탐색하며 답을 찾기 때문에, 반드시 답을 찾는 방법이기도 하다.(장점)
# - 다만, input의 크기에 따라서 시간이 오래 걸릴 수 있다는 단점이 있다. 
# - 그러므로 완전탐색을 사용한다면, 대략적인 경우의 수를 파악하여 시간복잡도를 아는 것이 관건이다. 

# 3) 완전탐색의 종류 
# - Brute-Force(브루트 포스): 단순히 for와 if문을 이용하여 모든 경우의 수를 점검하는 방법 
# - Bitmask(비트마스크): 컴퓨터의 이진수 연산을 이용하는 방법으로 0과 1에 해당하는 2가지 경우로 나누어 모든 경우의 수를 탐색하는 방법
# - Recursion(재귀): 비트마스크와 마찬가지로 2가지 경우로 나누어 모든 경우의 수를 탐색하는 방법 
# - Permutation(순열): N개의 서로 다른 수가 나열된 순열은 N!이 경우의 수가 된다. 순열의 경우 N < 10 일때 완전탐색을 사용할 수 있다.
# - BFS/DFS: 길찾기 문제에서 장애물이나 경유지 등이 존재하는 경우, 완전탐색을 사용 후 BFS/DFS를 적용한다.

# 4) 완전탐색을 적용하는 조건
# - 입력 데이터(N)의 크기가 매우 작은 경우  
# - 답(output)의 범위가 작고, 임의의 답을 하나 선택하여 시작하는 경우 
# - 여러 조건 중 하나의 조건을 고정시키고 답을 구하는 경우 

# 5) Back-Tracking의 특징
# - 백트래킹은 제약조건만족 문제에서 답을 찾기위한 전략이다. 
# - 답을 찾기위해 후보군에 제약조건을 검증하고, 제약조건을 만족하지 않는 경우가 발생하면 검증을 멈추고 다음 후보를 검증한다.
# - 이와 같은 방식을 사용하면 연산의 대상이 되는 후보군을 검증하는 반복연산의 횟수와 탐색시간이 줄어들어, 결과적으로 시간복잡도가 감소한다.

# 6) Back-Tracking의 로직(작동방식)
#   a. 모든 경우의 수를 상태공간트리(State Space Tree)로 표현한다.
#   b. DFS 방식을 이용해 탐색하며 조건에 부합하는지 확인한다.
#      - promising: 해당 경로가 조건에 부합하는지 검증하는 방법
#      - pruning(가지치기): 조건에 부합하지 않는 경우, 뒤로 돌아가 다른 경로를 탐색하는 방법 (탐색시간절약)

# 7) 상태공간트리란?
# - 각 노드마다 상태를 저장하는 공간을 가진 트리 
