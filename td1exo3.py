tri = [7, 27, 3, 8]
n = len(tri)
for i in range(n):
      for j in range(i):
          if tri[j] > tri[j+1]:
            a = tri[j]
            tri[j] = tri[j+1]
            tri[j+1] = a
          print(tri)