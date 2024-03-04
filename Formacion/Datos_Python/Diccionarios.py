# ------------------------------------------------------------------------------------------------
#    Diccionarios
# ------------------------------------------------------------------------------------------------
my_dict = { 'nombre':'Javi',
            'edad':25,
            'sexo':'V'}

print(my_dict.items())     	# displaya claves y valores
print(my_dict.keys())		# displaya claves
print(my_dict.values())		# displaya valores

for key in my_dict:
    print(key, my_dict[key])