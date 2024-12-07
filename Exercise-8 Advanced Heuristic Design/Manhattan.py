def manhattan(state, goal_state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            current_pos = (i // 3, i % 3)
            goal_pos = (goal_state.index(state[i]) // 3, goal_state.index(state[i]) % 3)
            distance += abs(current_pos[0] - goal_pos[0]) + abs(current_pos[1] - goal_pos[1])
    return distance