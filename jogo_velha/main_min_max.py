import heapq

class JogoDaVelha:
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro

    def gerar_movimentos(self, jogador):
        movimentos = []
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == '-':
                    novo_tabuleiro = [row[:] for row in self.tabuleiro]
                    novo_tabuleiro[i][j] = jogador
                    movimentos.append(JogoDaVelha(novo_tabuleiro))
        return movimentos

    def avaliar(self):
        # Avaliação simples: contar as ocorrências de X e O
        contador_x = 0
        contador_o = 0
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == 'X':
                    contador_x += 1
                elif self.tabuleiro[i][j] == 'O':
                    contador_o += 1
        return contador_o - contador_x

    def is_terminal(self):
        # Verifica se alguém ganhou ou se o tabuleiro está cheio
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != '-':
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != '-':
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != '-':
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != '-':
            return True
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == '-':
                    return False
        return True

    def __lt__(self, other):
        return self.avaliar() < other.avaliar()

def minimax(node, depth, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.avaliar()
    if maximizing_player:
        max_eval = float('-inf')
        for movimento in node.gerar_movimentos('X'):
            eval = minimax(movimento, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for movimento in node.gerar_movimentos('O'):
            eval = minimax(movimento, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def encontrar_melhor_jogada(node):
    melhor_jogada = None
    max_eval = float('-inf')
    for movimento in node.gerar_movimentos('X'):
        eval = minimax(movimento, 10, False) # profundidade pode ser ajustada
        if eval > max_eval:
            max_eval = eval
            melhor_jogada = movimento
    return melhor_jogada

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))
    print()

if __name__ == "__main__":
    tabuleiro_inicial = [
        ['-','-','-'],
        ['-','-','-'],
        ['-','-','-']
    ]
    jogo = JogoDaVelha(tabuleiro_inicial)

    while not jogo.is_terminal():
        imprimir_tabuleiro(jogo.tabuleiro)
        movimento_jogador = input("Digite a sua jogada (linha coluna): ").split()
        linha, coluna = map(int, movimento_jogador)
        if jogo.tabuleiro[linha][coluna] == '-':
            jogo.tabuleiro[linha][coluna] = 'O'
        else:
            print("Posição ocupada. Tente novamente.")
            continue

        if jogo.is_terminal():
            break

        melhor_jogada = encontrar_melhor_jogada(jogo)
        if melhor_jogada:
            jogo = melhor_jogada

    imprimir_tabuleiro(jogo.tabuleiro)
    if jogo.avaliar() > 0:
        print("Você ganhou!")
    elif jogo.avaliar() < 0:
        print("Você perdeu!")
    else:
        print("Empate!")
