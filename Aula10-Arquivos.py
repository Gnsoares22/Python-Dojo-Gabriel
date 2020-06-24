import shutil #para copiar arquivos
# Criando arquivo python
## w - write (escrever/criar arquivo) | a - append (acrescenta mais textos no arquivo) | r - read (arquivo em modo de leitura)

def criarArquivo(nome_arquivo,texto): 
    caminho = 'C:/Users/Gabriel/Desktop/' + nome_arquivo + ".txt"
    arquivo = open(caminho,'w') #abrindo um arquivo 
    arquivo.write(texto) # escreve o conteudo do arquivo 
    arquivo.close() # fecha arquivo

def atualizarArquivo(nome_arquivo,texto):
    caminho = 'C:/Users/Gabriel/Desktop/' + nome_arquivo + ".txt"
    arquivo = open(caminho,'a') #abrindo um arquivo 
    arquivo.write(texto) # adicionar mais conteudo do arquivo 
    arquivo.close() # fecha arquivo

def lerArquivo(nome_arquivo):
    caminho = 'C:/Users/Gabriel/Desktop/'
    arquivo = open(caminho + str(nome_arquivo)+".txt",'r').read()
    print(arquivo)
    
def copiarArquivo(nome_arquivo):
    caminho = 'C:/Users/Gabriel/Desktop/' + str(nome_arquivo) + ".txt"
    destino_copia = 'C:/Users/Gabriel/Desktop/Utilidades/Python'
    shutil.copy(caminho,destino_copia) #copia o arquivo para o caminho desejado 
    # shutil.move() pode ser usado tambem 


if __name__ == "__main__": # função principal __main__

    criarArquivo("Teste","Meu primeiro arquivo")
    lerArquivo("Teste")
    atualizarArquivo("Teste","\n Salve rapaziada !!!")
    copiarArquivo("Teste")



