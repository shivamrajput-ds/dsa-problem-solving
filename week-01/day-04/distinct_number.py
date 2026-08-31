n = int(input())
x = list(map(int, input().split()))

x.sort()

count = 1
last_seen = x[0]

for i in range(1, n):
    if x[i] != last_seen:
        count += 1
        last_seen = x[i]

print(count)