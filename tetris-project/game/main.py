import sys
import os
import csv

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
        self.key_press_time = {key: 0 for key in self.keys_held}
        self.key_repeat_time = {key: 0 for key in self.keys_held}
        
        
        self.das_delay = 133  # initial delay in ms before auto-repeat kicks in
        self.arr_delay = 10   # delay between repeated movements in ms

        # Timers and settings
        self.lock_timer = 0
        self.lock_delay = 500  # Lock delay in milliseconds

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
                    self.key_press_time[event.key] = pygame.time.get_ticks()
                    if event.key == pygame.K_LEFT:
                        self.current_tetromino.move(-1, 0, self.board)
                    elif event.key == pygame.K_RIGHT:
                        self.current_tetromino.move(1, 0, self.board)
                    elif event.key == pygame.K_DOWN:
                        self.current_tetromino.move(0, 1, self.board)
                
                if event.key == pygame.K_UP:
                    self.current_tetromino.rotate(1, self.board)
                elif event.key == pygame.K_z:
                    self.current_tetromino.rotate(-1, self.board)
                elif event.key == pygame.K_SPACE:
                    self.current_tetromino.hard_drop(self.board)
                elif event.key == pygame.K_a:
                    self.current_tetromino.rotate(2, self.board)
                elif event.key == pygame.K_c:
                    if(self.can_hold):
                        self.current_tetromino = self.hold.hold(self.current_tetromino)
                        if self.current_tetromino is None:
                            self.current_tetromino = self.spawn_tetromino()
                        self.can_hold = False
                    
            elif event.type == pygame.KEYUP:
                if event.key in self.keys_held:
                    self.keys_held[event.key] = False
                    # Reset timers when key is released
                    self.key_press_time[event.key] = 0
                    self.key_repeat_time[event.key] = 0

    def handle_continuous_movement(self):
        """Handles movement for held keys using DAS and ARR."""
        current_time = pygame.time.get_ticks()
        
        for key, is_held in self.keys_held.items():
            if is_held and self.key_press_time[key] > 0:
                time_held = current_time - self.key_press_time[key]
                
                if time_held >= self.das_delay:
                    if current_time >= self.key_repeat_time[key]:
                        if key == pygame.K_LEFT:
                            self.current_tetromino.move(-1, 0, self.board)
                        elif key == pygame.K_RIGHT:
                            self.current_tetromino.move(1, 0, self.board)
                        elif key == pygame.K_DOWN:
                            self.current_tetromino.move(0, 1, self.board)
                        
                        self.key_repeat_time[key] = current_time + self.arr_delay

    def handle_locking(self):

        current_position = (self.current_tetromino.x, self.current_tetromino.y, self.current_tetromino.rotation)
        if current_position == self.previous_position:  # If position hasn't changed
         
            if self.lock_timer == 0:  # Start the lock timer
                self.lock_timer = pygame.time.get_ticks()

           
            elif ( not self.current_tetromino.is_moving(self.board) or not self.current_tetromino.can_move( self.board ) and pygame.time.get_ticks() - self.lock_timer >= self.lock_delay ):
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
    
    def start_screen(self):
        font = pygame.font.Font(None, 36)
        title_font = pygame.font.Font(None, 48)

        start_button = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 + 50, 150, 50)

        running = True
        while running:
            self.screen.fill(BLACK)
        
            title_text = title_font.render("TETRIS", True, WHITE)
            self.screen.blit(title_text, (SCREEN_WIDTH // 2 - 50, 50))
        
            scores = self.get_scores(5)
            y_offset = 120
        
            for i, score_data in enumerate(scores):
                text = font.render(f"{i+1}. {score_data['Name']} - {score_data['Score']}", True, WHITE)
                self.screen.blit(text, (SCREEN_WIDTH // 2 - 100, y_offset))
                y_offset += 30
        
            pygame.draw.rect(self.screen, BLUE, start_button)
            start_text = font.render("Start", True, WHITE)
            self.screen.blit(start_text, (start_button.x + 45, start_button.y + 15))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):
                        return  

    
    def draw_game(self):
        self.screen.fill(BLACK)
        self.hold.draw(self.screen)
        self.queue.draw(self.screen)
        board_offset = 250
        self.board.draw(self.screen, board_offset)
        self.current_tetromino.get_lowest(self.board)
        self.current_tetromino.draw(self.screen)
        self.board.draw_grid(self.screen, self.board.width, self.board.height, board_offset)
        self.board.draw_score(self.screen, 10, 200)
        pygame.display.flip()


    def end_screen(self):
    
        font = pygame.font.Font(None, 36)
        input_box = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30, 200, 40)
        color_inactive = pygame.Color('lightskyblue3')
        color = color_inactive
        text = ''
    
        restart_button = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50, 150, 50)
        quit_button = pygame.Rect(SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2 + 120, 150, 50)
    
        running = True
        while running:
            self.screen.fill(BLACK)
        
            game_over_text = font.render("Game Over!", True, WHITE)
            self.screen.blit(game_over_text, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        
            name_text = font.render("Enter Your Name:", True, WHITE)
            self.screen.blit(name_text, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
        
            pygame.draw.rect(self.screen, color, input_box, 2)
            txt_surface = font.render(text, True, WHITE)
            self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        
        # Draw buttons
            pygame.draw.rect(self.screen, BLUE, restart_button)
            pygame.draw.rect(self.screen, RED, quit_button)
        
            restart_text = font.render("Restart", True, WHITE)
            quit_text = font.render("Quit", True, WHITE)
            self.screen.blit(restart_text, (restart_button.x + 30, restart_button.y + 15))
            self.screen.blit(quit_text, (quit_button.x + 45, quit_button.y + 15))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.write_score(self.board.get_score(), True, "None")
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.collidepoint(event.pos):
                        return text  # Return the name and restart
                    elif quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return text  # Pressing Enter also restarts
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode 

    def restart_game(self):
        self.__init__()  # Reinitialize the game
        self.run()

    def write_score(self, score, isHuman, name="None", filename="scores.csv"):
        exists = os.path.isfile(filename)

        with open(filename, mode='a', newline="") as f:
            writer = csv.writer(f)
            if not exists:
                writer.writerow(["Game ID", "Human/Bot", "Name", "Score"])
            id = sum( 1 for _ in open(filename) )
            writer.writerow([ id, "Human" if isHuman else "Bot", name, score])
        
        

    def get_scores(self, num, filename="scores.csv"):
        exists = os.path.isfile(filename)
        scores = []

        if not exists:
            return scores
        with open(filename, mode='r') as f:
            reader = csv.DictReader(f)
            for line in reader:
                scores.append( {"Game ID": int(line["Game ID"]), "Human/Bot": line["Human/Bot"], "Name": line["Name"], "Score": int(line["Score"])})
        scores.sort( key=lambda x: x["Score"], reverse=True)
        return scores[:num]
        
        

    def run(self):

        #starting screen or button or something?? dunno?? display high sores?? dunno
        self.start_screen()
        start_time = pygame.time.get_ticks()
        
        while self.running:

            
            if( pygame.time.get_ticks() - start_time >= self.DURATION ):
                self.running = False
                name = self.end_screen()
                self.write_score(self.board.get_score(), True, name)  # Save name
                self.restart_game()

            #print(pygame.time.get_ticks() - start_time)
            self.handle_events()
            self.handle_continuous_movement()
            self.handle_locking()
            self.board.gravity( self.current_tetromino )
            if self.check_topout():
                self.running = False
                name = self.end_screen()
                self.write_score(self.board.get_score(), True, name)  # Save name
                self.restart_game()
            self.draw_game()
            self.clock.tick(60)


        #some kinda stopping mechanism or restart mechanism i guess
        self.write_score( self.board.get_score(), True )


        #restart mechanism here 

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
        print(self.board.pps())
        self.write_score( self.board.get_score(), False)
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
    
    weights = [-0.7156849084207725, -0.46410597390900077, -0.8182796982481585, -0.25240742804407745, 0.4105997617287197, 0.31782852240290693, -0.3220757737205828, 0.4807079329940822]
    bot = Bot(10, weights)
    game.run()
    #game.run_bot(bot)


if __name__ == "__main__":
    main()