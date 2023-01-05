# amélioration de l'algorithme, on remplace : i par n-i-1 en ligne 5
tri = [7, 27, 3, 8]
n = len(tri)
for i in range(n):
      for j in range(n-i-1):
          if tri[j] > tri[j+1]:
            a = tri[j]
            tri[j] = tri[j+1]
            tri[j+1] = a
          print(tri)
