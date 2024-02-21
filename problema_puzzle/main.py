from queue import PriorityQueue

# Função para calcular a heurística (número de peças fora do lugar)
def heuristic(state, goal):
    count = 0
    for i in range(len(state)):
        if state[i] != goal[i]:
            count += 1
    return count

# Função para verificar se o estado é o objetivo
def is_goal(state, goal):
    return state == goal

# Função para encontrar os movimentos possíveis
def possible_moves(state):
    moves = []
    zero_index = state.index(0)
    """
    1 2 3
    4 5 6
    7 8 0
    """
    if zero_index not in [0, 1, 2]:  # Up
        moves.append(-3)
    if zero_index not in [0, 3, 6]:  # Left
        moves.append(-1)
    if zero_index not in [6, 7, 8]:  # Down
        moves.append(3)
    if zero_index not in [2, 5, 8]:  # Right
        moves.append(1)
    return moves

# Função para realizar um movimento
def move(state, direction):
    new_state = state[:]
    zero_index = new_state.index(0)
    new_state[zero_index], new_state[zero_index + direction] = new_state[zero_index + direction], new_state[zero_index]
    return new_state

# Algoritmo de busca gulosa
def greedy_search(start_state, goal_state):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((heuristic(start_state, goal_state), start_state))
    
    while not priority_queue.empty():
        current_state = priority_queue.get()[1]
        visited.add(tuple(current_state))
        
        if is_goal(current_state, goal_state):
            return current_state
        
        for move_direction in possible_moves(current_state):
            new_state = move(current_state, move_direction)
            if tuple(new_state) not in visited:
                priority_queue.put((heuristic(new_state, goal_state), new_state))
            #print(new_state)

        #print(visited)
    
    return None

# Estado inicial e estado objetivo 
start_state = [[2, 8, 3], [1, 6, 0], [4, 7, 5]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Executar a busca gulosa
result = greedy_search(start_state, goal_state)

if result:
    print("Solução encontrada:", result)
else:
    print("Não foi possível encontrar uma solução.")
