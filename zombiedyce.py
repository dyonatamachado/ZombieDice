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
            self.faces = ('C','P','C','T','P','C')
        elif(cor == "AMARELO"):
            self.cor = cor
            self.faces = ('T','P','C','T','P','C')
        else:
            self.cor = cor
            self.faces = ('T','P','T','C','P','T')

# Define objeto Placar que representa o placar dos turnos
class Placar:

    def __init__(self):
        self.cerebros = 0
        self.tiros = 0
        self.passos = 0

# Função para limpar tela do console
def limpartela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para escrever a Mensagem Inicial
def mostrar_mensagem_inicial():
    print("Bem-vindo ao Zombie Dice")
    print("************************")
    print("\n\n\n")

# Função para definir a quantidade de jogadores
def definir_quantidade_jogadores(limpartela):
    qtdJogadores = 0

    while(qtdJogadores < 2):
        print("Informe a quantidade de jogadores")
        qtdJogadores = int(input())
        limpartela()

        if(qtdJogadores < 2):
            print("Informe ao menos dois jogadores")
    return qtdJogadores

# Função para criar e armazenar jogadores em lista
def criar_e_armazenar_jogadores(limpartela, qtdJogadores):
    listaJogadores = []

    for i in range(0, qtdJogadores):
        indice = i + 1
        print("Informe o nome do {}º Jogador".format(indice))
        nome = input()
        limpartela()

        jogador = Jogador(indice, nome)
        listaJogadores.append(jogador)
    return listaJogadores

def criar_dados_e_listas_para_manipulalos():
    dadoVermelho = Dado("VERMELHO")
    dadoAmarelo = Dado("AMARELO")
    dadoVerde = Dado("VERDE")

    listaDados = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
            dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo, 
            dadoVermelho, dadoVermelho, dadoVermelho]
        
    # Lista que armazena os dados que vão sendo sorteados
    listaDadosRetirados = []

    # Lista auxiliar que armazena temporariamente os dados que tiveram
    # como resultado de sorteio a face "PASSOS"
    listaDadosQueFoiSorteadoPassos = []

    return listaDados,listaDadosRetirados,listaDadosQueFoiSorteadoPassos

def retirar_dados(listaDados, listaDadosRetirados):
    numSorteado = random.randrange(0,len(listaDados))
    dadoRetirado = listaDados.pop(numSorteado)
    listaDadosRetirados.append(dadoRetirado)
    print("Você recebeu um dado {}".format(dadoRetirado.cor))

def sortear_faces(dado):
    faces = dado.faces
    faceSorteada = random.choice(faces)
    return faceSorteada

# Funções get_tiro, get_cerebro e get_passos são responsáveis por receber o 
# resultado do sorteio do dado e aplicar as consequências
def get_tiro(placar, listaDadosRetirados, dado):
    print("Você levou um tiro com o dado {}".format(dado.cor))
    listaDadosRetirados.pop(0)
    placar.tiros += 1

def get_cerebro(placar, listaDadosRetirados, dado):
    print("Você comeu um cérebro com o dado {}".format(dado.cor))
    listaDadosRetirados.pop(0)
    placar.cerebros += 1

def get_passos(placar, listaDadosRetirados, listaDadosQueFoiSorteadoPassos, dado):
    print("Um humano fugiu de você com o dado {}".format(dado.cor))
    placar.passos += 1
    dadoQueFoiSorteadoPassos = listaDadosRetirados.pop(0)
    listaDadosQueFoiSorteadoPassos.append(dadoQueFoiSorteadoPassos)

def encerrar_turno_caso_jogador_leve_mais_de_dois_tiros(limpartela, mensagem_tecle_enter):
    print("Que pena você levou 3 ou mais tiros e não pontuou nesse turno.")
    input(mensagem_tecle_enter)
    limpartela()

def encerrar_turno_caso_jogador_coma_todos_os_cerebros(limpartela, mensagem_tecle_enter, jogador):
    print("Uau, você comeu todos os cérebros possíveis e atingiu a pontuação máxima.")
    print("Você tem 13 pontos! Portanto agora é a vez do próximo jogador.")
    input(mensagem_tecle_enter)
    limpartela()
    jogador.pontos = 13

def perguntar_se_jogador_deseja_continuar_seu_turno(limpartela, jogador):
    print("{}, vocẽ quer continuar a lançar os dados? Digite S para SIM ou N para NÃO".format(jogador.nome))
    resposta = input().upper()
    limpartela()
    return resposta

def encerrar_turno_caso_jogador_escolha_encerrar(limpartela, mensagem_tecle_enter, jogador, placar):
    jogador.pontos += placar.cerebros
    print("Sua pontuação somando todas os turnos disputados até o momento é: {}".format(jogador.pontos))
    print("\nVamos continuar com o próximo jogador\n")
    print(mensagem_tecle_enter)
    input()
    limpartela()

def guardar_dado_que_teve_resultado_passos_para_jogar_novamente(placar, listaDadosQueFoiSorteadoPassos):
    listaDadosRetirados = listaDadosQueFoiSorteadoPassos.copy()
    listaDadosQueFoiSorteadoPassos = []
    placar.passos = 0
    return listaDadosRetirados, listaDadosQueFoiSorteadoPassos

def gerenciar_e_imprimir_pontuacao_geral(listaJogadores, listaJogadoresComPontuacaoMaxima):
    print("PONTUAÇÂO")
    print("*********")
    
    for jogador in listaJogadores:
        print("#0{} {}: {} ponto(s)".format(jogador.indice, jogador.nome, jogador.pontos))
    
def avaliar_se_jogador_esta_com_pontuacao_maxima(listaJogadores, listaJogadoresComPontuacaoMaxima):
    for jogador in listaJogadores:
        if(jogador.pontos == 13):
            armazenar_jogadores_com_pontuacao_maxima(listaJogadores, listaJogadoresComPontuacaoMaxima, jogador)

def armazenar_jogadores_com_pontuacao_maxima(listaJogadores, listaJogadoresComPontuacaoMaxima, jogador):
    indiceJogador = listaJogadores.index(jogador)
    jogadorComPontuacaoMaxima = listaJogadores[indiceJogador]
    listaJogadoresComPontuacaoMaxima.append(jogadorComPontuacaoMaxima)

def imprimir_ganhador_caso_haja(limpartela, listaJogadoresComPontuacaoMaxima):
    teste_haganhador = True
    print("Parabéns {} você é o ganhador. O melhor zumbi da cidade.".format(listaJogadoresComPontuacaoMaxima[0].nome))
    print("Tecle qualquer tecla para encerrar.")
    input()
    limpartela()
    return teste_haganhador

def imprimir_jogadores_com_pontuacao_maxima_e_iniciar_turno_desempate(limpartela, mensagem_tecle_enter, listaJogadoresComPontuacaoMaxima):
    print("Os seguintes jogadores atingiram a pontuação máxima: ")

    for jogador in listaJogadoresComPontuacaoMaxima:
        print("Jogador #0{0}: {1}".format(jogador.indice, jogador.nome))
        jogador.pontos = 0
        
    listaJogadores = listaJogadoresComPontuacaoMaxima.copy()
    listaJogadoresComPontuacaoMaxima = []

    print("\nSuas pontuações serão resetadas para uma rodada de desempate")
    input(mensagem_tecle_enter)
    limpartela()

    return listaJogadores, listaJogadoresComPontuacaoMaxima

def continuar_jogo_caso_nao_haja_ganhador(limpartela):
    print("Terminamos o turno e ainda não há ganhador")
    print("Cada jogador poderá jogar novamente os dados, mas lembre-se que você não poderá acumular mais do que 13 pontos.")
    input("Tecle para continuar")
    limpartela()

mensagem_tecle_enter = "Tecle ENTER para continuar"
mostrar_mensagem_inicial()
qtdJogadores = definir_quantidade_jogadores(limpartela)
listaJogadores = criar_e_armazenar_jogadores(limpartela, qtdJogadores)

# Cria variável e lista para auxiliar controle de ganhadores
haganhador = False
listaJogadoresComPontuacaoMaxima = []

# Inicia o jogo
print("Vamos começar o jogo")
input(mensagem_tecle_enter)
limpartela()


while(not haganhador):

    # Define jogador do turno e mensagem de interação com o mesmo
    for jogador in listaJogadores:

        print("Agora é a vez do Jogador #0{}: {}. Tecle para continuar".format(jogador.indice, jogador.nome))
        input()

        # Cria placar do turno
        placar = Placar()

        # Chama função para criar dados e listas que os manipulam
        listaDados, listaDadosRetirados, listaDadosQueFoiSorteadoPassos = criar_dados_e_listas_para_manipulalos()

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

                retirar_dados(listaDados, listaDadosRetirados)
            
            # Sorteia a face dos dados e retorna resultado em tela
            print("\nAgora é a vez de rolar os dados.")
            input("{} tecle para continuar\n".format(jogador.nome))
            limpartela()

            # Os índices estão todos com o valor 0 pois trabalho com estrutra de fila (FIFO)
            while(len(listaDadosRetirados) > 0):
                dado = listaDadosRetirados[0]
                faceSorteada = sortear_faces(dado)

                if(faceSorteada == "T"):
                    get_tiro(placar, listaDadosRetirados, dado)
                elif(faceSorteada == "C"):
                    get_cerebro(placar, listaDadosRetirados, dado)
                else:
                    get_passos(placar, listaDadosRetirados, listaDadosQueFoiSorteadoPassos, dado)
            
            print("\nTecle para continuar")
            input()
            limpartela()
            
            # Mostra placar e interage para verificar se passa para o próximo jogador
            print("\nSeu placar atual do turno é:")
            print("Cérebros: {}\nTiros: {}\nPassos: {}".format(placar.cerebros, placar.tiros, placar.passos))

            input(mensagem_tecle_enter)
            limpartela()
            
            
            if(placar.tiros > 2): # Passa para o próximo jogador direto
                encerrar_turno_caso_jogador_leve_mais_de_dois_tiros(limpartela, mensagem_tecle_enter)
                break
            if((jogador.pontos + placar.cerebros) >= 13): 
                encerrar_turno_caso_jogador_coma_todos_os_cerebros(limpartela, mensagem_tecle_enter, jogador)
                break
            
            # Verifica se jogador quer continuar rolando os dados no turno atual
            resposta = "C"
            while(resposta != "S" and resposta != "N" ):
                resposta = perguntar_se_jogador_deseja_continuar_seu_turno(limpartela, jogador)
            
            if(resposta == "S"):
                
                # Verifica se jogador teve algum dado que teve "Passos" como resultado
                # e adiciona ele novamente a lista de dados retirados para que o jogador
                # jogue estes mesmos dados novamente. 

                if(placar.passos > 0):
                    print("Você continuará em mãos com o(s) seguinte(s) dado(s): ")
                    for dado in listaDadosQueFoiSorteadoPassos:
                        print(dado.cor)

                    listaDadosRetirados, listaDadosQueFoiSorteadoPassos = guardar_dado_que_teve_resultado_passos_para_jogar_novamente(placar, listaDadosQueFoiSorteadoPassos)

                    print()
                    print(mensagem_tecle_enter)
                    input()
                    limpartela()

                # Define quantidade necessária a mais de dados para 
                # que jogador continue o turno atual
                qtdDadosARetirar = 3 - len(listaDadosRetirados)

                # Considera quantidade de dados disponíveis ainda a retirar
                if(len(listaDados) < qtdDadosARetirar):
                    qtdDadosARetirar = len(listaDados)       
            else:
                encerrar_turno_caso_jogador_escolha_encerrar(limpartela, mensagem_tecle_enter, jogador, placar)
                break
    
    # Mostra pontuação geral até o momento e armazena jogadores que tenham
    # atingido a pontuação máxima
    gerenciar_e_imprimir_pontuacao_geral(listaJogadores, listaJogadoresComPontuacaoMaxima)
    avaliar_se_jogador_esta_com_pontuacao_maxima(listaJogadores, listaJogadoresComPontuacaoMaxima)
    
    input(mensagem_tecle_enter)
    limpartela()
    
    # Controla se há ganhadores
    if(len(listaJogadoresComPontuacaoMaxima) == 1):
        haganhador = imprimir_ganhador_caso_haja(limpartela, listaJogadoresComPontuacaoMaxima)
    elif(len(listaJogadoresComPontuacaoMaxima) > 1):
        listaJogadores, listaJogadoresComPontuacaoMaxima = imprimir_jogadores_com_pontuacao_maxima_e_iniciar_turno_desempate(limpartela, mensagem_tecle_enter, listaJogadoresComPontuacaoMaxima)
    else:
        continuar_jogo_caso_nao_haja_ganhador(limpartela)