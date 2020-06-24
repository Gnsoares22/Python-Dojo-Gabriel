import random as r
import string as s

#array bidimensional, composto por linhas e colunas
matriz = [[0] * 3 for n in range(3)] ## ou matriz = [[1,1,1],[1,1,1],[1,1,1]] no caso 3x3
elemento_repetido = 0
count = 0

def verificaElementoRepetido(matriz,lp,cp,elemento_repetido): #função que verifica a duplicidade dos elementos da matriz
    for x in range(0,lp):
        for y in range(0,cp):
            if(elemento_repetido == matriz[x][y]):
                return False
             

for i in range(0,3):
    for j in range(0,3):
        elemento_repetido = r.randint(1,10) 
        while verificaElementoRepetido(matriz,3,3,elemento_repetido) == False:
            elemento_repetido = r.randint(1,10) 
        matriz[i][j] = elemento_repetido


print("-------= Matriz Gerada (sem elementos repetidos) =--------- ") 

for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^3}]', end= '')
    print('\n')


print("-------= Diagonal Principal =--------- ") 

for i in range(0,3):
    for j in range(0,3):
        if i == j:
            print(f'[{matriz[i][j]}]')

print("-------= Diagonal Secundário =--------- ") 

for i in range(0,3):
    for j in range(0,3):
        if len(matriz) - 1 - j == i:
            print(f'[{matriz[i][j]}]')

