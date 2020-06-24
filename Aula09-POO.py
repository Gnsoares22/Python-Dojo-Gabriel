class Calculadora: # criando a primeira classe
    def __init__(self,num1,num2): # seu método construtor
        self.valor_a = num1 #atributo da classe num1 e num2
        self.valor_b = num2
    def soma(self): # O método soma da classe
        return self.valor_a + self.valor_b # SELF É COMO SE FOSSE O THIS

calculadora = Calculadora(10,2) #instanciando a classe já passando os parametros direto
print(calculadora.soma()) #invocando o método soma() da classe



# 2 exemplo

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 0

    def ligarTv(self): #metodo void sem retorno
        self.ligada = True

    def desligarTv(self):
        if self.ligada == True:
            self.ligada = False

    def mudarCanal(self):
        if tv.ligada == True:
            self.canal += 1
        else:
            print("TV ESTÁ DESLIGADA !!!")

    def voltarCanal(self):
        if tv.ligada == True:
            self.canal -= 1
        else:
            print("TV ESTÁ DESLIGADA !!!")

#método/função principal, semelhante ao de outras linguagens, como por exemplo, em c++: int main()  
if __name__ == "__main__":
    #pass  comando que faz nada 
    tv = Televisao()
    tv.ligarTv()
    print(tv.ligada)

    tv.desligarTv()
    print(tv.ligada)

    tv.ligarTv()
    print(tv.ligada)

    tv.mudarCanal()
    print("Canal atual: " + str(tv.canal))
    tv.voltarCanal()
    print("Canal atual: " + str(tv.canal))


   # FUNÇÕES TRADICIONAL JÁ CONHECEMOS || def nomeFuncao(parametrox,y,z.....n) podendo ter n parametros

   #Função anônima (uso do lambda)

    soma = lambda a,b : a+b 
    print(soma(6,7))

