import sys


n=int(sys.stdin.readline())

def hanoi(n,start,end):
    if n==1:
        print(start,end)
        return

    hanoi(n-1,start,6-start-end)
    print(start,end)
    hanoi(n-1,6-start-end,end)


def num(n):
    if n==1:
        return 1
    else:
        return 2*num(n-1)+1
    

print(num(n))
hanoi(n,1,3)


