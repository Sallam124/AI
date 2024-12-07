def linear_conflict(state, goal_state):
    conflict = 0
    
    for i in range(3):
        row = [state[i*3 + j] for j in range(3)]
        goal_row = [goal_state[i*3 + j] for j in range(3)]
        
        # Check for conflicts within each row
        for j in range(2):
            for k in range(j+1, 3):
                if (row[j] != 0 and row[k] != 0 and 
                    goal_state.index(row[j]) > goal_state.index(row[k])):
                    conflict += 2  # Each conflict adds a penalty of 2

    return conflict
