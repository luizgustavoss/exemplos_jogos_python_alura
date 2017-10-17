import random

def jogar():

    apresentar_jogo()

    # variáveis de controle para saber se o usuário já errou todas as
    # chances que tinha ou se acertou a palavra
    perdeu = False
    acertou = False

    # a forca como vai sendo desenhada
    forca_mostrar = ""
    # preparando o desenho da forca
    forca = preparar_forca()
    palavra_secreta = selecionar_palavra_secreta()

    letras_sugeridas = {()}

    # construção da palavra com os acertos do usuário
    letras_acertadas = iniciarlizar_lista_letras(palavra_secreta)

    while(not perdeu and not acertou):

        print(forca_mostrar)
        print("Palavra {}".format(letras_acertadas))

        chute = solicitar_input_usuario()

        if chute in letras_sugeridas:
            print("Você já sugeriu esta letra antes!")
            continue

        letras_sugeridas.add(chute)

        algum_acerto = marca_chute(palavra_secreta, chute, letras_acertadas)

        if not algum_acerto:
            forca_mostrar = forca_mostrar + forca.pop()

        if letras_acertadas.count("_") == 0:
            acertou = True
            imprime_mensagem_vencedor()
            print("A palavra secreta é: '{}' ".format(palavra_secreta))

        if len(forca) == 0:
            perdeu = True
            print("VOCÊ PERDEU!")
            print(forca_mostrar)


def apresentar_jogo():

    print("*********************************** ")
    print("*** Bem vindo ao jogo da Forca! *** ")
    print("*********************************** ")


def preparar_forca():
    # preparando o desenho da forca
    forca = [" 0 \n", "/", "|", "\\\n", "/ ", "\\"]
    forca.reverse()
    return forca


def selecionar_palavra_secreta():

    # lendo o arquivo que contém as definições de palavras
    arquivo = open("frutas.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    indice = random.randrange(0, len(palavras))

    # a palavra que precisa ser descoberta (ainda fixo)
    return  palavras[indice]


def iniciarlizar_lista_letras(palavra_secreta):

    letras_acertadas = ["_" for ps in palavra_secreta]
    return letras_acertadas


def solicitar_input_usuario():

    chute = input("Informe uma letra: \n");
    chute = chute.strip()
    return chute


def marca_chute(palavra_secreta, chute, letras_acertadas):
    index = 0
    algum_acerto = False
    for letra in palavra_secreta:
        if (letra.lower() == chute.lower()):
            # print("Encontrada a letra {} na posição {} ".format(letra, index))
            letras_acertadas[index] = letra
            algum_acerto = True
        index += 1
    return algum_acerto


def imprime_mensagem_vencedor():
    print(" Parabéns, você ganhou! ")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")



if(__name__ == "__main__"):
    jogar()