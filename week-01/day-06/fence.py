n, k = map(int,input().split(" "))
h = list(map(int,input().split(" ")))

total = 0
start_index = 1 
for i in range(k):
    total += h[i]

minimum_sum_fence = total
res = start_index

for i in range(k,n):
    total -= h[i - k]
    total += h[i]
    start_index += 1
    
    if total < minimum_sum_fence:
        minimum_sum_fence = total
        res = start_index

print(res)        
          
    
    
    
