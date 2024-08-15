import pygame
import random
from enum import Enum
from collections import namedtuple
import sys

pygame.init()
font = pygame.font.Font('src/arial.ttf', 25)

STARTING_STONES = 4
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 800
HOLE_RADIUS = 36
GOAL_WIDTH = 200
GOAL_HEIGHT = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (165, 42, 42)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Hole:
    def __init__(self, stones = STARTING_STONES):
        self.stones = stones

class Goal:
    def __init__(self):
        self.stones = 0

class Board:
    def __init__(self, player1, player2):
        self.players = [player1,player2]
        self.holes = [
            [Hole() for _ in range(6)],  # Player 1's side
            [Hole() for _ in range(6)],  # Player 2's side
        ]
        self.goals = [Goal(),Goal()]
        self.cur_player_index = 0

    def move(self, hole_index):
        # move logic
        pass

    def is_game_over(self):
        # check if one side has no stones in any hole and implement logic
        pass

Point = namedtuple('Point', 'x, y')

# rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
GREEN = (0,200,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)     

BLOCK_SIZE = 20
SPEED = 20

class MancalaGame:
    def __init__(self, w=WINDOW_WIDTH, h=WINDOW_HEIGHT):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Mancala')
        self.clock = pygame.time.Clock()
        self.clicked_hole = None
        
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.board = Board(self.player1, self.player2)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            self.display_board()
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

    def display_board(self):
        self.display.fill(WHITE)
        
        # draw goal
        pygame.draw.rect(self.display, BROWN, (WINDOW_WIDTH/2-(GOAL_WIDTH/2), 0, GOAL_WIDTH, GOAL_HEIGHT))
        pygame.draw.rect(self.display, BROWN, (WINDOW_WIDTH/2-(GOAL_WIDTH/2), WINDOW_HEIGHT-GOAL_HEIGHT, GOAL_WIDTH, GOAL_HEIGHT))
        
        # draw holes
        for i in range(6):
            pygame.draw.circle(self.display, BROWN, ((2* HOLE_RADIUS) , GOAL_HEIGHT + 30 + i*120), HOLE_RADIUS)
            pygame.draw.circle(self.display, BROWN, (2*HOLE_RADIUS + HOLE_RADIUS + 220,  GOAL_HEIGHT + 30 + i*120), HOLE_RADIUS)
        
        # display stone counts
        for i in range(6):
            self.draw_text(str(self.board.holes[0][i].stones), 2* HOLE_RADIUS, GOAL_HEIGHT + 30 + i*120)
            self.draw_text(str(self.board.holes[1][5-i].stones), 2*HOLE_RADIUS + HOLE_RADIUS + 220, GOAL_HEIGHT + 30 + i*120)
        self.draw_text(f"Player {self.board.cur_player_index+1} Turn", WINDOW_WIDTH/2-(GOAL_WIDTH/2)+100, 200)
        self.draw_text(str(self.board.goals[1].stones), WINDOW_WIDTH/2-(GOAL_WIDTH/2)+20, 10)
        self.draw_text(str(self.board.goals[0].stones), WINDOW_WIDTH/2-(GOAL_WIDTH/2)+20, WINDOW_HEIGHT-GOAL_HEIGHT+20)

        if self.clicked_hole is not None:
            side, index = self.clicked_hole
            if side == 0:  # Left side
                center = (2 * HOLE_RADIUS, GOAL_HEIGHT + 30 + index * 120)
            else:  # Right side
                center = (2 * HOLE_RADIUS + HOLE_RADIUS + 220, GOAL_HEIGHT + 30 + (5-index) * 120)
            pygame.draw.circle(self.display, GREEN, center, HOLE_RADIUS + 2, 5) 

    def draw_text(self, text, x, y):
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(x, y))
        self.display.blit(text_surface, text_rect)

    def check_left(self, x, y):
        if HOLE_RADIUS <= x <= 3 * HOLE_RADIUS:
            for i in range(6):
                hole_center_y = GOAL_HEIGHT + 30 + i * 120
                if hole_center_y - HOLE_RADIUS <= y <= hole_center_y + HOLE_RADIUS:
                    return i
        return -1
                        
    def check_right(self, x, y):
        if 2 * HOLE_RADIUS + HOLE_RADIUS + 220 - HOLE_RADIUS <= x <= 2 * HOLE_RADIUS + HOLE_RADIUS + 220 + HOLE_RADIUS:
            for i in range(6):
                hole_center_y = GOAL_HEIGHT + 30 + i * 120
                if hole_center_y - HOLE_RADIUS <= y <= hole_center_y + HOLE_RADIUS:
                    return 5 - i
        return -1

    def handle_click(self, pos):
        x, y = pos
        print(f"Handled click at position: {pos}")

        left_hole = self.check_left(x, y)
        right_hole = self.check_right(x, y)

        # MESSAGE TO FUTURE: MAKE IT SO THAT IF I HAVE ENOUGH STONES, IT NEVER GOES INTO OPPONENTS STORE, ONLY MY OWN 

        if self.board.cur_player_index == 0:  # player 1's turn (right side)
            if right_hole != -1 and self.board.holes[1][right_hole].stones > 0:
                print(f"Player 1 chose: {right_hole}")
                self.clicked_hole = (1, right_hole)
                self.make_move(1, right_hole)
            elif left_hole != -1:
                print("It's not Player 2's turn")
            else:
                print("Invalid click")
        else:  # player 2's turn (left side)
            if left_hole != -1 and self.board.holes[0][left_hole].stones > 0:
                print(f"Player 2 chose: {left_hole}")
                self.clicked_hole = (0, left_hole)
                self.make_move(0, left_hole)
            elif right_hole != -1:
                print("It's not Player 1's turn")
            else:
                print("Invalid click")

    def make_move(self, side, hole_index):
        # move logic 
        print(f"Making move for {side} from hole {hole_index}")
        
        # if side == 1:  
        #     hole_index = 5 - hole_index
        
        numStones = self.board.holes[side][hole_index].stones
        self.board.holes[side][hole_index].stones = 0

        currentSide = side
        currentIndex = hole_index
        lastStone = None

        for _ in range(numStones):
            currentIndex += 1
        
            if currentIndex == 6:
                self.board.goals[side].stones += 1
                lastStone = 7
            else:
                if currentIndex > 5:
                    currentSide = 1 - currentSide  # switch sides
                    currentIndex = 0

                if currentSide == side and self.board.holes[currentSide][currentIndex].stones == 0 and numStones == 1:
                    # capture the stones from the opposite hole
                    oppositeIndex = 5 - currentIndex
                    capturedStones = self.board.holes[1 - currentSide][oppositeIndex].stones
                    self.board.goals[side].stones += capturedStones + 1  # add the captured stones plus the last stone
                    self.board.holes[1 - currentSide][oppositeIndex].stones = 0
                    print(f"Captured {capturedStones} stones from side {1 - currentSide}, hole {oppositeIndex}")
                else:
                    self.board.holes[currentSide][currentIndex].stones += 1
                    lastStone = currentIndex
        
        if lastStone == 7: # if stone ended on a goal then its still your turn
            self.board.cur_player_index = self.board.cur_player_index
        else:
            # switch turns after the move   
            self.board.cur_player_index = 1 - self.board.cur_player_index


if __name__ == '__main__':
    game = MancalaGame()
    game.run()