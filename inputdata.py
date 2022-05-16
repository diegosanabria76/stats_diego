def input_user():
    lista = []
    n = int(input("enter the number of items do you want to enter"))
    suma = 0
    counter = 0


    for i in range(0,n):
        number = int(input("enter a number"))
        lista.append(number)

    print("You've have entered  : ", len(lista)," items")

    #print(lista)
    promedio = 0
    for num in lista:
        suma += num
        counter += 1
    promedio = suma / counter
    return promedio, lista

def desvi():
    promedio, lista = input_user()
    new_lista = []

    print("lista desde desvi() : ",promedio, lista)
    suma = 0
    for i in range(0, len(lista)):
        lista[i] = lista[i]-promedio
        new_lista.append(lista[i]**2)

    print(new_lista)
    n = len(new_lista)
    sum_= 0
    for j in new_lista:
        sum_ += j
    vari = sum_ / (n-1)
    desv_stan = vari**(1/2)

    return vari, desv_stan

print(desvi())
