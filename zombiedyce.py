# Dyonata Eliezer Ambrosio Machado
# Jogo desenvolvido na disciplina Raciocínio Computacional 
# do curso de Análise e Desenvolvimento de Sistemas EAD da PUCPR

# Faz imports necessários para o código
import random
import os

# Define objeto Jogador com índice, nome e pontos
class Jogador:

    def __init__(self, indice, nome):
        self.indice = indice
        self.nome = nome
        self.pontos = 0

# Define objeto Dado com cor e string que representa as faces
class Dado:

    def __init__(self, cor):
        if(cor == "VERDE"):
            self.cor = cor
            self.faces = "CPCTPC"
        elif(cor == "AMARELO"):
            self.cor = cor
            self.faces = "TPCTPC"
        else:
            self.cor = cor
            self.faces = "TPTCPT"

# Define objeto Placar que representa o placar dos turnos
class Placar:

    def __init__(self):
        self.cerebros = 0
        self.tiros = 0
        self.passos = 0

# Função para limpar tela do console
def limpartela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Escreve a Mensagem Inicial e define a quantidade de jogadores

print("Bem-vindo ao Zombie Dice")
print("************************")
print("\n\n\n")

qtdJogadores = 0

while(qtdJogadores < 2):

    print("Informe a quantidade de jogadores")
    qtdJogadores = int(input())
    limpartela()

    if(qtdJogadores < 2):
        print("Informe ao menos dois jogadores")

# Cria lista para armazenar jogadores. Inicializa jogadores e adiciona em lista
listaJogadores = []

for i in range(0, qtdJogadores):
    indice = i + 1
    print("Informe o nome do {}º Jogador".format(indice))
    nome = input()
    limpartela()

    jogador = Jogador(indice, nome)
    listaJogadores.append(jogador)

# Cria variável e lista para auxiliar controle de ganhadores
haganhador = False
listaJogadoresComPontuacaoMaxima = []

# Inicia o jogo
print("Vamos começar o jogo")
input("Tecle Enter para continuar")
limpartela()

while(not haganhador):

    # Define jogador do turno e mensagem de interação com o mesmo
    for jogador in listaJogadores:

        print("Agora é a vez do Jogador #0{}: {}. Tecle para continuar".format(jogador.indice, jogador.nome))
        input()

        # Cria placar do turno
        placar = Placar()

        # Cria dados e listas necessárias para manipulá-los
        dadoVermelho = Dado("VERMELHO")
        dadoAmarelo = Dado("AMARELO")
        dadoVerde = Dado("VERDE")

        # Lista de todos os 13 dados do jogo
        listaDados = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
            dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo, 
            dadoVermelho, dadoVermelho, dadoVermelho]
        
        # Lista que armazena os dados que vão sendo sorteados
        listaDadosRetirados = []

        # Lista auxiliar que armazena temporariamente os dados que tiveram
        # como resultado de sorteio a face "PASSOS"
        listaDadosQueFoiSorteadoPassos = []

        # Variavel usada para verificar quantos dados retirar para sorteio
        qtdDadosARetirar = 3 

        while(True):
            
            # Retira dados para sorteio
            if(qtdDadosARetirar == 3):
                print("Você não tem nenhum dado em mãos")

            print("Tecle para receber {} dado(s)".format(qtdDadosARetirar))
            input()
            limpartela()

            for i in range(0, qtdDadosARetirar):

                numSorteado = random.randrange(0,len(listaDados))
                dadoRetirado = listaDados.pop(numSorteado)
                listaDadosRetirados.append(dadoRetirado)
                print("Você recebeu um dado {}".format(dadoRetirado.cor))
            
            # Sorteia a face dos dados e retorna resultado em tela
            print("\nAgora é a vez de rolar os dados.")
            input("{} tecle para continuar\n".format(jogador.nome))
            limpartela()

            while(len(listaDadosRetirados) > 0):
                dado = listaDadosRetirados[0] # Estrutura de Fila(FIFO)
                faces = dado.faces
                faceSorteada = random.choice(faces)

                if(faceSorteada == "T"):
                    print("Você levou um tiro com o dado {}".format(dado.cor))
                    listaDadosRetirados.pop(0) # Estrutura de Fila(FIFO)
                    placar.tiros += 1
                elif(faceSorteada == "C"):
                    print("Você comeu um cérebro com o dado {}".format(dado.cor))
                    listaDadosRetirados.pop(0) # Estrutura de Fila(FIFO)
                    placar.cerebros += 1
                else:
                    print("Um humano fugiu de você com o dado {}".format(dado.cor))
                    placar.passos += 1
                    dadoQueFoiSorteadoPassos = listaDadosRetirados.pop(0) # Estrutura de Fila(FIFO)
                    listaDadosQueFoiSorteadoPassos.append(dadoQueFoiSorteadoPassos)
            
            print("\nTecle para continuar")
            input()
            limpartela()
            
            # Mostra placar e interage para verificar se passa para o próximo jogador
            print("\nSeu placar atual do turno é:")
            print("Cérebros: {}\nTiros: {}\nPassos: {}".format(placar.cerebros, placar.tiros, placar.passos))

            input("Tecle ENTER para continuar")
            limpartela()
            
            # Jogador levou 3 tiros no turno
            if(placar.tiros > 2): # Passa para o próximo jogador direto
                print("Que pena você levou 3 ou mais tiros e não pontuou nesse turno.")
                input("Tecle ENTER para continuar")
                limpartela()
                break
            
            # Considera pontuação do jogador somado ao número de cérebros do turno atual
            # para verificar se jogador já atingiu placar máximo
            # não permite que jogador tenha mais que 13 pontos
            if((jogador.pontos + placar.cerebros) >= 13): 
                print("Uau, você comeu todos os cérebros possíveis e atingiu a pontuação máxima.")
                print("Você tem 13 pontos! Portanto agora é a vez do próximo jogador.")
                input("Tecle ENTER para continuar")
                limpartela()
                jogador.pontos = 13
                break
            
            # Verifica se jogador quer continuar rolando os dados no turno atual
            resposta = "C"
            while(resposta != "S" and resposta != "N" ):
                print("{}, vocẽ quer continuar a lançar os dados? Digite S para SIM ou N para NÃO".format(jogador.nome))
                resposta = input().upper()
                limpartela()
            
            if(resposta == "S"):
                
                # Verifica se jogador teve algum dado que teve "Passos" como resultado
                # e adiciona ele novamente a lista de dados retirados para que o jogador
                # jogue estes mesmos dados novamente. 

                if(placar.passos > 0):
                    print("Você continuará em mãos com o(s) seguinte(s) dado(s): ")
                    for dado in listaDadosQueFoiSorteadoPassos:
                        print(dado.cor)

                    listaDadosRetirados = listaDadosQueFoiSorteadoPassos.copy()
                    listaDadosQueFoiSorteadoPassos = []
                    placar.passos = 0

                    print("\nTecle para continuar")
                    input()
                    limpartela()

                # Define quantidade necessária a mais de dados para 
                # que jogador continue o turno atual
                qtdDadosARetirar = 3 - len(listaDadosRetirados)

                # Considera quantidade de dados disponíveis ainda a retirar
                if(len(listaDados) < qtdDadosARetirar):
                    qtdDadosARetirar = len(listaDados)       
            else:
                jogador.pontos += placar.cerebros
                print("Sua pontuação somando todas os turnos disputados até o momento é: {}".format(jogador.pontos))
                print("\nVamos continuar com o próximo jogador\n")
                print("Tecle Enter para continuar")
                input()
                limpartela()
                break
    
    # Mostra pontuação geral até o momento e armazena jogadores que tenham
    # atingido a pontuação máxima
    print("PONTUAÇÂO")
    print("*********")
    for jogador in listaJogadores:
        print("#0{} {}: {} ponto(s)".format(jogador.indice, jogador.nome, jogador.pontos))
        if(jogador.pontos == 13):
            indiceJogador = listaJogadores.index(jogador)
            jogadorComPontuacaoMaxima = listaJogadores.pop(indiceJogador)
            listaJogadoresComPontuacaoMaxima.append(jogadorComPontuacaoMaxima)
    
    input("Tecle para continuar\n")
    limpartela()
    
    # Verifica se há ganhador ou jogadores empatados com pontuação máxima, 
    # caso haja empate, reseta a pontuação e inicia rodada de desempate apenas
    # com os jogadores que atingiram pontuação máxima
    if(len(listaJogadoresComPontuacaoMaxima) == 1):
        haganhador = True
        print("Parabéns {} você é o ganhador. O melhor zumbi da cidade.".format(listaJogadoresComPontuacaoMaxima[0].nome))
        print("Tecle qualquer tecla para encerrar.")
        input()
        limpartela()
    elif(len(listaJogadoresComPontuacaoMaxima) > 1):
        print("Os seguintes jogadores atingiram a pontuação máxima: ")

        for jogador in listaJogadoresComPontuacaoMaxima:
            print("Jogador #0{0}: {1}".format(jogador.indice, jogador.nome))
            jogador.pontos = 0
        
        listaJogadores = listaJogadoresComPontuacaoMaxima.copy()
        listaJogadoresComPontuacaoMaxima = []

        print("\nSuas pontuações serão resetadas para uma rodada de desempate")
        input("Tecle para continuar")
        limpartela()
    else:
        print("Terminamos o turno e ainda não há ganhador")
        print("Cada jogador poderá jogar novamente os dados, mas lembre-se que você não poderá acumular mais do que 13 pontos.")
        input("Tecle para continuar")
        limpartela()