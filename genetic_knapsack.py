import random
import numpy as np

# Parâmetros do algoritmo genético
POPULATION_SIZE = 100
MAX_GENERATIONS = 100
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.1

# Definição dos itens e suas propriedades (valor e peso)
items = [
    {"name": "Item 1", "value": 10, "weight": 5},
    {"name": "Item 2", "value": 8, "weight": 2},
    {"name": "Item 3", "value": 15, "weight": 8},
    {"name": "Item 4", "value": 12, "weight": 3},
    {"name": "Item 5", "value": 20, "weight": 10},
]

# Capacidade máxima da mochila
MAX_CAPACITY = 50


def generate_individual():
    """Gera um indivíduo aleatório (vetor binário)."""
    return [random.randint(0, 1) for _ in range(len(items))]


def calculate_fitness(individual):
    """Calcula a pontuação (fitness) de um indivíduo."""
    total_value = 0
    total_weight = 0
    for i in range(len(items)):
        if individual[i] == 1:
            total_value += items[i]["value"]
            total_weight += items[i]["weight"]
    if total_weight > MAX_CAPACITY:
        total_value = 0  # Penaliza a solução se a capacidade for excedida
    return total_value


def selection(population):
    """Realiza a seleção de pais utilizando o método da roleta viciada."""
    total_fitness = sum(calculate_fitness(individual) for individual in population)
    probabilities = [calculate_fitness(individual) / total_fitness for individual in population]
    return random.choices(population, probabilities, k=2)


def crossover(parent1, parent2):
    """Realiza o cruzamento (recombinação) de dois indivíduos."""
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(1, len(items) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2
    else:
        return parent1, parent2


def mutation(individual):
    """Realiza a mutação em um indivíduo."""
    mutated_individual = []
    for gene in individual:
        if random.random() < MUTATION_RATE:
            mutated_individual.append(1 - gene)  # Inverte o bit
        else:
            mutated_individual.append(gene)
    return mutated_individual

def genetic_algorithm():
    # Inicialização da população
    population = [generate_individual() for _ in range(POPULATION_SIZE)]

    for generation in range(MAX_GENERATIONS):
        # Avaliação da aptidão dos indivíduos
        fitness_scores = [calculate_fitness(individual) for individual in population]

        # Melhor indivíduo da geração
        best_individual = population[fitness_scores.index(max(fitness_scores))]
        best_fitness = max(fitness_scores)

        print(f"Generation {generation + 1} - Best Fitness: {best_fitness}")

        # Seleção e cruzamento para gerar a próxima geração
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            # Seleção de pais
            parent1, parent2 = selection(population)

            # Cruzamento (recombinação)
            child1, child2 = crossover(parent1, parent2)

            # Mutação
            child1 = mutation(child1)
            child2 = mutation(child2)

            # Adicionar os descendentes à nova população
            new_population.extend([child1, child2])

        # Substituir a população atual pela nova população
        population = new_population

    # Avaliação final da aptidão dos indivíduos
    fitness_scores = [calculate_fitness(individual) for individual in population]

    # Melhor indivíduo da última geração
    best_individual = population[fitness_scores.index(max(fitness_scores))]
    best_fitness = max(fitness_scores)

    # Imprimir resultados
    print("Genetic Algorithm - Knapsack Problem")
    print(f"Best Solution: {best_individual}")
    print(f"Best Fitness: {best_fitness}")

genetic_algorithm()
