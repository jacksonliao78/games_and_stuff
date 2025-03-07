
import random
from bot import Bot
from game.main import Game
#use genetic algorithms to find best weights for a tetris bot, given the attributes it's looking for

def main( generations ):
    print('hi')
    gen = generate_initial( 100, 7 )

    for _ in range(generations):
        gen = get_generation( gen )

    for bot in simulate_generation(gen)[:2]:
        print(bot.weights)
    
    


def get_generation( gen ):
    newgen = [ indiv for indiv in simulate_generation( gen )]

    for _ in range( 90 ):
        p1, p2 = random.randint(0, len(newgen) - 1), random.randint(0, len(newgen) - 1)
        newgen.append( mutation(crossover( newgen[p1], newgen[p2]) ) )

    return newgen
    

def mutation( bot ):
    rate = 0.05
    
    for key in bot.weights:
        if random.uniform(0, 1) <= rate:
            bot.weights[key] += random.uniform( -0.1, 0.1 )

    return bot

def crossover( p1, p2 ):
    weights = []


    for key in p1.weights:
        weights.append( ( p1.weights[key] + p2.weights[key] ) / 2 ) 

    return Bot(2, weights)

def simulate_generation( bots ):
    vals = []
    for bot in bots:
        vals.append( ( fitness(bot), bot ) )
    vals = sorted(vals, key=lambda x: x[0], reverse=True)
    
    return [val[1] for val in vals[:10]]
    

def fitness( bot ):
    game = Game()
    return game.simulate_game( bot )



def generate_initial(pop_size, num_weights):
    population = []
    
    weight_ranges = [
        (-1.0, -0.2), 
        (-1.0, -0.2), 
        (-1.0, -0.2),   
        (-0.5, -0.1), 
        (0.2, 1.0),    
        (0.1, 0.5),    
        (-0.5, -0.1), 
        (0.2, 0.8)     
    ]
    
    for _ in range(pop_size):
        weights = [random.uniform(min_val, max_val) for min_val, max_val in weight_ranges]
        population.append(Bot(2, weights))
    
    return population
    

if __name__ == "__main__":
    print("b")
    main( 1000 )