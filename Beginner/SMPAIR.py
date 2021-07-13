# cook your dish here
try:
    for _ in range(int(input())):
        N = int(input())
        a = list(map(int, input().split()))
        a.sort()
        print(a[0]+a[1])
except:
    pass
