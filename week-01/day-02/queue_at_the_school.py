n, t =map(int,input().split())
s = input()

res = []

for ch in s:
    res.append(ch)

while t != 0:
    i = 0
    while i < n - 1:
        if res[i] == "B" and res[i+1] == "G":
            res[i],res[i+1] = "G","B"
            i += 2
            continue
        i += 1
    t -= 1

print("".join(res))   
