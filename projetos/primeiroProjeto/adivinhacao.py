print("********************************")
print("Bem vindo ao jogo de adivinhacao")
print("********************************")

numero_secreto = 42

chute = input("Digite seu palpite ")

print("Você digitou: ", chute)

if(chute == numero_secreto):
    print("Você acertou!")
else:
    print("Errrrrôôôô!!")



