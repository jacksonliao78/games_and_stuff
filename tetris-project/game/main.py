import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame
from pygame.locals import *
from game.board import Board
from game.pieces import Piece
from game.queue import Queue
from game.hold import Hold
from abot.bot import Bot

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 630
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
        self.board = Board(300 // GRID_SIZE, 630 // GRID_SIZE)
        self.queue = Queue(400)
        self.hold = Hold(200)
        self.score = 0

        self.can_hold = True
        self.current_tetromino = self.spawn_tetromino()
        self.keys_held = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_DOWN: False}
        self.key_last_pressed = {key: 0 for key in self.keys_held}

        # Timers and settings
        self.lock_timer = 0
        self.lock_delay = 500  # Lock delay in milliseconds
        self.key_delay = 20
        self.key_repeat = 50



        # Track positions
        self.rotation_count = 0
        self.previous_position = (self.current_tetromino.x, self.current_tetromino.y, self.current_tetromino.rotation)

        self.running = True

    def spawn_tetromino(self):
        return Piece( 300 // GRID_SIZE // 2 - 2, 0, self.queue.get_piece(), 250)

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
                            self.current_tetromino = self.spawn_tetromino()
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



        current_position = (self.current_tetromino.x, self.current_tetromino.y, self.current_tetromino.rotation)
        if current_position == self.previous_position:  # If position hasn't changed
         
            if self.lock_timer == 0:  # Start the lock timer
                self.lock_timer = pygame.time.get_ticks()

           
            elif ( not self.current_tetromino.can_move( self.board ) and pygame.time.get_ticks() - self.lock_timer >= self.lock_delay ):
                self.current_tetromino.stop()
                self.board.lock_piece(self.current_tetromino)
                self.board.clear_lines()
                self.score = self.board.get_score()
                self.can_hold = True
                self.current_tetromino = self.spawn_tetromino()
                self.lock_timer = 0
        else:
            self.lock_timer = 0  # Reset the lock timer if the position changes

        self.previous_position = (self.current_tetromino.x, self.current_tetromino.y, self.current_tetromino.rotation)

    def check_topout(self):
        return not self.board.is_valid_position(self.current_tetromino) and not self.current_tetromino.can_move( self.board ) and self.current_tetromino.y <=  1
    
    
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

            #print(pygame.time.get_ticks() - start_time)
            self.handle_events()
            self.handle_continuous_movement()
            self.handle_locking()
            self.board.gravity( self.current_tetromino )
            if( self.check_topout() ):
                self.running = False
            self.draw_game()
            self.clock.tick(60)


        #some kinda stopping mechanism or restart mechanism i guess
        


        pygame.quit()

    #to visualize bot playing in real time
    def run_bot(self, bot):

        speed = Game.DURATION / ( bot.speed_cap * 100 )

        print(speed)

        start_time = pygame.time.get_ticks()
        piece_time = pygame.time.get_ticks()

        while self.running:

            self.handle_events()
           
            current_time = pygame.time.get_ticks()

            if( current_time - start_time >= self.DURATION ):
                self.running = False

            if( current_time - piece_time >= speed ):
                bot.make_move( self )
                bot.print_board( self.board )
                print("move made")
                self.board.clear_lines()
                self.score = self.board.get_score()
                self.current_tetromino = self.spawn_tetromino()
                if( self.check_topout() ):
                    self.running = False
                piece_time = pygame.time.get_ticks()
            self.draw_game()
            self.clock.tick(60)
            #print("skibii")

                #draw things probably


    #for ai purposes
    def simulate_game(self, bot):
        for _ in range( int(bot.speed_cap * Game.DURATION / 1000) ):
            bot.make_move( self )
            self.board.clear_lines()
            self.score = self.board.get_score()
            self.current_tetromino = self.spawn_tetromino()
            if( self.check_topout() ):
                return self.score
        return self.score

        #return score here or smth

    


def main():
    game = Game()
    
    weights = [ -0.6460856708097908, -0.7438680313063725, -0.16241082335092175, -0.3894047332115014, 1.034599119943385, -0.0706335058108325, 0, 0, 0 ] #  -0.0706335058108325  -0.46617836785448064    0.6233213406339039
    bot = Bot(2, weights)
    #game.run()
    game.run_bot(bot)


if __name__ == "__main__":
    main()