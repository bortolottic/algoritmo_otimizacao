from queue import PriorityQueue

def generate_children(puzzle):
    children = []
    zero_index = puzzle.index(0)
    moves = [-3, 3, -1, 1]
    for move in moves:
        new_index = zero_index + move
        if 0 <= new_index < 9 and (zero_index % 3 != 0 or move != 1) and (zero_index % 3 != 2 or move != -1):
            new_puzzle = puzzle[:]
            new_puzzle[zero_index], new_puzzle[new_index] = new_puzzle[new_index], new_puzzle[zero_index]
            children.append(new_puzzle)
    return children

def heuristic(puzzle):
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    return sum([1 if puzzle[i] != goal[i] else 0 for i in range(8)])

def solve(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    visited = set()
    while not frontier.empty():
        current, move = frontier.get()
        if current == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            path = []
            while current[1]:
                path.append(current[0])
                current = current[1]
            path.append(current[0])
            path.reverse()
            return path
        visited.add(tuple(current))
        for child in generate_children(current):
            if tuple(child) not in visited:
                priority = move + heuristic(child)
                frontier.put((priority, (child, current, move + 1)))
    return None

def main():
    initial_state = [2, 8, 3, 1, 6, 0, 4, 7, 5]
    solution = solve(initial_state)
    if solution:
        print("Solução encontrada em", len(solution) - 1, "passos:")
        for state in solution:
            print('\n'.join([str(state[i:i+3]) for i in range(0, 9, 3)]))
            print()
    else:
        print("Não foi possível encontrar uma solução.")

if __name__ == "__main__":
    main()
