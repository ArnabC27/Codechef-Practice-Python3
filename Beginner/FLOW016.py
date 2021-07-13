# cook your dish here
try:
    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b%a, a)
        
    for i in range(int(input())):
        a, b = map(int, input().split())
        g = gcd(a, b)
        print(g, (a*b)//g)
except:
    pass
