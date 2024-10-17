print (" ")#Salto de linea
print ("Velazquez Mares Jesus Eliu 3W 1276")
print (" ")#Salto de linea
#Creacion de un diccionario vacio con las espasificaciones antes dadas
dic = {
    'nombre': ' ',
    'edad': ' ',
    'sexo': ' ',
    'telefono':' ',
    'correo electronico':' '
}
#Le pide datos al usuario y los guarda en el diccionario
dic['nombre'] = input("Ingresa tu nombre: ")
print (" ")#Salto de linea
dic['edad'] = input("Ingresa tu edad: ")
print (" ")#Salto de linea
dic['sexo'] = input("Ingresa tu sexo: ")
print (" ")#Salto de linea
dic['telefono'] = input("Ingresa tu numero telefonico: ")
print (" ")#Salto de linea
dic['correo electronico'] = input("Ingresa tu correo electronico: ")

print (" ")#Salto de linea

#Imprime los datos del usuario antes dados por el mismo
print ("Tu nombre es ", dic['nombre'])
print ("y tienes una edad de ", dic['edad'])
print ("Eres de genero", dic['sexo'])
print ("Tu numero telefonico es: ", dic['telefono'])
print ("Y tu correo electronico es el siguiente: ", dic['correo electronico'])