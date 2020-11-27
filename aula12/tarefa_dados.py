from random import randrange
lista = []

for i in range(100):
    lista.append(randrange(1,7))

print(lista)

for i in range (1,7):
    print(f'O número {i} apareceu', lista.count(i), 'vezes')