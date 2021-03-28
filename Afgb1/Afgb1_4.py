a = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
k = len(a)

for i in range(0, k-1):
 for j in range(0, k-1):
  if a[i] == a[j]:
    gleich = True

print gleich
