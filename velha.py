# Cria uma matriz 3x3 que representa o tabuleiro do jogo da velha
from random import randint
def criaMatriz():
    mat = [["1", "2", "3"],
           ["4", "5", "6"],
           ["7", "8", "9"]]
    return mat

#def apresentaMatriz(mat):define a função apresentaMatriz()que recebe uma matriz mat como argumento.
#print("-------------")imprime uma linha horizontal para separar as linhas do tabuleiro.
#for i in range(3):inicia um loop que itera sobre os índices das linhas do tabuleiro. O tabuleiro possui 3 linhas numeradas de 0 a 2.
#print("|", end=" ")imprima um caractere "|" para delimitar as colunas do tabuleiro. O parâmetro end=" "é usado para evitar que a função print()pule para a próxima linha após imprimir o caractere "|" e continue na mesma linha.
#for j in range(3):inicia um loop que itera sobre os índices das colunas do tabuleiro. O tabuleiro possui 3 colunas numeradas de 0 a 2.
#print(matriz[i][j], "|", end=" ")imprime o valor da posição matriz[i][j]do tabuleiro, seguido de um caractere "|", para delimitar as colunas. O parâmetro end=" "é usado novamente para evitar que a função print()pule para a próxima linha.
#print("\n-------------")imprime uma linha horizontal após cada linha do tabuleiro, para separar as linhas.

def apresentaMatriz(mat):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(matriz[i][j], "|", end=" ")
        print("\n-------------")


#def posicaoOcupada(matriz, posicao): define a função posicaoOcupada() que recebe uma matriz e uma posição como argumentos.
#for i in range(3): inicia um loop que itera sobre os índices das linhas do tabuleiro. O tabuleiro possui 3 linhas numeradas de 0 a 2.
#for j in range(3): inicia um loop alinhado que itera sobre os índices das colunas do tabuleiro. O tabuleiro possui 3 colunas numeradas de 0 a 2.
#if matriz[i][j] == str(posicao): verifica se o valor da posição matriz[i][j], convertido para string, é igual à posição desejada.
#return False retorna False imediatamente se a posição estiver ocupada, indicando que a posição escolhida já está ocupada.
#return True se a posição estiver livre

def posicaoOcupada(matriz, posicao):
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == str(posicao):
                return False
    return True

# Função que verifica se um jogador venceu o jogo da velha.
#Args:
      #matriz (list): A matriz representando o tabuleiro do jogo da velha.
      #jogador (str): A marca do jogador ('X' ou 'O').
      #Returns:
     # bool: True se o jogador venceu, False caso contrário.

def verificarVitoria(matriz, jogador):
    for i in range(3):
        # Verifica se o jogador preencheu uma linha
        if matriz[i][0] == matriz[i][1] == matriz[i][2] == [jogador]:
            return True

    for j in range(3):
        # Verifica se o jogador preencheu uma coluna
        if matriz[0][j] == matriz[1][j] == matriz[2][j] == [jogador]:
            return True

    # Verifica se o jogador preencheu a diagonal principal
    if matriz[0][0] == matriz[1][1] == matriz[2][2] == [jogador]:
        return True

    # Verifica se o jogador preencheu a diagonal secundária
    if matriz[0][2] == matriz[1][1] == matriz[2][0] == [jogador]:
        return True

    # Caso nenhuma condição de vitória seja satisfeita, retorna False
    return False


print("*** JOGO DA VELHA ***\n")
print("Desafie o seu colega no jogo da velha.\n")
print("Regras:\n a) O primeiro jogador participará com a letra X e o segundo com a letra O.")
print(" b) Os números de 1 a 9 representam os espaços que estão livres.")
print(" c) Você só poderá escolher as posições livres.")
print(" d) O vencedor será o primeiro jogador a preencher uma linha, uma coluna ou uma diagonal.")

matriz = criaMatriz()
jogador = "X"
c = 0

while c < 9:
    # Apresenta o tabuleiro do jogo
    apresentaMatriz(matriz)

    # Solicita a posição desejada pelo jogador
    posicao = int(input(f"(Jogador {jogador}) Informe a posição desejada: "))


    if posicaoOcupada(matriz, posicao):
        if posicao <= 0:
          print('\033[0:31m DIGITE UM NUMERO MAIOR QUE 0!!\033[m')
          continue

        print("\nVocê não pode escolher uma posição que já está ocupada. Tente novamente.")
        continue
    else:
        for i in range(3):
            for j in range(3):
                if matriz[i][j] == str(posicao):
                    # Atualiza a matriz com a marca do jogador na posição escolhida
                    matriz[i][j] = jogador

        if verificarVitoria(matriz, jogador):
            # Verifica se o jogador venceu o jogo
            apresentaMatriz(matriz)
            print(f"\nO jogador {jogador} venceu!")
            break

        # Alterna o jogador atual entre "X" e "O"
        jogador = "O" if jogador == "X" else "X"
        c += 1
else:
    apresentaMatriz(matriz)
    print("\nDEU VELHA!")
