

"https://colab.research.google.com/drive/11L8qDxtCPFtHwuSs1Mh8VE3hS4RUdbg6"
"""
# Hola, mundo
Hacer un programa que pida el nombre y te salude por tu nombre

##Restricciones
Mantener entrada, salida y concatenación separados

Retos:
    Escribir el programa sin usar variables
    Escribir un programa que devuelva diferentes tipos de saludos a diferentes tipos de persona.
"""
"""
#entrada
nombre= input("Ingresa tu nombre: ")
#concatenacion
saludo= "Hola " +nombre
#salida
print(saludo)
"""

#Primer reto
print("Hola "+ input("Ingresa el nombre:  "))

#Segundo reto
personaslista=["Alba","Maria","Francisco"]
saludolista=["Hola ","Hello ","Ciao "]
"""
print(saludolista[0] +personaslista[0])
print(saludolista[1] +personaslista[1])
print(saludolista[2] +personaslista[2])
"""

for i in range(3):
    print(saludolista[i] +personaslista[i])

