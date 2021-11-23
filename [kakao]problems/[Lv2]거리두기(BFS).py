#https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%EA%B1%B0%EB%A6%AC%EB%91%90%EA%B8%B0-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0-Python

from collections import deque


def bfs(place):
    start = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                start.append([i, j])
    # print(start)

    for s in start:
        que = deque([s])
        print(que)
        visited = [[0] * 5 for i in range(5)]
        distance = [[0] * 5 for i in range(5)]
        visited[s[0]][s[1]] = 1

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        while que:
            y, x = que.popleft()
            # print(y, x)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # print(ny,nx)
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0 and place[ny][nx] != 'X':
                    que.append([ny, nx])
                    visited[ny][nx] = 1
                    distance[ny][nx] = distance[y][x] + 1
                    if place[ny][nx] == 'P' and distance[ny][nx] <= 2:
                        return 0

    return 1

def solution(places):
    answer=[]
    for place in places:
        answer.append(bfs(place))
    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]



print(solution(places))

