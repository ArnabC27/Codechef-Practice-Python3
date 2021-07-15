# cook your dish here
try:
    for _ in range(int(input())):
        s = list(map(int, input().split()))
        s.sort()
        if s[0] == s[1] and s[2] == s[3]:
            print('YES')
        else:
            print('NO')
except:
    pass
