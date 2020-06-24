# Operadores  matemáticos e lógicos

import math # importando a biblioteca matematica 
import pdb

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

print("===== Soma: {:=^20.0f}".format(num1+num2)) #truques do print (:=^20 20 simbolos do = na frente do número)
print("===== Subtração: {:=^20.0f}".format(num1-num2)) #truques do print
print("===== Multiplicação: {:=^20.0f}".format(num1*num2)) #truques do print
print("===== Divisão: {:=^20.0f}".format(num1/num2)) #truques do print
print("===== Resto: {:=^20.0f}".format(num1%num2)) #truques do print
print("===== Potência: {:=^20.0f}".format(num1**num2)) #truques do print
print("===== Raíz Quadrada: {:=^20.2f}".format(math.sqrt(num1))) #truques do print

expressao = 9*5+30 # em certos casos ele já reconhece a procedência das operações 
#numeros negativos -x (x é um numero qualquer)

print("Expresão: {:.2f} " .format(expressao))

#Desafios 

numero = int(input("Digite um numero: "))
print("Sucessor: {} " .format(numero+1))
print("Antecessor: {} " .format(numero-1))
print("Dobro: {} " .format(numero*2))
print("Triplo: {} " .format(numero*3))
print("Raíz Quadrada: {} " .format(math.sqrt(numero)))

print("\n") # qubra linha \n

nota1 = float(input("Digite a nota1: "))
nota2 = float(input("Digite a nota2: "))

media = (nota1+nota2)/2
print("Média: {:.2f} " .format(media))

print("\n") # qubra linha \n

# pdb.set_trace() serve para debbugar sendo n (next) c (continue) q (quite) l (list) 

metros = int(input("Metros: "))
print("{:.2f} metros equivale a {:*^10.2f} cm " .format(metros,metros*100))


# Operadores logicos utiliza-se com if sendo  | / or (ou)  & / and (and)  > < => <= != not (não) is (é)



