
"""https://colab.research.google.com/drive/1jLDOM-UuM-nFDbJ8HwfItpGQrnZWsgOH"""
"""
Contando caracteres
El programa pedirá una cadena de caracteres y devolverá el número de caracteres.

Restricciones
Asegurate de que devuelve la cadena original
Utiliza la función específica de python para resolverlo
Retos
Si el usuario no introduce nada, el programa le conminará a que escriba algo.
Hazlo sin utilizar la función específica de python
"""
"""
#Cuenta los caracteres de una cadena utilizando len
def count_caract(letter):
    return len(letter)

letter= input("Escribe algo: ")

while letter == "":
    letter= input("Escribe algo: ")

print(letter)
print(count_caract(letter))


#Lo hacemos sin utilizar len
def count_caract(letter):
    counter=0
    for n in letter:
        counter = counter + 1
    return counter

letter= input("Escribe algo: ")

while letter == "":
    letter= input("Escribe algo: ")

print(letter)
print(count_caract(letter))
"""
