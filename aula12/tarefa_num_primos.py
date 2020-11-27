numero = int(input("Digite o número até onde contarei os multiplos: "))
multiplo = 0

for num in range (2,numero):
    if (numero % num == 0):
        print("múltiplo de ", num)
        multiplo += 1

if(multiplo==0):
    print(f"{numero} é número primo")
else:
    print(f"{multiplo} múltiplos até {numero}, não é primo")