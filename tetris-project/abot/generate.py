
import random
from bot import Bot
from game.main import Game


""" Function that returns the top best 5 bot weights after a certain number of generations """
def main( generations ):
    gen = generate_initial( 100, 7 )

    count = 0
    for _ in range(generations):
        print(count)
        gen = get_generation( gen )
        count += 1

    for bot in gen[:5]:
        print( bot.weights )    
    
""" Creates a new generation given the top 10 individuals from the current one """
def get_generation( gen ):
    newgen = [ indiv for indiv in simulate_generation( gen )]

    for _ in range( 90 ):
        p1, p2 = random.randint(0, len(newgen) - 1), random.randint(0, len(newgen) - 1)
        newgen.append( mutation(crossover( newgen[p1], newgen[p2]) ) )

    return newgen
    
""" Changes weights slightly, simulating mutation (small chance) """
def mutation( bot ):
    rate = 0.05
    
    for key in bot.weights:
        if random.uniform(0, 1) <= rate:
            bot.weights[key] += random.uniform( -0.1, 0.1 )

    return bot

""" Creates a new bot from two parents, by averging their weights """
def crossover( p1, p2 ):
    weights = []

    for key in p1.weights:
        weights.append( ( p1.weights[key] + p2.weights[key] ) / 2 ) 

    return Bot(2, weights)

""" Simulates a generation of bots, returning the top ten """
def simulate_generation( bots ):
    vals = []
    for bot in bots:
        vals.append( ( fitness(bot), bot ) )
    vals = sorted(vals, key=lambda x: x[0], reverse=True)
    
    return [val[1] for val in vals[:10]]
    
""" Simulates a two minute blitz game for a bot, returning its score """
def fitness( bot ):
    game = Game()
    return game.simulate_game( bot )

""" Randomly generates the initial population """
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
    main( 10 )