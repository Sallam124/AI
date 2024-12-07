import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import matplotlib.animation as animation

def bfs(matrix, start_node, end_node):
    solution = []
    costs = 0

    def get_neighbors(node):
        row, col = node
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] != 'B':  
                neighbors.append((r, c))
        return neighbors

    frontier = deque([start_node])
    visited = set([start_node])
    parent_map = {start_node: None} 
    order_of_visits = [start_node]

    while frontier:
        selected_node = frontier.popleft()

        if selected_node == end_node:
            node = selected_node
            while node is not None:
                solution.append(node)
                node = parent_map[node]
            solution.reverse()
            break

        for neighbor in get_neighbors(selected_node):
            if neighbor not in visited:
                visited.add(neighbor)
                frontier.append(neighbor)
                parent_map[neighbor] = selected_node
                order_of_visits.append(neighbor)

        costs += 1

    return solution, visited, costs, order_of_visits

def visualize_bfs(matrix, path, visited, order_of_visits):
    visual_grid = np.array([[0 if cell == 'S' or cell == 'E' else 1 if cell == 'B' else 0 for cell in row] for row in matrix], dtype=np.float32)
    
    fig, ax = plt.subplots()
    im = ax.imshow(visual_grid, cmap='Blues', origin='upper', interpolation='nearest')

    def update(frame):
        if frame >= len(order_of_visits):
            return [im]  

        x, y = order_of_visits[frame]
        visual_grid[x, y] = 0.5  # Color all explored nodes with the same color

        if (x, y) in path:
            visual_grid[x, y] = 0.7  # Highlight path nodes with a different color

        im.set_array(visual_grid)
        return [im]

    frames_to_show = len(order_of_visits)

    # Make sure to show grid lines by adjusting settings
    ax.set_xticks(np.arange(-0.5, len(matrix[0]), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(matrix), 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=1)

    ani = animation.FuncAnimation(fig, update, frames=frames_to_show, blit=True, repeat=False, interval=500)
    plt.title("BFS Maze Solving Visualization")
    plt.xticks(range(len(matrix[0])))
    plt.yticks(range(len(matrix)))
    plt.grid(color='black', linewidth=0.5)
    plt.show()

if __name__ == "__main__":
    matrix = [
        ['S', 'B', 'B', 'B', 'B', 'A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'B', 'H', 'B', 'I', 'B', 'J', 'B', 'K'],
        ['B', 'L', 'B', 'M', 'B', 'N', 'O', 'P', 'B', 'Q'],
        ['R', 'S', 'T', 'U', 'B', 'B', 'B', 'B', 'B', 'V'],
        ['W', 'B', 'B', 'B', 'B', 'X', 'Y', 'Z', 'B', 'AA'],
        ['BB', 'CC', 'DD', 'EE', 'DD', 'EE', 'B', 'FF', 'B', 'GG'],
        ['B', 'HH', 'B', 'B', 'B', 'B', 'B', 'II', 'B', 'JJ'],
        ['KK', 'LL', 'MM', 'NN', 'OO', 'PP', 'QQ', 'RR', 'B', 'SS'],
        ['TT', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'UU'],
        ['WW', 'XX', 'YY', 'ZZ', 'AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'E']
    ]
    
    start = (0, 0)
    end = (9, 9)

    path, visited, moves, order_of_visits = bfs(matrix, start, end)

    print("Number of moves required to reach the goal:", moves)

    visualize_bfs(matrix, path, visited, order_of_visits)
