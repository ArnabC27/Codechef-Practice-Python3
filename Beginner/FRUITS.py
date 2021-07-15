# cook your dish here
try:
    for _ in range(int(input())):
        N, M, K = map(int, input().split())
        d = abs(N-M)
        print(0 if d <= K else d-K)
except:
    pass
