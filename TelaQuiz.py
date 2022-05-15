import funcoesQuiz


def main():
    linha_main = 0
    coluna_main = 0
    pontos = 0
    print("Pergunta Inicial\nVamos começar? [Digite Sim ou Não]")
    funcoesQuiz.continuidade(linha_main)
    print("Então vamos lá!")

    for x in range(8):
        pontos += funcoesQuiz.perguntas(linha_main, coluna_main, pontos)
        linha = funcoesQuiz.prints(linha_main, pontos)
        if linha == 7:
            break
        linha_main += funcoesQuiz.continuidade(linha_main)

    print("\nChegamos ao fim do Quiz!! Seu resultado foi... [Clique Enter] ")
    while True:
        mostrar_resultado = funcoesQuiz.continuidade(linha_main)
        if mostrar_resultado != "":
            print("[Clique Enter para ver seu resultado]")
        else:
            break

    funcoesQuiz.classificacao(pontos)


main()
