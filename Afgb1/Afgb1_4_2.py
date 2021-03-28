b = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
l = len(b)
n = 0

def calc(n):
 return n*n

for i in range(0, 100):
 for j in range(0, l):
  k = l
  while k > 1:
    calc(k)
    n = n + 1
    k = k / 2
