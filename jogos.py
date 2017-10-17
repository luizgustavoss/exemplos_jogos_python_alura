import forca
import adivinhacao


def escolhe_jogo():

    print("*********************************")
    print("        Escolha seu Jogo         ")
    print("*********************************")


    print("Escolha seu Jogo (1) Forca ou (2) Advinhação ")

    jogo = int(input("Qual Jogo?"))

    if(jogo == 1):
        print("Jogo da Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogo da Adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()