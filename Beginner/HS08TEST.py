# cook your dish here
X, Y = map(float, input().split())
if(X % 5 != 0 or X + 0.5 > Y):
  print("{:.2f}".format(Y))
else:
  print("{:.2f}".format(Y - X - 0.5))
