import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame
from pygame.locals import *
from board import Board
from pieces import Piece
from queue import Queue
from hold import Hold

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 30  
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)




class Game:

    DURATION = 120 * 1000

    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH + 200, SCREEN_HEIGHT))  # Extra width for UI
        self.clock = pygame.time.Clock()

        # Initialize game components
        self.board = Board(300 // GRID_SIZE, 600 // GRID_SIZE)
        self.queue = Queue(400)
        self.hold = Hold(200)

        self.can_hold = True
        self.current_tetromino = Piece(300 // GRID_SIZE // 2, 0, self.queue.get_piece(), 250)
        self.keys_held = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_DOWN: False}
        self.key_last_pressed = {key: 0 for key in self.keys_held}

        # Timers and settings
        self.lock_timer = 0
        self.lock_delay = 500  # Lock delay in milliseconds
        self.key_delay = 20
        self.key_repeat = 50



        # Track positions
        self.previous_position = (self.current_tetromino.x, self.current_tetromino.y)

        self.running = True

    def handle_events(self):
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in self.keys_held:
                    self.keys_held[event.key] = True
                if event.key == pygame.K_UP:
                    self.current_tetromino.rotate(1, self.board)
                elif event.key == pygame.K_z:
                    self.current_tetromino.rotate(-1, self.board)
                elif event.key == pygame.K_SPACE:
                    self.current_tetromino.hard_drop(self.board)
                elif event.key == pygame.K_a:
                    self.current_tetromino.rotate(2, self.board)
                elif event.key == pygame.K_c:
                    if( self.can_hold ):
                        self.current_tetromino = self.hold.hold(self.current_tetromino)
                        if self.current_tetromino is None:
                            self.current_tetromino = Piece(300 // GRID_SIZE // 2, 0, self.queue.get_piece(), 250)
                        self.can_hold = False
                    
            elif event.type == pygame.KEYUP:
                if event.key in self.keys_held:
                    self.keys_held[event.key] = False

    def handle_continuous_movement(self):
        """Handles movement for held keys."""
        current_time = pygame.time.get_ticks()
        for key, is_held in self.keys_held.items():
            if is_held:
                if current_time - self.key_last_pressed[key] > self.key_delay or self.key_last_pressed[key] == 0:
                    if key == pygame.K_LEFT:
                        self.current_tetromino.move(-1, 0, self.board)
                    elif key == pygame.K_RIGHT:
                        self.current_tetromino.move(1, 0, self.board)
                    elif key == pygame.K_DOWN:
                        self.current_tetromino.move(0, 1, self.board)
                    self.key_last_pressed[key] = current_time + self.key_repeat

    


    def handle_locking(self):
        current_position = (self.current_tetromino.x, self.current_tetromino.y)
        if current_position == self.previous_position:  # If position hasn't changed
         
            if self.lock_timer == 0:  # Start the lock timer
                self.lock_timer = pygame.time.get_ticks()

           
            elif ( not self.current_tetromino.can_move( self.board ) and pygame.time.get_ticks() - self.lock_timer >= self.lock_delay ):
                self.current_tetromino.stop()
                self.board.lock_piece(self.current_tetromino)
                self.board.clear_lines()
                self.can_hold = True
                self.current_tetromino = Piece(300 // GRID_SIZE // 2, 0, self.queue.get_piece(), 250)
                self.lock_timer = 0
        else:
            self.lock_timer = 0  # Reset the lock timer if the position changes

        self.previous_position = (self.current_tetromino.x, self.current_tetromino.y)

    def check_topout(self):
        pass
    
    
    def draw_game(self):
        self.screen.fill(BLACK)
        self.hold.draw(self.screen)
        self.queue.draw(self.screen)
        board_offset = 250
        self.board.draw(self.screen, board_offset)
        self.current_tetromino.draw(self.screen)
        self.board.draw_grid(self.screen, self.board.width, self.board.height, board_offset)
        self.board.draw_score(self.screen, 10, 200)
        pygame.display.flip()

    def run(self):

        start_time = pygame.time.get_ticks()
        
        while self.running:

            
            if( pygame.time.get_ticks() - start_time >= self.DURATION ):
                self.running = False

            print(pygame.time.get_ticks() - start_time)
            self.handle_events()
            self.handle_continuous_movement()
            self.handle_locking()
            self.board.gravity( self.current_tetromino )
            self.check_topout()
            self.draw_game()
            self.clock.tick(60)


        #some kinda stopping mechanism or restart mechanism i guess
        


        pygame.quit()


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()