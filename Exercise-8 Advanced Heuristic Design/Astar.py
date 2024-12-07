import heapq
import time
from Manhattan import manhattan
from Misplaced import misplaced_tiles
from Linear import linear_conflict

class PuzzleState:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Cost to reach this state (number of moves)
        self.h = h  # Heuristic estimate
        self.f = g + h  # Total cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f

# A* Search Algorithm
def a_star(start_state, goal_state, heuristic_fn):
    open_list = []
    closed_list = set()
    nodes_expanded = 0  # Initialize the counter for expanded nodes
    
    # Initialize with the start state
    start = PuzzleState(start_state, None, 0, heuristic_fn(start_state, goal_state))
    heapq.heappush(open_list, start)
    
    while open_list:
        current = heapq.heappop(open_list)
        
        # Increment the nodes expanded counter
        nodes_expanded += 1
        
        # If we reach the goal state
        if current.state == goal_state:
            path = []
            while current:
                path.append(current.state)
                current = current.parent
            return path[::-1], nodes_expanded  # Return reversed path and the number of nodes expanded
        
        closed_list.add(tuple(current.state))
        
        # Expand neighbors (implementing the actual puzzle moves)
        for neighbor in get_neighbors(current.state):
            if tuple(neighbor) in closed_list:
                continue
            g = current.g + 1
            h = heuristic_fn(neighbor, goal_state)
            neighbor_state = PuzzleState(neighbor, current, g, h)
            heapq.heappush(open_list, neighbor_state)

    return None, nodes_expanded  

# Define a helper function to get neighbors (state transitions)
def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    zero_row, zero_col = zero_index // 3, zero_index % 3
    
    # List possible moves (up, down, left, right)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (row_change, col_change)
    
    for move in moves:
        new_row = zero_row + move[0]
        new_col = zero_col + move[1]
        
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = state[:]
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append(new_state)
    
    return neighbors

# Function to print puzzle in a 3x3 grid format
def print_puzzle(state):
    for i in range(0, len(state), 3):
        print(state[i:i+3])
    print()  # for separation between puzzles

# Goal State
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# List of puzzles to test
puzzles = [
    ([0, 2, 3, 4, 5, 6, 7, 8, 1], "Puzzle 1"),  
    ([1, 2, 3, 4, 5, 6, 0, 7, 8], "Puzzle 2"),
    ([1, 0, 3, 4, 2, 5, 7, 8, 6], "Puzzle 3"),
    ([1, 2, 3, 4, 5, 6, 8, 7, 0], "Puzzle 4"),
    ([1, 3, 2, 5, 4, 6, 7, 8, 0], "Puzzle 5")  
]
# Iterate over each puzzle
for start_state, puzzle_name in puzzles:
    print(f"\n{puzzle_name}...")
    
    # Print the initial state of the puzzle
    print("Initial State:")
    print_puzzle(start_state)
    
    start_time = time.time()
    
    # path = a_star(start_state, goal_state, manhattan)
    # path = a_star(start_state, goal_state, misplaced_tiles)
    path, nodes_expanded = a_star(start_state, goal_state, linear_conflict)
    
    end_time = time.time()
    
    if path:
        print("Solution Path:")
        for step in path:
            print_puzzle(step)
    else:
        print("No solution found.")
    
    print(f"Execution Time: {end_time - start_time:.4f} seconds")
    print(f"Nodes Expanded: {nodes_expanded}")
