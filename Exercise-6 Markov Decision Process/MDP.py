grid_size = 4
states = [(x, y) for x in range(grid_size) for y in range(grid_size)]
seen = []

def get_next_state(state, action):
    x, y = state
    if action == 'Up' and y < 3:
        y += 1
    elif action == 'Down' and y > 0: 
        y -= 1
    elif action == 'Left' and x > 0: 
        x -= 1
    elif action == 'Right' and x < 3: 
        x += 1
    return (x, y)

def reward(state,goal_state):
    if state == goal_state:  
        return 10
    else:
        return -1

start_state = (0, 0)
goal_state = (3, 2)
steps = 20 

state = start_state
current_reward = 0
total_reward = 0

print("Robot's Path:")

seen.append(start_state)


def move_to_goal(state, goal_state):
    x, y = state
    goal_x, goal_y = goal_state

    if x < goal_x:
        return (x + 1, y)
    elif x > goal_x:
        return (x - 1, y)

    if y < goal_y:
        return (x, y + 1)
    elif y > goal_y:
        return (x, y - 1)

    return state  



for i in range(steps):
    if state == goal_state:
        print("Reached Goal at " + str(state) + "!")
        break

    next_state = move_to_goal(state, goal_state)

    seen.append(next_state) 

    total_reward += reward(next_state,goal_state)

    print(f"State: {state} -> Next State: {next_state} -> Reward: {reward(next_state,goal_state)}")
    
    state = next_state

print("\nTotal Reward: " + str(total_reward))
