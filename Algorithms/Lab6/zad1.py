import random
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Load data from a text file
objects = []
with open('packages/packages20.txt') as txt:
    lines = txt.readlines()
    for i in range(2, len(lines)):
        index, x, y, z = map(int, lines[i].split(","))
        objects.append((x, y, z))

# Genetic algorithm parameters
bag_size = [20, 20]
population_size = 100
generations = 50
mutation_rate = 0.01

# Function to check if an item fits in the knapsack
def can_item_fit(item_width, item_height, knapsack):
    for x1 in range(len(knapsack) - item_width + 1):
        for y1 in range(len(knapsack) - item_height + 1):
            fits = True
            for x2 in range(item_width):
                for y2 in range(item_height):
                    if knapsack[x1 + x2][y1 + y2]:
                        fits = False
                        break
                if not fits:
                    break
            if fits:
                return (x1, y1, False)
    for x1 in range(len(knapsack) - item_height + 1):
        for y1 in range(len(knapsack) - item_width + 1):
            fits = True
            for x2 in range(item_height):
                for y2 in range(item_width):
                    if knapsack[y1 + y2][x1 + x2]:
                        fits = False
                        break
                if not fits:
                    break
            if fits:
                return (x1, y1, True)
    return False

# Greedy algorithm to solve the 2D knapsack problem with visualization
def greedy_algorithm(objects, bag_size):
    knapsack = [[0 for j in range(bag_size[0])] for i in range(bag_size[1])]
    value = 0
    sorted_objects = sorted(objects, key=lambda x: x[2], reverse=True)
    fig, ax = plt.subplots(1)
    ax.set_xlim([0, bag_size[0]])
    ax.set_ylim([0, bag_size[1]])
    for obj in sorted_objects:
        fit = can_item_fit(obj[0], obj[1], knapsack)
        if fit:
            if fit[2]:
                for x in range(fit[0], obj[0] + fit[0]):
                    for y in range(fit[1], obj[1] + fit[1]):
                        knapsack[y][x] = 1
                ax.add_patch(patches.Rectangle((fit[0], fit[1]), obj[1], obj[0], edgecolor='black', facecolor='none'))
            else:
                for x in range(fit[0], obj[0] + fit[0]):
                    for y in range(fit[1], obj[1] + fit[1]):
                        knapsack[x][y] = 1
                ax.add_patch(patches.Rectangle((fit[0], fit[1]), obj[0], obj[1], edgecolor='black', facecolor='none'))
            value += obj[2]
    plt.title('Greedy Algorithm Solution')
    plt.xlabel('Width')
    plt.ylabel('Height')
    plt.show()

# Genetic Algorithm class for solving the 2D knapsack problem
class GeneticAlgorithm2d:
    def __init__(self, objects, bag_size, population_size, generations, mutation_rate):
        self.objects = objects
        self.bag_size = bag_size
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    # Function to calculate the fitness value of an individual
    def fitness(self, individual):
        knapsack = [[0 for j in range(self.bag_size[0])] for i in range(self.bag_size[1])]
        value = 0
        for i in range(len(individual)):
            if individual[i] == 1:
                fit = can_item_fit(self.objects[i][0], self.objects[i][1], knapsack)
                if fit:
                    if fit[2]:
                        for x in range(fit[0], self.objects[i][0] + fit[0]):
                            for y in range(fit[1], self.objects[i][1] + fit[1]):
                                knapsack[y][x] = 1
                    else:
                        for x in range(fit[0], self.objects[i][0] + fit[0]):
                            for y in range(fit[1], self.objects[i][1] + fit[1]):
                                knapsack[x][y] = 1
                    value += self.objects[i][2]
                else:
                    return 0
        return value

    # Function to create a random individual
    def create_individual(self):
        return [random.randint(0, 1) for i in range(len(self.objects))]

    # Function to create the initial population
    def create_population(self):
        return [self.create_individual() for i in range(self.population_size)]

    # Function for individual selection
    def selection(self, population):
        sorted_population = sorted(population, key=lambda x: self.fitness(x), reverse=True)
        return sorted_population[:self.population_size // 2]

    # Function for crossover between two individuals
    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, len(self.objects) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    # Function for individual mutation
    def mutation(self, individual):
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]
        return individual

    # Function to run the genetic algorithm
    def run(self):
        population = self.create_population()
        for i in range(self.generations):
            population = self.selection(population)
            new_population = []
            while len(new_population) < self.population_size:
                parent1 = random.choice(population)
                parent2 = random.choice(population)
                child1, child2 = self.crossover(parent1, parent2)
                new_population.append(self.mutation(child1))
                new_population.append(self.mutation(child2))
            population = new_population
        best_individual = max(population, key=lambda x: self.fitness(x))
        return best_individual

# Create an instance of the GeneticAlgorithm2d class
ga = GeneticAlgorithm2d(objects, bag_size, population_size, generations, mutation_rate)

# Run the genetic algorithm and measure the time
stime = time.time()
best_individual = ga.run()
genetic_time = time.time() - stime

# Get the value of the best individual from the genetic algorithm
best_value = ga.fitness(best_individual)

# Print the results of the genetic algorithm
print("Genetic Algorithm Solution:")
print(best_individual)
print("Best Value:", best_value)
print("Time:", genetic_time)

# Measure the time of the greedy algorithm
stime = time.time()
greedy_value = greedy_algorithm(objects, bag_size)
greedy_time = time.time() - stime

# Print the results of the greedy algorithm
print("\nGreedy Algorithm Solution:")
print(greedy_value)
print("Time:", greedy_time)

# Function to visualize the genetic algorithm's solution
def visualize_genetic(best_individual, best_value):
    knapsack = [[0 for j in range(bag_size[0])] for i in range(bag_size[1])]
    fig, ax = plt.subplots(1)
    ax.set_xlim([0, bag_size[0]])
    ax.set_ylim([0, bag_size[1]])

    for i in range(len(best_individual)):
        if best_individual[i] == 1:
            fit = can_item_fit(objects[i][0], objects[i][1], knapsack)
            if fit:
                if fit[2]:
                    for x in range(fit[0], objects[i][0] + fit[0]):
                        for y in range(fit[1], objects[i][1] + fit[1]):
                            knapsack[y][x] = 1
                    ax.add_patch(patches.Rectangle((fit[0], fit[1]), objects[i][1], objects[i][0],
                                                   edgecolor='black', facecolor='none'))
                else:
                    for x in range(fit[0], objects[i][0] + fit[0]):
                        for y in range(fit[1], objects[i][1] + fit[1]):
                            knapsack[x][y] = 1
                    ax.add_patch(patches.Rectangle((fit[0], fit[1]), objects[i][0], objects[i][1],
                                                   edgecolor='black', facecolor='none'))
    plt.title('Genetic Algorithm Solution')
    plt.xlabel('Width')
    plt.ylabel('Height')
    plt.show()

# Visualize the genetic algorithm's solution with added titles
visualize_genetic(best_individual, best_value)
