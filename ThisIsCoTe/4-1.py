"""
구현
- 상하좌우: 문제 조건
"""

# N 입력 받기
n = int(input())

# 시작 좌표
x, y = 1, 1

# 방향 입력 받기
plans = input().split()

# L R U D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ["L", "R", "U", "D"]


# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for idx in range(len(move_types)):
        if plan == move_types[idx]:
            nx = x + dx[idx]
            ny = y + dy[idx]

    # 공간을 넘어서면 이동 무시
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

    # 이동 수행
    x, y = nx, ny

print(x, y)
