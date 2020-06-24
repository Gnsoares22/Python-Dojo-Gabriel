frase = str(input())
nova_string = ""
count = 0

if (frase.isalpha() or len(frase) <= 50 or frase.find('*')):
    for x in range(len(frase)):
        if frase[x] == '_':
            count+=1
            if count % 2 == 1:
                nova_string += frase[x].replace('_','<i>')
            else:
                nova_string += frase[x].replace('_','</i>')
        
        elif frase[x] == '*':
            count+=1
            if count % 2 == 1:
                nova_string += frase[x].replace('*','<b>')
            else:
                nova_string += frase[x].replace('*','</b>')
        else:
            nova_string += frase[x]

print(nova_string)
