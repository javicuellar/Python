def fusc(n):
	assert type(n) == int and n >= 0
	if n == 0 or n == 1:
		return n
	elif n%2 == 0:
		return fusc(int(n/2))
	else:
		n -= 1
		return (fusc(int(n/2)) + fusc((int(n/2) + 1)))


print(fusc(0))  	# 0
print(fusc(1))  	# 1
print(fusc(2))  	
print(fusc(3))  
print(fusc(4))  
print(fusc(85)) 	# 21
