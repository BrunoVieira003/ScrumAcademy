def jogo():

    tentativas = []
    acertos = 0
    num = 1

    for k in questoes:
        print("-------------------------")
        print(k)
        for i in opcoes[num-1]:
            print(i)
        tentativa = input("Enter (A, B, C, or D): ")
        tentativa = tentativa.upper()
        tentativas.append(tentativa)

        acertos += checar(questoes.get(k), tentativa)
        num += 1

    pontuacao(acertos, tentativas)


def checar(resposta, tentativa):

    if resposta == tentativa:
        print("Acertou!")
        return 1
    else:
        print("Errou")
        return 0


def pontuacao(acertos, tentativas):
    print("-------------------------")
    print("Resultados")
    print("-------------------------")

    print("Gabarito: ", end="")
    for i in questoes:
        print(questoes.get(i), end=" ")
    print()

    print("Suas respostas: ", end="")
    for i in tentativas:
        print(i, end=" ")
    print()

    score = int((acertos/len(questoes))*100)
    print("Porcentagem de acertos: "+str(score)+"%")


def novamente():

    denovo = input("Quer tentar novamente?(sim ou nao): ")
    denovo = denovo.upper()

    if denovo == "SIM":
        return True
    else:
        return False



questoes = {
 "Qual das opções é uma responsabilidade do Product Owner: ": "A",
 "Qual ferramenta pode ser utilizada para determinar o tempo de uma atividade'?: ": "B",
 "Qual destas é uma soft skill?: ": "C",
 "Qual destas é uma qualidade de uma boa equipe de desenvolvimento?: ": "A"
}

opcoes = [["A. Entender a visão e os objetivos do produto e da empresa.", "B. Identificar e resolver conflitos internos", "C. Ordenar o que cada integrante da equipe deve fazer", "D. Reunir a equipe para comer bolo"],
          ["A. MVP", "B. Planning Poker", "C. Burndown", "D. Product Backlog"],
          ["A. Método Scrum", "B. Fluência em inglês", "C. Comunicação", "D. Saber utilizar tecnologias"],
          ["A. Trabalho colaborativo","B. Trabalho sem comunicação", "C. Equipe individualista", "D. Entregas sempre atrasadas"]]


jogo()

while novamente():
    jogo()