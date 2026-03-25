import sys


def bfs(x,y):
    arr[x][y]=0
    dx=[-1,1,0,0,-1,1,-1,1]
    dy=[0,0,-1,1,-1,-1,1,1]
    q=list()
    q.append([x,y])
    while q:
        x,y=q.pop()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w:
                if arr[nx][ny]==1:
                    arr[nx][ny]=0
                    q.append([nx,ny])
                
                    
while True:
    w,h=map(int,sys.stdin.readline().split())
    if w == 0 and h==0:
        break
    
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    cnt=0
    for i in range(h):
        for j in range(w):
            if arr[i][j]==1:
                bfs(i,j)
                cnt+=1
    print(cnt)