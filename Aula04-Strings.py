# Manipulação de strings
import string
import math
frase = "Hoje eu li na cama robson crusie da França"

print(frase)
print(frase[1:10]) # ou print(frase[1]) pega a posição da string sem necessidade de substr
print(len(frase)) #comprimento da frase
print(frase.upper()) # upper() maiusculo | lower() mínusculo
print(frase.replace('da França','do Brasil')) #replace substitui
print(frase.split(" ")) # transforma a string em um vetor
print("*".join(frase)) # une caracteres de separação de string

if "Hoje" not in frase: #not | in
    print("true")
else:
    print("false")

Nome = "Gabriel Nascimento Soares"

print("Meu nome é  \"{}\"" .format(Nome)) #format serve tambem para strigs

#capitalize() | count() | startswith() | endswith() outras demais funções 

Nome2 = "Jonas Pereira Pinto"
vetor_nome = Nome2.split(" ")
print('Primeiro nome: {}  ultimo nome: {} ' .format(vetor_nome[0],vetor_nome[len(vetor_nome)-1])) # [len(vetor_nome)-1] pega o ultimo indice do array

print(Nome.upper())
print(Nome.lower())
print(len(Nome) - Nome.count(' '))
print(Nome.find(' ')) #find() conta quantos caracteres tem até o primeiro espaço | é semelhante ao indexOf

print('\n')

