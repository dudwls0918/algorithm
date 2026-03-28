#pypy3는 통과인데 python3는 시간초과 
import sys

n=int(sys.stdin.readline())

row=[0]*n
cnt=0

def solve(a):
    for i in range(a):
        if (row[a]==row[i]) or abs(row[a]-row[i])==abs(a-i):
            return False
        
    return True

def queen(a):
    global cnt
    if a==n:
        cnt+=1
        return
    
    for i in range(n):
        row[a]=i
        if solve(a):
            queen(a+1)


queen(0)
print(cnt)
