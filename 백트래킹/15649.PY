import sys

n,m=map(int,sys.stdin.readline().split())
arr=list()
visited=[False]*(n+1)

def func(n,m):
    if len(arr)==m:
        for i in arr:
            print(i,end=" ")
        print()

    for i in range(1,n+1):
        if visited[i]==False:
            visited[i]=True
            arr.append(i)
            func(n,m)
            arr.pop()
            visited[i]=False


func(n,m)