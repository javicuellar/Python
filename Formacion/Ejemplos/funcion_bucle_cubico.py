# buscamos i siendo i el número que da como resultado:
#  m = 1 + (2)^3 + ... + (i)^3

def find_nb(m):
	a, i = 1, 1
	while True:
		if a == m:
			return i
		elif a > m:
			return -1
		else:
			i += 1
			a += i**3
 
print (find_nb(36))    # 3
print (find_nb(4183059834009))    # 2022
print (find_nb(24723578342962))   # -1
print (find_nb(135440716410000))  # 4824
print (find_nb(40539911473216))   # 3568
print (find_nb(26825883955641))   # 3218
