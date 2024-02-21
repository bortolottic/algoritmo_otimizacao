import heapq

class JogoDaVelha:
    def __init__(self, tabuleiro, jogador):
        self.tabuleiro = tabuleiro
        self.jogador = jogador

    def gerar_movimentos(self):
        movimentos = []
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == '-':
                    novo_tabuleiro = [row[:] for row in self.tabuleiro]
                    novo_tabuleiro[i][j] = self.jogador
                    movimentos.append(JogoDaVelha(novo_tabuleiro, 'X' if self.jogador == 'O' else 'O'))
        return movimentos

    def avaliar_heuristica(self):
        # Conta o número de espaços vazios no tabuleiro
        count = 0
        for row in self.tabuleiro:
            count += row.count('-')
        return count

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
        return self.avaliar_heuristica() < other.avaliar_heuristica()

def a_estrela(jogo):
    fila_prioridade = [(jogo.avaliar_heuristica(), jogo)]
    while fila_prioridade:
        _, estado = heapq.heappop(fila_prioridade)
        if estado.is_terminal():
            return estado
        for proximo_estado in estado.gerar_movimentos():
            heapq.heappush(fila_prioridade, (proximo_estado.avaliar_heuristica(), proximo_estado))
    return None

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
    jogo_inicial = JogoDaVelha(tabuleiro_inicial, 'X')

    while not jogo_inicial.is_terminal():
        imprimir_tabuleiro(jogo_inicial.tabuleiro)
        movimento_jogador = input("Digite a sua jogada (linha coluna): ").split()
        linha, coluna = map(int, movimento_jogador)
        if jogo_inicial.tabuleiro[linha][coluna] == '-':
            jogo_inicial.tabuleiro[linha][coluna] = 'O'
        else:
            print("Posição ocupada. Tente novamente.")
            continue

        if jogo_inicial.is_terminal():
            break

        melhor_jogada = a_estrela(jogo_inicial)
        if melhor_jogada:
            jogo_inicial = melhor_jogada

    imprimir_tabuleiro(jogo_inicial.tabuleiro)
    if jogo_inicial.avaliar_heuristica() > 0:
        print("Você ganhou!")
    elif jogo_inicial.avaliar_heuristica() < 0:
        print("Você perdeu!")
    else:
        print("Empate!")    
