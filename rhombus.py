import math

max = 7
mid = math.ceil(max/2)

for x in range(1, max+1):
	for y in range(1, max+1):
		if x == mid:
			print(f"*", end="")
		elif x - mid > 0:
			if y <= x - mid:
				print(f" ", end="")
			elif y > max-(x-mid):
				print(f" ", end="")
			else:
				print(f"*", end="")
		elif x - mid < 0:
			if y <= mid - x:
				print(f" ", end="")
			elif y > max-(mid -x):
				print(f" ", end="")
			else:
				print(f"*", end="")
	print("")

