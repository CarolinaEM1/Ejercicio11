#Pide números e insertalos en una lista, cuando el usuario digite 0 dejaremos de insertar y ordenaremos la lista de menor a mayor.

lista = []
salir = False


while not salir:
    numero = int(input("Digite un número -> "))
    if numero ==0:
        salir=True
    else:
        lista.append(numero)
lista.sort()

print(f"\nLa lista ordenada es: \n{lista}")

#Carolina EM

