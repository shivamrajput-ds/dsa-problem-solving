n = int(input())
values = list(map(int, input().split()))

sorted_values = sorted(values)

prefix_original = [0] * (n + 1)
prefix_sorted = [0] * (n + 1)

for i in range(n):
    prefix_original[i + 1] = prefix_original[i] + values[i]
    prefix_sorted[i + 1] = prefix_sorted[i] + sorted_values[i]

m = int(input())

for _ in range(m):
    query_type, left, right = map(int, input().split())

    if query_type == 1:
        print(prefix_original[right] - prefix_original[left - 1])
    else:
        print(prefix_sorted[right] - prefix_sorted[left - 1])