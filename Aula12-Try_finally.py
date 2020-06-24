# Tratamento de erros

#Exception

# NameError / ValueError / ZeroDivisionError / TypeError / IndexError / KeyError/ EOFError /KeybordInterrupt 
# OSERROR / MemoryError / ConnectionError/ RuntimeError / ModuleNotFoundError (as principais)

try: #trata o erro 
    divisao = 10 / 0
    print(divisao)
except Exception as e: #Excpetion já me mostra o erro sem ter que adivinhar qual erro é 
    print("Erro: " + str(e))
else:
    print("DEU BOAAA ") # caso não tenha erro
finally:
    print("Comentário extraaaa") #comentário extra

print('*' * 40)

try:
    lista = [6]
    for x in range(4):
        print(lista[x])
        #raise Exception("Deu erro") #substitui a mensagem padrão do excpetion e coloca outra que voce quiser
except Exception as e: #Excpetion já me mostra o erro sem ter que adivinhar qual erro é 
    print("Erro: " + str(e))  
        
