from collections import defaultdict
guest_name = input().upper()
host_name = input().upper()
pile = input().upper()

freq = defaultdict(int)

for ch in guest_name:
    freq[ch] += 1

for ch in host_name:
    freq[ch] += 1


for ch in pile:
    freq[ch] -= 1

check = True
for ch,val in freq.items():
    if val != 0:
        check = False
        break

if check == False:
    print("NO")
else:
    print("YES")        
            
