# mancalaDeepLearning
Repo for my mancala deep learning project - MAYBE DO 4 VERSION LATER

## Planning (Model):
## Code:
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
1: [1,0,0,0,0,0] (YOUR GOAL HERE)
2: [0,1,0,0,0,0]
3: [0,0,1,0,0,0]
4: [0,0,0,1,0,0]
5: [0,0,0,0,1,0]
6: [0,0,0,0,0,1]

State:
YOUR SIDE: [4,4,4,4,4,4,0] (Normalize by dividing by 12*NUM_START_STONES)
OPPONENT SIDE: [4,4,4,4,4,4,0]

### Game - Pygame - Mancala
### Model - Deep Q Learning (PyTorch)