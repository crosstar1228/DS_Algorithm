import sys
inp = sys.stdin.readline

n ,m  = map(int, inp().split()) # space로 나누어진 입력
pattern = [list(inp().rstrip()) for i in range(n)]
visited = [[0]*m for i in range(n)]
# print(pattern)
def dfs(y, x,pattern):
    d = [-1, 1]

    if pattern[y][x]=='-' and visited[y][x]==0:
        visited[y][x]=1
        for dx in d:
            X = x + dx
            if 0<=X<m and pattern[y][X]=='-' and visited[y][X]==0:
                dfs(y,X,pattern)
    if pattern[y][x]=='|' and visited[y][x]==0:
        visited[y][x]=1
        for dy in d:
            Y = y + dy
            if 0<=Y<n and pattern[Y][x]=='|' and visited[Y][x]==0:
                dfs(Y,x,pattern)
cnt=0
for i in range(n):
    for j in range(m):
        if visited[i][j]==0:
            dfs(i,j,pattern)
            # print(visited)
            cnt+=1
print(cnt)