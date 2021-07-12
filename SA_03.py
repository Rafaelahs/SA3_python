#Situação de Aprendizagem 3


soma_total = 0
soma_recebido = 0



perg ='S'



if perg=='S':    
    while perg == 'S':
           val_total = float(input('Qual a valor da compra?'))
           soma_total =soma_total + val_total
           perg=str(input('"s"= sim, "n"=não\ntem mais alguma compra?s ou n?')).upper()
         
          
           
        
if perg==('N').upper():
    print("Valor total das compras: " , ("%.2f" % soma_total))
    val_recebido =float(input('Qual o valor que você vai pagar? '))

    
    if val_recebido<soma_total:
        valor_faltou = (val_recebido- soma_total)*-1
        print('Seu valor foi baixo do que valor de suas compras')
        print('faltou',   ("%.2f" % valor_faltou), 'R$')
        print('Tente novamente e pague corretamente')




        
    if val_recebido>soma_total:
        troco = val_recebido- soma_total
        print('----------------------')
        print("Valor total das compras: " , soma_total)
        print ('Valor Recebido: ',val_recebido )
        print('troco:  ' , ("%.2f" % troco))
        quant=troco
        nota = 200
        totalnot=0
        quant=troco
        
        while troco>0:
            if quant >=nota:
                quant = quant - nota
                totalnot = totalnot + 1
            else:
                if totalnot>0:
                   print(totalnot, 'Nota:', nota, 'R$')

           
                if nota == 200:
                    nota = 100
                elif nota ==100:
                     nota = 50
                elif nota ==50:
                     nota =20
                elif nota ==20:
                     nota =10
                elif nota ==10:
                     nota =5
                elif nota ==5:
                     nota =2
                elif nota ==2:
                     nota =1
                elif nota ==1:
                     nota =0.5

                elif nota ==0.5:
                     nota==0.25

                totalnot=0

                if quant==0:            
                    break
    
    
    if val_recebido==soma_total:
        notas = val_recebido- soma_total
        print('----------------------')
        print("Valor total das compras: " , soma_total)
        print ('Valor Recebido: ',val_recebido )
        print('Não é preciso de troco, obrigada pela compra<3') 
    
else:
    print('tente novamente e escreva o "s" ou "n" corretamente ')
   
        
    
    
    
    

    

 
  
   



    








