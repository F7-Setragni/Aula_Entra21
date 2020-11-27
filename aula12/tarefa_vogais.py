def conta_vogais(str):
    vogais = 'a e i o u'
    str = str.lower() 
    contagem = {}
    for i in vogais:
        contagem[i] = str.count(i)
    return contagem

print("Digite uma frase, qualquer uma :]")
frase = input()
print(conta_vogais(frase))
