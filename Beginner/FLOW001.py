# cook your dish here

#Read the number of test cases.
T = int(input())
for _ in range(T):
	# Read integers a and b.
	(a, b) = map(int, input().split())
	
	ans = a + b
	print(ans)
