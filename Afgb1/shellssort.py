def shellsort(liste):

  h =len(liste)
  gap =h//4
  whilegap > 0:

  for outer in range(gap,h):

  tmp =liste[outer]
  inner =outer
  while  j >=gap andliste[inner-gap] >tmp:

  liste[inner] =liste[inner-gap]
  inner -=gap
  liste[inner] =tmp
  gap //=4

  liste =[ 4, 10, 2, 8, 1, 7, 12, 3, 6, 11, 5, 9]
  h =len(liste)
  print(„Eingabeliste:“)
  forouter inrange(h):

  print(liste [outer]),

  shellsort(liste)
  print(„\nSortierte Liste:“)
  forouter inrange(h):
