def misplaced_tiles(state, goal_state):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal_state[i])
