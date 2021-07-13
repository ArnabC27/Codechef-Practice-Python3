# cook your dish here
try:
    for _ in range(int(input())):
        h, cc, ts = map(float, input().split())
        if h > 50.0 and cc < 0.7 and ts > 5600.0:
            print('10')
        elif h > 50.0 and cc < 0.7:
            print('9')
        elif cc < 0.7 and ts > 5600.0:
            print('8')
        elif h > 50.0 and ts > 5600.0:
            print('7')
        elif h > 50.0 or cc < 0.7 or ts > 5600.0:
            print('6')
        else:
            print('5')
except:
    pass
