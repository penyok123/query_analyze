data = open("data", "r", encoding="utf8")

all_lag = 0
for item in data.readlines():
    lag = item.strip().split()
    all_lag += int(lag[5])

print(all_lag)

"""
7791170   3052
7790667   3138
7790953
7790810
 439297
"""

print(0.7 * int(3) + 0.3 * int(0))