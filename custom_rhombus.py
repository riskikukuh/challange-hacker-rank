import math

# Default / minimum
min = 7
midLine = 3

max = 20
x = max
y = 11
mid = math.ceil(max/2)

for x in range(1, min+1):
	for y in range(1, min+1):
		print(f"{x}", end="")
	print("")

