import matplotlib.pyplot as plt
import numpy as np
import heapq
import matplotlib.animation as animation

def heuristic(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def a_star_solve_maze(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {start: None}
    g_cost = {start: 0}  # Actual cost from start to current node
    f_cost = {start: heuristic(start, goal)}  # Estimated total cost (g_cost + heuristic)
    
    visited_cells = np.zeros((rows, cols), dtype=np.float32)
    path = []
    step_count = 0

    while open_list:
        _, current_cell = heapq.heappop(open_list)

        if current_cell == goal:
            # Reconstruct the path from the goal to the start
            while current_cell is not None:
                path.append(current_cell)
                current_cell = came_from[current_cell]
            path.reverse()  # Reverse the path to go from start to goal
            step_count = len(path) - 1
            break

        x, y = current_cell
        visited_cells[x, y] = 0.3  # Mark as visited

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (x + dx, y + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and (grid[neighbor[0]][neighbor[1]] == 0 or grid[neighbor[0]][neighbor[1]] == 'E'):
                tentative_g_cost = g_cost[current_cell] + 1
                if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                    came_from[neighbor] = current_cell
                    g_cost[neighbor] = tentative_g_cost
                    f_cost[neighbor] = tentative_g_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_cost[neighbor], neighbor))
                    visited_cells[neighbor[0], neighbor[1]] = 0.5  # Mark neighbor as visited

    return path, visited_cells, step_count 

def visualize_a_star(grid, path, visited_cells):
    visual_grid = np.array([[0 if cell == 'S' or cell == 'E' else cell for cell in row] for row in grid], dtype=np.float32)
    fig, ax = plt.subplots()
    im = ax.imshow(visual_grid, cmap='Blues', origin='upper', interpolation='nearest')

    def update(frame):
        if frame < len(path):
            x, y = path[frame]
            visual_grid[x, y] = 0.7  # Highlight the path
        
        # Show visited cells
        for i in range(len(visited_cells)):
            for j in range(len(visited_cells[i])):
                if visited_cells[i][j] == 0.3:  # Mark cell as visited
                    visual_grid[i, j] = 0.5  # Show visited cells with different color

        im.set_array(visual_grid)
        return [im]

    ani = animation.FuncAnimation(fig, update, frames=len(path), blit=True, repeat=False, interval=500)
    plt.title("A* Maze Solving Visualization")
    plt.xticks(range(len(grid[0])))
    plt.yticks(range(len(grid)))
    plt.grid(color='black', linewidth=0.5)
    plt.show()

if __name__ == "__main__":
    grid = [
        ['S', 1, 1, 1, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 'E']
    ]

    start = (0, 0)
    goal = (9, 9)

    path, visited_cells, moves = a_star_solve_maze(grid, start, goal)
    print("Number of Steps required to reach the goal: ", moves)
    visualize_a_star(grid, path, visited_cells)
