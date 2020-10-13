#Checkear si un numero es primo

def checkIfPrimo(num):
	if num == 1: return False
	return sum([1 for i in range(2, num-1) if num%i == 0])==0

numero = int(input("Ingrese su numero para verificar que sea primo:	"))
print(checkIfPrimo(numero))