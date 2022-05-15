import listasQuiz
import random


def continuidade(linha):
    soma_sair = 0
    funcao_sair = 0
    while True:
        opcao = input()
        if opcao.lower().capitalize() == "Sim":
            break
        elif linha == 7 and opcao == "":   # Serve para validar o Enter da pergunta 8
            return ""
        elif linha >= 5 and soma_sair == 1:   # Funciona nas perguntas 7 e 8
            opcao = input("Não gostaria de finalizar o quiz? ")
            funcao_sair = sair(opcao)
        elif linha >= 1 and soma_sair == 1:  # Funciona da pergunta 2 até a 6
            opcao = input("Você quer continuar a fazer o quiz? ")
            funcao_sair = sair(opcao)
        elif soma_sair == 1:  # Serve para o início (introdução e pergunta 1) e para as alternativas inválidas
            opcao = input("Você quer mesmo fazer o quiz? ")
            funcao_sair = sair(opcao)
        else:
            print("Tente novamente!")
            soma_sair += 1
        if funcao_sair == "sair":
            break
    return 1


def sair(opcao):
    if opcao.lower().capitalize() == "Sim":
        return "sair"
    else:
        quit()


def perguntas(linha, coluna, pontos):
    coluna_justificativa = 0
    soma_respostas = 0
    lista_quases = ["Foi por pouco!", "Foi quase!", "Poxa, você quase acertou..."]

    print(f"\n{listasQuiz.listaPerguntas[linha][coluna]}")
    print(listasQuiz.listaPerguntas[linha][coluna+1])
    print()

    for j in range(5):
        print(listasQuiz.listaAlternativas[linha][j])
    print()

    while True:
        resposta = input("Qual a alternativa correta? ")
        resposta = resposta.upper()
        if resposta == "A" or resposta == "B" or resposta == "C" or resposta == "D" or resposta == "E":
            break
        else:
            soma_respostas += 1
            print("Digite uma alternativa possível!\n")
        if soma_respostas == 2:
            sair_perguntas = input("Você quer mesmo fazer o quiz? ")
            if sair_perguntas.lower().capitalize() == "Sim":
                soma_respostas = 0
            else:
                quit()

    if resposta == "A":
        coluna_justificativa = 0
    elif resposta == "B":
        coluna_justificativa = 1
    elif resposta == "C":
        coluna_justificativa = 2
    elif resposta == "D":
        coluna_justificativa = 3
    elif resposta == "E":
        coluna_justificativa = 4

    if resposta == listasQuiz.listaAcerto[linha][coluna]:
        print("Parabéns! Resposta correta!! \n[+100 pontos]")
        pontos += 100
        return 100
    elif resposta == listasQuiz.listaMeioAcerto[linha][coluna]:
        print(random.choice(lista_quases), end=" ")
        print(listasQuiz.listaJustificativas[linha][coluna_justificativa], "\n[+50 pontos]")
        pontos += 50
        return 50
    else:
        print("Poxa, você errou...", end=" ")
        print(listasQuiz.listaJustificativas[linha][coluna_justificativa])
        return 0


def prints(linha, pontos):
    lista_prox_pergunta = ["Próxima pergunta?", "Vamos para a próxima?", f"Vamos para a pergunta {linha + 2}?"]
    if linha != 7:
        print(f"\nPontuação Atual = {pontos} pontos")
    if linha == 3:  # Na pergunta 4
        print(f"Chegamos na metade! {random.choice(lista_prox_pergunta)}", end=" ")
    elif linha == 6:  # Na pergunta 7
        print("Última questão! Você está preparado(a)?", end=" ")
    elif linha == 7:  # Na pergunta 8
        return linha
    else:
        print(f"{random.choice(lista_prox_pergunta)}", end=" ")
    print("[Digite Sim ou Não]")


def classificacao(pontos):
    if pontos == 0:
        print(listasQuiz.listaClassificacao[0])
    elif pontos <= 150:
        print(listasQuiz.listaClassificacao[1])
    elif pontos <= 350:
        print(listasQuiz.listaClassificacao[2])
    elif pontos <= 550:
        print(listasQuiz.listaClassificacao[3])
    elif pontos <= 750:
        print(f"Por pouco você não gabarita! Mas parabéns, você fez {pontos} pontos! \n{listasQuiz.listaClassificacao[4]}")
    else:
        print(f"Parabéns, você atingiu a pontuação máxima!! \n{listasQuiz.listaClassificacao[5]}")
