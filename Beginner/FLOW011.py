# cook your dish here
try:
    for _ in range(int(input())):
        salary = int(input())
        gs = salary
        if salary < 1500:
            gs += 0.1 * salary + 0.9 * salary
        else:
            gs += 500 + 0.98 * salary
        print(gs)
except:
    pass
