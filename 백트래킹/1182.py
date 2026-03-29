import sys

n,s=map(int,sys.stdin.readline().split())

arr=list(map(int,sys.stdin.readline().split()))

ans=0
def partsum(idx,sum):
    global ans

    if idx>=n:
        return
    
    sum+=arr[idx]

    if sum==s:
        ans+=1
    
    partsum(idx+1,sum)
    partsum(idx+1,sum-arr[idx])


partsum(0,0)
print(ans)
