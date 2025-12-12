"""
Imprimiendo comillas
Construir un programa que pida una cita y un autor y devuelva una única cadena con la cita entre comillas y el autor.

Restricciones
No usar format ni % ni fstring. Hacerlo concatenando cadenas y escapando caracteres
"""

#Programa que pide una cita y un autor:

date= input("Dime una cita: ")
aut=input("Nombre del autor: ")
print("\"" + date + "\"" + " - " + aut)