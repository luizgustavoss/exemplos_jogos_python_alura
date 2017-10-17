import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = round(int(random.randrange(1, 100)))
    acertou = False
    tentativas = 0
    pontos = 1000
    pontos_perdidos = 0

    while (not acertou):
        tentativas += 1
        chute_str = input("Digite o seu número: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve escolher um número entre 0 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou!")

            pontos -= pontos_perdidos

            print("Tentativas: ", tentativas, sep=" ")
            print("Pontos: ", pontos, sep=" ")
            print("Pontos Perdidos: ", pontos_perdidos, sep=" ")
        else:
            if(maior):
                print("O seu chute ({}) foi maior do que o número secreto!".format(chute), end="\n")
            elif(menor):
                print("O seu chute ({}) foi menor do que o número secreto!".format(chute), end="\n")
            pontos_perdidos += abs(numero_secreto - chute)


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()