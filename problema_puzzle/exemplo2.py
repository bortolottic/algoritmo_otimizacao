from queue import PriorityQueue

class PuzzleState:
    def __init__(self, puzzle, parent=None, move=0):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.goal = [1, 2, 3, 4, 5, 6, 7, 8]

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __lt__(self, other):
        return False

    def __str__(self):
        return '\n'.join([str(self.puzzle[i:i+3]) for i in range(0, 9, 3)])

    def generate_children(self):
        children = []
        zero_index = self.puzzle.index(0)
        moves = [-3, 3, -1, 1]
        for move in moves:
            new_index = zero_index + move
            if 0 <= new_index < 9 and (zero_index % 3 != 0 or move != 1) and (zero_index % 3 != 2 or move != -1):
                new_puzzle = self.puzzle[:]
                new_puzzle[zero_index], new_puzzle[new_index] = new_puzzle[new_index], new_puzzle[zero_index]
                children.append(PuzzleState(new_puzzle, self, self.move + 1))
        return children

    def heuristic(self):
        return sum([1 if self.puzzle[i] != self.goal[i] else 0 for i in range(8)])

    def solve(self):
        frontier = PriorityQueue()
        frontier.put((0, self))
        visited = set()
        while not frontier.empty():
            _, current = frontier.get()
            if current.puzzle == self.goal:
                path = []
                while current.parent:
                    path.append(current)
                    current = current.parent
                path.append(current)
                path.reverse()
                return path
            visited.add(current)
            for child in current.generate_children():
                if child not in visited:
                    priority = child.move + child.heuristic()
                    frontier.put((priority, child))
        return None

def main():
    initial_state = PuzzleState([2, 8, 3, 1, 6, 0, 4, 7, 5])
    solution = initial_state.solve()
    if solution:
        print("Solução encontrada em", len(solution) - 1, "passos:")
        for state in solution:
            print(state)
    else:
        print("Não foi possível encontrar uma solução.")

if __name__ == "__main__":
    main()
