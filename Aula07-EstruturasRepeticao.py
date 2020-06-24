import time
import emoji

carros = ["Honda","Fiat","HB20"]
carros[0] = "Magy"

for x in carros:
    print(x)
    if(x == "Honda"):
        print("HONDA CIVIC")

for n in range(0,6,1):
    print(n)

print("\n")

# enumerate() mostra os elementos com seus respectivos indices

for n in enumerate(carros):
    print(n)

print(carros)

## DESCOMENTE ABAIXO, CASO QUEIRA VER FUNCIONANDO !!! 

""" for n in range(10,0,-1): # funciona com reversed() ou com range(10,0,-1)
    print(n)
    time.sleep(1) #biblioteca de timer
print(emoji.emojize("Feliz ano novo !! :fireworks:")) """

#verificar se é primo

""" numero = int(input("Digite um número: "))
cont = 0
for i in range(1,numero + 1):
    if(numero % i == 0):
        cont +=1
if(cont == 2):
    print("É primo")
else:
    print("Não é primo") """

#palindromo

# palavra = str(input("Digite uma palavra: ")).strip()

""" 1 - Possibilidade (muito fácil)

if palavra[::-1] == palavra:
    print("É um palindromo")
else:
    print("Não é um palindromo")

"""
""" inverso = ""
for letra in range(len(palavra) - 1, -1, -1): # INVERTENDO PALAVRA 2 - Possibilidade (menos fácil)
    inverso+= palavra[letra]

if palavra == inverso:
    print("É um palindromo")
else:
    print("Não é um palindromo") """


""" pesos = []
for i in range(0,5,1):
    peso = float(input("Digite o peso da pessoa número " + str(i) + " : "))
    pesos.append(peso)

maior = pesos[0]
menor = pesos[0]
seg_maior = pesos[1]
for x in range(len(pesos)):
    if pesos[x] > maior:
        maior = pesos[x]
        if pesos[x] > maior:
            seg_maior = pesos[x]
    
    if pesos[x] < menor:
        menor = pesos[x]
   
    
print("Maior: " + str(maior))
print("Maior2: " + str(seg_maior))
print("Menor: " + str(menor))
 """



     

