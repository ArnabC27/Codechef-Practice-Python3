# cook your dish here
try:
    def solution(n):
        n //= 2
        return (n * (n-1)) // 2
        
    for i in range(int(input())):
        N = int(input())
        print(solution(N))
except:
    pass
