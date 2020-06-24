# Mais conceitos
import random as r # apelida o import 
#from math import sqrt, sin #escolhe quais operações especificas posso importar da biblioteca math
import emoji 
import math
import playsound 
import pygame

# conversao (cast)

a = "1"
b = 3 
print("Resultado: {}".format(int(a)+b))  # float() int() complex() 

# random
"""
numero_aleatorio = r.randrange(1,888)
print("Número aleatorio gerado: " + str(numero_aleatorio))

print(emoji.emojize('Python is :bug:',use_aliases= True))

numero = float(input("Digite um numero: "))
print("Parte real do número {:.0f}".format(numero)) # ou math.floor()
"""

nomes = []
for x in range(1,5,1):
    nome = str(input("Digite o " + str(x) + " nome: "))
    nomes.append(nome)


r.shuffle(nomes) # shuffle() embaralha o array || choice() escolhe um item da lista
print(nomes)

#reproduzindo audio com a lib playsound (1° metodo mais facil)
#playsound.playsound('Viva_La_Vida.mp3')

#(2° metodo mais chatinho) utilizando a lib pygame
pygame.mixer.init()
pygame.mixer.music.load('Viva_La_Vida.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

