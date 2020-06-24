# Comandos básicos Python

print("Hello Word")
print(7+10)  # comenta multilinha aspas triplas """ tres aspas para abrir e tres para fechar """

nome = 'Gabriel'  # variáveis são dinâmicas
idade = 23
peso = 89.9
vivo = True
sexo = 'Masculino'

# tipos int, float e até complex (para números complexos) | str (string)


print(nome + '-' + sexo)  # concatenção de duas strings

# olha o if
if 10 > 2:
    print("É maior que 2")
else:
    print("Não é menor que 2")


# Recebendo um valor digitado pelo usuario
nome = input("Digite seu nome: ")  # input le o valor que o usuario digitar

# format (formata a string inserindo dentro das chaves {})
print("Seja bem vindo {}".format(nome))


# Funções
def ExibeNome():
    global nome
    # tipagem de variavel global que pode ser acessada em qualquer parte do codigo
    nome = "APRENDENDO PYTHON"
    print(nome)


ExibeNome()  # escreve a função


# Exibe a soma de dois numeros reais
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1+num2
# para formatar a precisão do numero float basta usar :.2f (no lugar do 2 coloque o numero de casas que voce quiser)
print("Resultado de {:.0f} + {:.0f} = {:.0f}".format(num1, num2, soma))


# Dissecando variavel funções básicas strings

variavel = input("Digite algo: ")

# type() mostra que tipo a variavel é ex: strint, int
print("O tipo primitivo desse valor é + " + str(type(variavel)))
# isspace() verifica se tem espaços na variavel
print("Só tem espaços? {}".format(variavel.isspace()))
# isnumeric() verifica se é um número
print("É um número? {}".format(variavel.isnumeric()))
# isalpha() verifica se é um alfabetico
print("É alfabético? {}".format(variavel.isalpha()))
# isalnum() verifica se é um alfanumerico
print("É alfanumérico? {}".format(variavel.isalnum()))
# isupper() verifica se é Maiuscula
print("Está em maíusculo? {}".format(variavel.isupper()))
# islower() verifica se é Minuscula
print("Está em mínusculo? {}".format(variavel.islower()))
# istitle() verifica se a primeira letra da frase está em maiuscula, ou seja, é um titulo
print("Esta Capitalizada? {}".format(variavel.istitle()))


print("\n")

# numero complexo
c = complex(1, 2)
print("Tipo " + str(c.real) + " " + str(c.imag) +
      str(type(c)))  # conversão (cast)


# Listas
frutas = ["Pera", "Uva", "Maçã", "Banana"]  # vetor array
print(frutas)

jogadores = ("Rubinho","Pelé","Maradona","Pepe") #Tupla
print(jogadores)


# Json // Dictionary
x = {
    "canal":"Matematicos",
    "professor":"Juan",
    "ano":"2007"
}

print(x["professor"]) # pega pela chave

numeros = {0,1,15,6,7,7,1,6,7,4,8} #set não repete valores
print(numeros)

y = range(1,30,3) # range cria uma sequencia 

for n in y:
    print(n) # imprime a sequencia 