print (" ")#Salto de linea
print ("Velazquez Mares Jesus Eliu 3W 1276")
print (" ")#Salto de linea

#Crea un diccionario con las palabras en español e ingles
dic = {
    'hola': 'hello',
    'adiós': 'goodbye',
    'gracias': 'thank you',
    'por favor': 'please',
    'sí': 'yes',
    'no': 'no',
    'bueno': 'good',
    'malo': 'bad',
    'casa': 'house',
    'perro': 'dog',
    'gato': 'cat',
}

#Pide al usuario una palabra para tradusirla en el diccionario
p = input("Introduce una palabra en español: ").strip().lower()

#Si la variable p esta en el diccionario entonces
if p in dic:
    t = dic[p]
    #imprime en pantalla lo siguiente
    print("La traduccion de la palabra",p,"es",t,"en ingles")
else:#Sino
    #Imprime en pantalla un mensaje de error
    print("esa palobra no se encuentra en el diccionario")
