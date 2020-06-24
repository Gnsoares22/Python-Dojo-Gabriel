soma = 0 # variavel inicialmente é zerada
i = 0


# lembrando que os índices sempre começam com zero (0,1,2,3) <- totalizando 4 elementos (contando com zero), ou melhor,
# 4 notas
while i < 4: # vai incrementando até i que vale 0, se tornar igual a 4 
   nota = float(input("Digite a {} nota: ".format(i))) # digita as notas no formato float
   
   while nota < 0 or nota > 10: # Esse loop é executado
      # gerando a mensagem abaixo ATÉ que você digite uma nota maior/igual a 0 OU menor/igual a 10
      print("Nota deve ser um número entre 0 e 10 !!!")
      nota = float(input("Digite a {} nota: ".format(i)))


   soma += nota # As notas são somadas a cada iteração do primeiro while 
   i+=1 # itera o while, incrementando + 1 em i, até que i seja igual a 4 


print("Média: {:.2f}".format(soma / i)) # como i vale 4 (0,1,2,3) eu pego a váriavel coma e divido por ele
# obtendo assim a média de "4" NOTAS !!


#:.2f faz o resultado da média ser obtido com duas casas após a vírgula
