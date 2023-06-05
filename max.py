import random

# Определение функции, которую нужно максимизировать
def fitness_function(x):
    return 78 + 9*x - 2*x**2 + 3*x**3

# Создание начальной популяции случайных решений
def create_initial_population(population_size, min_value, max_value):
    population = []
    for _ in range(population_size):
        individual = random.uniform(min_value, max_value)
        population.append(individual)
    return population

# Оценка приспособленности каждого решения в популяции
def calculate_fitness(population):
    fitness_scores = []
    for individual in population:
        fitness_scores.append(fitness_function(individual))
    return fitness_scores

# Выбор родителей для скрещивания (пропорционально приспособленности)
def select_parents(population, fitness_scores):
    # Выбираем двух родителей, используя рулеточный выбор
    parent1 = random.choices(population, weights=fitness_scores)[0]
    parent2 = random.choices(population, weights=fitness_scores)[0]
    return parent1, parent2

# Скрещивание двух родителей для создания потомка
def crossover(parent1, parent2):
    # Одноточечное скрещивание
    child = (parent1 + parent2) / 2
    return child

# Мутация потомка
def mutate(child, mutation_rate):
    if random.random() < mutation_rate:
        child = random.uniform(min_value, max_value)
    return child

# Генетический алгоритм для поиска максимума функции
def genetic_algorithm(population_size, min_value, max_value, num_generations, mutation_rate):
    population = create_initial_population(population_size, min_value, max_value)
    
    for generation in range(num_generations):
        fitness_scores = calculate_fitness(population)
        
        # Находим максимальное значение приспособленности
        max_fitness = max(fitness_scores)
        max_index = fitness_scores.index(max_fitness)
        best_individual = population[max_index]
        
        print(f"Поколение {generation}: Лучшее значение = {best_individual}, Максимальная приспособленность = {max_fitness}")
        
        # Создаем новую популяцию для следующего поколения
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = select_parents(population, fitness_scores)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        
        population = new_population
    
    return best_individual

# Параметры генетического алгоритма
population_size = 100
min_value = -12
max_value = 51
num_generations = 50
mutation_rate = 0.01

# Запуск генетического алгоритма
best_solution = genetic_algorithm(population_size, min_value, max_value, num_generations, mutation_rate)
print("Максимум функции:", fitness_function(best_solution))
