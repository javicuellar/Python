def starting_mark(height):
	inicio = 9.45
	dif = height - 1.52
	return round((inicio + (dif * 1.22) / 0.31), 2)

print (starting_mark(1.52))  # 9.45
print (starting_mark(1.83)) # 10.67
print (starting_mark(1.22)) # 8.27
print (starting_mark(2.13)) # 11.85
print (starting_mark(1.75)) # 10.36