

#Ejercicio contador billetes

dinero = int(input("Ingrese cantida de dinero a convertir: "))
resto = dinero
billetes20mil = (resto - resto%20000)//20000
resto = resto % 20000

billetes10mil = (resto - resto % 10000)//10000
resto = resto % 10000

billetes5mil = (resto - resto % 5000)//5000
resto = resto % 5000

billetes2mil = (resto - resto % 2000)//2000
resto = resto % 2000

billetes1mil = (resto - resto % 1000)//1000
#resto = resto % 2000

print("cantidad billetes 20 mill ",str(billetes20mil))
print("cantidad billetes 10 mill ",str(billetes10mil))
print("cantidad billetes 5 mill  ",str(billetes5mil))
print("cantidad billetes 2 mill  ",str(billetes2mil))
print("cantidad billetes 1 mill  ",str(billetes1mil))
