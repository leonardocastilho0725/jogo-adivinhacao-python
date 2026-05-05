import random

def jogar():
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    # primeiro peço para o programa um numero aleatorio sempre que for rodar


    print('='*30)
    print("bem vindo ao jogo, adivinhe o numero")
    print('='*30)
    #interface

    while True:
        palpite =int(input("digite seu chute: "))
        tentativas+=1
        if palpite == numero_secreto:
            print(f"parabens, voce acertou em {tentativas} tentativas!")
            break
        elif palpite > numero_secreto:
            print("tente um numero menor")
        else:
            print("tente um numero maior")
            
    # faço um laço de repetiçao com o while, o usuario fica em um looping até acertar o numero.
    # para facilitar utilizo um if, elif e else para dizer se o chute tem que ser menor ou maior, e sempre contando quantas tentativas ja foram.


jogar()