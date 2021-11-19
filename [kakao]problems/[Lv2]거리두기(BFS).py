from collections import deque
def bfs(p):
    start = []

    for i in range(5):  # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])

    for s in start:
        # print(s) # p점을 의미
        queue = deque([s])
        visited = [[0]*5 for i in range(5)] #방문처리된 곳 1로
        distance = [[0]*5 for i in range(5)] #경로 길이
        visited[s[0]][s[1]] = 1
        # print(visited) # p가 지나간 점
        while queue:
            y, x = queue.popleft()
            print(y,x)
            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i] # nx, ny는 한 포인트 움직인 후 점 좌표

                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0: #인덱스 안에 있고 방문한 적이 없다
                    queue.append([ny, nx])
                    visited[ny][nx] = 1
                    distance[ny][nx] = distance[y][x] + 1

                if p[ny][nx] == 'P' and distance[y][x] <= 1:
                    return 0
    return 1



places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
answer=[]
for room in places:
    answer.append(bfs(room))

print(answer)

