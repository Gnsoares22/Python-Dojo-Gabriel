conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8,9}

conjunto.add(6) # adiciona elemento no conjunto
conjunto.discard(6) #remove elemento do conjunto

uniao = conjunto.union(conjunto2)
print(uniao) #imprime o conjunto união (conjunto U conjunto2)

interseccao = conjunto.intersection(conjunto2)
print(interseccao) #imprime o conjunto intersecção (somente os elementos em comum entre os dois conjuntos)

diferenca = conjunto.difference(conjunto2)
print(diferenca) #imprime o conjunto diferença (o que tem em um conjunto menos o que tem no outro)

diferenca_simetrica = conjunto.symmetric_difference(conjunto2)
print(diferenca_simetrica) #imprime a diferença simetrica 

a = {4,5,6,7,8,9,10}
b = {6,7,8}
sub_conjunto = b.issubset(a)
print(sub_conjunto)

#set() remove elementos duplicados 