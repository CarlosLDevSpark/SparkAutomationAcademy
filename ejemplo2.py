nombre = input('Digame su nombre: ')
apellido = input('Digame su apellido: ')
edad = input('Digame su edad: ')
edad = int(edad)
if edad < 18:
    resultado = 'menor'
elif edad <= 65:
    resultado = 'mayor'
elif edad <= 120:
    resultado = 'jubilado'
else:
    resultado = 'un cadaver'
print("Su nombre es: {0} {1} y usted es {2}".format(nombre, apellido, resultado))
