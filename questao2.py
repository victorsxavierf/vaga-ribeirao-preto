def contadorA (word):
    count = 0

    for i in word:
        if i == 'a' or i == 'A':
            count+=1

    print("Nesta" ,word, "tem esta quantidade de A: " ,count)


palavra = str(input("Digite alguma palavra: "))
contadorA(palavra)