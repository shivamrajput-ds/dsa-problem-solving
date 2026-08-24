import math

n, m, a = map(int, input().split())

no_of_flagstones_req = math.ceil(n / a) * math.ceil(m / a)

print(no_of_flagstones_req)