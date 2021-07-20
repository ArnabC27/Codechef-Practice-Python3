# cook your dish here
try:
    for _ in range(int(input())):
        l = list(map(int, input().split()))
        l.sort()
        print(l[-2])
except:
    pass
