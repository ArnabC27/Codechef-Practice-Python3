# cook your dish here
try:
    for _ in range(int(input())):
        S = input()
        l = S[:len(S)//2]
        r = S[len(S)//2 + 1 :] if len(S)%2 == 1 else S[len(S)//2 :]
        if sorted(list(l)) == sorted(list(r)):
            print('YES')
        else:
            print('NO')
except:
    pass
