import bubble_sort as bs

while True:

    lista = []
    fin = False

    while True:

        while True:
            n = input("escriba numero a ordenar: ")
            if n == "fin":
                fin = True
                break
            try:
                n = int(n)
                break
            except:
                print("lo escrito no es valido")
        if fin:
            break
        if (n == -9999):
            break
        lista.append(n)
    if fin:
        break
    lo = bs.BubbleSort(lista)
    print("Lista ordenada: ", '\n', lo.sorted_list)