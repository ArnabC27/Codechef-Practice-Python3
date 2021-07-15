# cook your dish here
try:
    for _ in range(int(input())):
        N = int(input())
        S = input()
        
        if 'Y' not in S and 'I' not in S:
            print('NOT SURE')
        elif 'Y' in S:
            print('NOT INDIAN')
        elif 'I' in S:
            print('INDIAN')
except:
    pass
