matrix = []

for _ in range(5):
  row = list(map(int,input().split()))
  matrix.append(row)
  
one = None
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            one = [i,j]
            break
        
    if one is not None:
        break    

steps = abs(2-one[0]) + abs(2 - one[1])  

print(steps)     
      