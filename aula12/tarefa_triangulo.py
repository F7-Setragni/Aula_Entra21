lado_A = float(input('Qual é a largura do lado a: '))
lado_B = float(input('Qual é a largura do lado b: '))
lado_C = float(input('Qual é a largura do lado c: '))

if lado_A == lado_B != lado_C or lado_A == lado_C != lado_B or lado_C == lado_B != lado_A:
    print('É um triângulo isósceles')
elif lado_A != lado_B != lado_C:
    print('É um triângulo escaleno')
elif lado_A == lado_B == lado_C:
    print('É um triângulo equilátero')
else:
    print('inválido!')