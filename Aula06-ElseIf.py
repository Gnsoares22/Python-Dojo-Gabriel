import random
import math
# Estrutura condiciona If | else | Elif

"""
palpite = int(input('Digite um numero: '))

sorteado = random.randint(0,10)

if palpite == sorteado:
    print("Acertouu miserávii !!")
else:
    print("Errrouuuuuuuuuuuu !! O numero sorteado era " + str(sorteado))
"""

""" km_rodado = int(input("Digite quantos kilometros o carro percorreu: "))

if km_rodado <= 80:
    print("Você não foi multado")
else:
    print("Voce foi multado !!!")
    print("Valor da multa R$ {} " .format((km_rodado - 80)*7)) """

""" numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("Par")
else: 
    print("Impar") """

""" distancia = int(input("Qual a distância da viagem: "))

if distancia <= 200:
    preco = distancia * 0.50
    print("Valor da viagem R$ " + str(preco))
else:
    preco = distancia * 0.45
    print("Valor da viagem R$ " + str(preco)) """


""" valor_casa = float(input("Digite o valor da casa R$ "))
salario = float(input("Digite o valor do seu salário R$ "))
tempo_pagamento = int(input("Digite o tempo do pagamento das parcelas 1 -  Anos | 2 - Meses: "))

if tempo_pagamento == 2:
    meses = int(input("Quantos meses voce vai pagar ?: "))
    if meses <= 12:
        prestacao = valor_casa / meses
        if prestacao >= 0.30 * salario:
            print("Empréstimo Negado !!!")
        else:
            print("Emprestimo Aprovado !! Valor da prestação R$ {}" .format(prestacao))
    elif meses > 12:
        print("Os meses vão até 12 !!!")
elif tempo_pagamento == 1:
    anos = int(input("Quantos anos voce vai pagar ?: "))
    prestacao = valor_casa / anos
    if prestacao >= 0.30 * salario:
        print("Empréstimo Negado !!!")
    else:
        print("Emprestimo Aprovado !! Valor da prestação R$ {}" .format(prestacao))
else:
    print("Opção Inválida !!")"""



# Functions com if e elif 

def converter_binario(num):
    i = 2
    binario_convertido = []
    while num >= 1:
        resto = num % i
        resto_arredondado = math.floor(resto)
        binario_convertido.append(resto_arredondado)
        num/=i  
    binario_convertido.reverse()
    return binario_convertido

def converter_octal(num):
    octal_convertido = []
    i = 8
    while num >= 1:
        resto = num % i
        resto_arredondado = math.floor(resto)
        octal_convertido.append(resto_arredondado)
        num/=i
    octal_convertido.reverse()
    print(octal_convertido)



numero = int(input("Digite um número: "))
conversao_tipo = int(input("Voce beseja converter em 1 - Binário | 2 - Octal: "))


if conversao_tipo == 1:
   
    print("O número " + str(numero) + " em binário corresponde ", converter_binario(numero))

elif conversao_tipo == 2:
    print("O número " + str(numero) + " em octal corresponde ", converter_octal(numero))

  





# Cores (Ver na internet as receitas de cores !!)
cores = {
    'azul': '\033[34m',
    'ciano': '\033[36m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'branco': '\033[37m'
}

nome = "Gabriel"

print('Meu nome é {} {} {} ' .format(cores['verde'], nome, cores['branco']))
