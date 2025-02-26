
import random
from bot import Bot
from game.main import Game
#use genetic algorithms to find best weights for a tetris bot, given the attributes it's looking for

def main():


    pass

def mutation( bot ):
    rate = 0.05
    pass

def crossover( p1, p2 ):
    pass

def simulate_generation( bots ):
    vals = []
    for bot in bots:
        vals.append(fitness(bot), bot)
    vals = sorted(vals)
    return vals[:10]

def fitness( bot ):
    game = Game()
    return game.simulate_game( bot )



def generate_initial(pop_size, num_weights):
    return [ Bot(2 ,[ random.uniform(-1, 1) for _ in range(num_weights)] )  for _ in range(pop_size) ]
    

print(generate_initial( 10, 7))