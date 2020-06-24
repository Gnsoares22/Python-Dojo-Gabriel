# vetor com elementos repetidos

vetor = [1,1,2,3,4,5,6,6,7,8,8,9,9,10,1]
i = 1
j = 0

#remove elementos duplicados do array
while i < len(vetor):
    while j < i:
        if(vetor[i] == vetor[j]):
            del vetor[j]
        j+=1
    i+=1


print(vetor)
