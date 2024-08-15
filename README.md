# mancalaDeepLearning
Repo for my mancala deep learning project - MAYBE DO 4 VERSION LATER

## Planning (Model):
### Agent 
* Game
* Model
Training:
1. state = get_state(game)
2. action = get_move(state)
3. reward, game_over, score = game.play_step(action)
4. new_state = get_state(game)
5. remember
6. model.train()

Rewards:
* Get stone in - +10
* Eat opponent stones - +10 (per stone)
* Opponent eat your stones -10 (per stone)
* win - +200
* lose - -200

Actions:
- 1: [1,0,0,0,0,0] (YOUR GOAL HERE)
- 2: [0,1,0,0,0,0]
- 3: [0,0,1,0,0,0]
- 4: [0,0,0,1,0,0]
- 5: [0,0,0,0,1,0]
- 6: [0,0,0,0,0,1]
- 6 POSSIBLE ACTIONS

State:
- YOUR SIDE: [4,4,4,4,4,4,0] (Normalize by dividing by 12*NUM_START_STONES)
- OPPONENT SIDE: [4,4,4,4,4,4,0] -> 14 INPUTS

### Game - Pygame - Mancala
Get more stones by the end than your opponent - (goal target: 12*NUM_START_STONES/2 + 1)

### Model - Deep Q Learning (PyTorch)
0. Initialize Q value (=init model)
1. Choose action (model.predict(state))
2. Perform action
3. Meausre reward
4. Update Q value, and train model (Bellman equation)
5. Repeat 1-4

Loss: (Qnew-Q)^2 - MSE
