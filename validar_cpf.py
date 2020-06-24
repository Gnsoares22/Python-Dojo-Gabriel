#modelo de cpf a ser testado 529.982.247-25 || 111.111.111-11
# o cpf tradicional tem 14 digitos, mas devido ao replace esse cpf terá 11 digitos, pois eu tirei os pontos
# assim o vetor começa na posição 0 e vai até a 11 // totalizando 12 elementos 

cpf = str(input("Digite o seu cpf: "))
i = 0
j = 0
conta_repetidos = 0
soma_penultimo = 0
soma_ultimo = 0

# verifica se o cpf tem 14 digitos incluindo os pontos e traço
if len(cpf) == 14:

    novo_cpf = cpf.replace(".","").replace("-","") #tira pontos e o traço
    penultimo = novo_cpf[9] # penultima posicao
    ultimo = novo_cpf[10] #ultima posicao

    #verifica se o cpf é repetido ex: 111.111.111-11
    while i < 10:
        while j < i:      
            if(novo_cpf[i] == novo_cpf[j]):
                conta_repetidos+=1
            j+=1
        i+=1

    if(conta_repetidos >= 8):
        print("CPF REPETIDO !!!")

    else:

    # 1 etapa verifica o penultimo digito após o "-"
        for x in range(0,9,1):
            soma_penultimo+= int(novo_cpf[x]) * (10 - x) 

        resto_penultimo = (soma_penultimo * 10) % 11   # 2 (penultimo digito após o "-")

        # 2 etapa verifica o ultimo digito após o penultimo
        for x in range(0,10,1):
            soma_ultimo+= int(novo_cpf[x]) * (11 - x) 

        resto_ultimo = (soma_ultimo * 10) % 11    # 5 (ultimo digito após o numero 2)

        if ((int(penultimo) == resto_penultimo) and (int(ultimo) == resto_ultimo)):
            print("CPF VÁLIDO !!")
        else:
            print("CPF INVÁLIDO !!!")

else:
    print("CPF DEVE CONTER 14 DIGITOS INCLUINDO PONTUAÇÃO !!!")






