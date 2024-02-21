import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.parent = parent
        self.move = move
        self.dimension = len(board)
        self.goal_state = self.get_goal_state()
    
    def __lt__(self, other):
        return self.heuristic() < other.heuristic()
    
    def __eq__(self, other):
        return self.board == other.board
    
    def __hash__(self):
        return hash(str(self.board))
    
    def get_goal_state(self):
        goal_board = [[0] * self.dimension for _ in range(self.dimension)]
        num = 1
        for i in range(self.dimension):
            for j in range(self.dimension):
                goal_board[i][j] = num
                num = (num + 1) % (self.dimension ** 2)
        goal_board[self.dimension - 1][self.dimension - 1] = 0
        return goal_board
    
    def find_blank_position(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.board[i][j] == 0:
                    return i, j
    
    def heuristic(self):
        # Heuristic function: Manhattan distance
        distance = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.board[i][j] != 0:
                    value = self.board[i][j] - 1
                    goal_row = value // self.dimension
                    goal_col = value % self.dimension
                    distance += abs(i - goal_row) + abs(j - goal_col)
        return distance
    
    def successors(self):
        successors = []
        row, col = self.find_blank_position()
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.dimension and 0 <= new_col < self.dimension:
                new_board = [row[:] for row in self.board]
                new_board[row][col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[row][col]
                successors.append(PuzzleState(new_board, parent=self, move=(new_row, new_col)))
        return successors
    
    def is_goal_state(self):
        return self.board == self.goal_state

def solve_puzzle(initial_state):
    open_set = [initial_state]
    closed_set = set()
    
    while open_set:
        current_state = heapq.heappop(open_set)
        if current_state.is_goal_state():
            return construct_path(current_state), len(closed_set) + 1
        closed_set.add(current_state)
        successors = current_state.successors()
        for successor in successors:
            if successor not in closed_set:
                heapq.heappush(open_set, successor)
    return None, len(closed_set) + 1

def construct_path(state):
    path = []
    while state:
        path.append(state)
        state = state.parent
    return path[::-1]

# Configuração inicial
initial_board = [
    [2, 8, 3],
    [1, 6, 0],
    [4, 7, 5]
]

initial_state = PuzzleState(initial_board)

# Resolver o puzzle
path, num_moves = solve_puzzle(initial_state)

if path:
    print("Solução encontrada em {} movimentos:".format(num_moves))
    for i, state in enumerate(path):
        print("Movimento #{}:".format(i + 1))
        for row in state.board:
            print(row)
        print()
else:
    print("Não há solução para o puzzle.")
