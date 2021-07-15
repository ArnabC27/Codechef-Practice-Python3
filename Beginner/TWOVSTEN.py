# cook your dish here
try:
    for _ in range(int(input())):
        X = int(input())
        if X % 5 != 0:
            print('-1')
        elif X % 10 == 0:
            print('0')
        else:
            print('1')
except:
    pass
