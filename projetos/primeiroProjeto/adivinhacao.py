print("********************************")
print("Bem vindo ao jogo de adivinhacao")
print("********************************")

numero_secreto = 42

chute_str = input("Digite seu palpite ")

print("Você digitou: ", chute_str)

chute = int(chute_str)
if(chute == numero_secreto):
    print("Você acertou!")
else:
    print("Errrrrôôôô!!")

print("Fim do jogo")



