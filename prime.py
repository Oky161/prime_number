#Checkear si un numero es primo

def checkIfPrimo(num):
	if num == 1: return False
	return sum([1 for x in range(2, num-1) if num%x == 0])==0

number = int(input("Ingrese su número para verificar que sea primo:	"))
print(checkIfPrimo(number))

print("Verificador de numeros primos\n-------------------")
nombre = input("Ingrese su nombre!! ")
nombre = nombre[0].upper() + nombre[1:]
print("Bienvenido" + nombre + "!")

numero = int(input("Ingrese su numero para verificar que sea primo:	"))
print(checkIfPrimo(numero))
print(checkIfPrimo(8))
