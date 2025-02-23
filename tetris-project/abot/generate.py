
import random
from bot import Bot
#use genetic algorithms to find best weights for a tetris bot, given the attributes it's looking for

def main():


    pass


def fitness( bot ):
    pass


def generate_initial(pop_size, num_weights):
    return [ Bot(2 ,[ random.uniform(-1, 1) for _ in range(num_weights)] )  for _ in range(pop_size) ]
    

print(generate_initial( 10, 6))