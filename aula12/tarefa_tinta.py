import math
area_pintada = float(input("Qual será o tamanho da área pintada?: "))
litros = area_pintada / 6
latas = area_pintada / 108
galao = area_pintada / 21.6
folga = litros + (litros * .1)

tinta = input('Digite 1 para comprar latas de 18L e 2 para galões de 3,6L ou 3 para misturar e obter melhor preço: ')

if tinta == '1':
    valor = math.ceil(latas) * 80
    print('Você precisará de', math.ceil(latas), ' lata(s) que posso vender por R$',valor)
elif tinta == '2':
    valor = math.ceil(galao) * 25
    print('Você precisará de', math.ceil(galao), ' galões(ão) que posso vender por R$',valor)
elif tinta == '3':
    latas_folga = int(folga / 18)
    a2 = folga % 18
    galao_folga = math.ceil(a2 / 3.6)
    valor = ((latas_folga * 80)+(galao_folga * 25))
    print('Você precisará de', math.ceil(latas), ' lata(s), ', math.ceil(galao), ' galões(ão) que posso vender por R$',valor)