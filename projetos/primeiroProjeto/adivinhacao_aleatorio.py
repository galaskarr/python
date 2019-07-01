import random

print("********************************")
print("Bem vindo ao jogo de adivinhacao")
print("********************************")

numero_secreto = random.randrange(1,101)

numero_tentativas = 3
rodada = 1

#while(numero_tentativas > 0):
while(rodada <= numero_tentativas):

    print("Tentativa {} de {}".format(rodada, numero_tentativas))
    chute_str = input("Digite seu palpite ")

    print("Você digitou: ", chute_str)

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if(chute == numero_secreto):
        print("Você acertou!")
    else:
        print("Errrrrôôôô!!")
        if(menor == True):
            print("Palpitou abaixo do número secreto")
        elif(maior == True):
            print("Palpitou acima do número secreto")
        else:
            print("Palpitou exatamente o número secreto")

    #if (acertou == False):
    #        numero_tentativas = numero_tentativas - 1
    #else:
    #    fim do jogo é antecipado
    #    numero_tentativas = 0

    rodada = rodada + 1

print("Fim do jogo")



