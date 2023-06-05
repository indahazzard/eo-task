import random

def fitness_function(x):
    return 78 + 9*x - 2*x**2 + 3*x**3

def create_initial_population(population_size, min_value, max_value):
    population = []
    for _ in range(population_size):
        individual = random.uniform(min_value, max_value)
        population.append(individual)
    return population

def calculate_fitness(population):
    fitness_scores = []
    for individual in population:
        fitness_scores.append(fitness_function(individual))
    return fitness_scores

def select_parents(population, fitness_scores):
    parent1 = random.choices(population, weights=fitness_scores)[0]
    parent2 = random.choices(population, weights=fitness_scores)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    child = (parent1 + parent2) / 2
    return child

def mutate(child, mutation_rate):
    if random.random() < mutation_rate:
        child = random.uniform(min_value, max_value)
    return child

def genetic_algorithm(population_size, min_value, max_value, num_generations, mutation_rate):
    population = create_initial_population(population_size, min_value, max_value)
    
    for generation in range(num_generations):
        fitness_scores = calculate_fitness(population)
        
        max_fitness = max(fitness_scores)
        max_index = fitness_scores.index(max_fitness)
        best_individual = population[max_index]
        
        print(f"generation {generation}: best individual = {best_individual}, max fitness = {max_fitness}")
        
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = select_parents(population, fitness_scores)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        
        population = new_population
    
    return best_individual

population_size = 100
min_value = -12
max_value = 51
num_generations = 50
mutation_rate = 0.01

best_solution = genetic_algorithm(population_size, min_value, max_value, num_generations, mutation_rate)
print("max:", fitness_function(best_solution))
