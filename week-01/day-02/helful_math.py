# n is the number of char in the numbers
# SC -> 0(N) 
numbers= list(map(int,input().split("+")))

ones = 0
twos = 0
threes = 0

# TC -> 0(N)
for num in numbers:
    if num == 1:
        ones += 1
    elif num == 2:
        twos += 1
    else:
        threes += 1

res = []
while ones != 0:
    res.append("1")
    ones -= 1
while twos != 0: 
    res.append("2")
    twos -= 1
while threes != 0:
    res.append("3")
    threes -= 1
 
# TC -> O(N) 
print("+".join(res))       
    
            


    
    
    