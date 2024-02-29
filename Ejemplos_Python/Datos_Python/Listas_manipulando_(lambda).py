# ------------------------------------------------------------------------------------------------
#   COGIENDO TROZOS DE LISTAS
# ------------------------------------------------------------------------------------------------

l = [i ** 2 for i in range(1, 11)]

print(l)            # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(l[2:9:1])     # [9, 16, 25, 36, 49, 64, 81]   del 2 incluido(empieza en 0) al 9 excluido
print(l[2:9:2])	    # [9, 25, 49, 81] del 2 al 9 pero de dos en dos

#   No funciona bien porque no genera la lista si no una variable de tipo range
my_list = range(1, 11) 	    # Lista de numbers 1 - 10
print("\nLista inicial: ", my_list, type(my_list))
print(my_list[::2])         # saca los numeros impares (desde el principio, cada dos)
print(my_list[::9])		    # saca el primero y 9 números después, el último

backwards = my_list[::-1] 	# lista invertida, del 10 al 1
print(backwards)

to_one_hundred = range(101)					# lista de 1 a 100
backwards_by_tens = to_one_hundred[::-10]	# lista invertida de 100 a 10 (de 10 en 10)
print(backwards_by_tens)

my_list = range(16)         # lista de números del 0 al 15
print(filter(lambda x: x % 3 == 0, my_list))

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(filter(lambda x: x == "Python", languages))

threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
print(threes_and_fives)				# [3, 5, 6, 9, 10, 12, 15]

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-1]
print(message)   			# IX XaXmX XtXhXeX XsXeXcXrXeXtX XmXeXsXsXaXgXeX!
message = message[::2]
print(message)				# I am the secret message!

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x:x != 'X' ,garbled)
print(message)				# I am another secret message!