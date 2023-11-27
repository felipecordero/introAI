import random
from IPython.display import display
import chess

total_solution = 25

def fitness(child):
    attacks = 0
    for i in range(len(child)):
        for j in range(i + 1, len(child)):
            # print(child[i], child[j])
            if child[i] == child[j]:
                attacks += 1
            elif abs(i - j) == abs(child[i] -  child[j]):
                attacks += 1
    return 28 - attacks

child = [1, 4, 3, 4, 7, 6, 2, 8]

fitness(child)

def crossover(parent_1, parent_2):
    child_1 = parent_1[:4]
    child_2 = parent_2[:4]
    child_1.extend(parent_1[4:])
    child_2.extend(parent_2[4:])

    return child_1, child_2

def mutate(child):
    random_index = random.randint(0,7)
    randon_value = random.randint(0,7)

    child[random_index] = randon_value

    return child

solutions = []

while len(solutions) < total_solution:
    father = []
    mother = []
    for i in range(8):
        father.append(random.randint(0, 7))
        mother.append(random.randint(0, 7))
    father_fitness = fitness(father)
    mother_fitness = fitness(mother)
    while father_fitness < 28 and mother_fitness < 28:
        child_1, child_2 = crossover(father, mother)
        child_3, child_4 = crossover(mother, father)

        children = [child_1, child_2, child_3, child_4]

        mutated_children = []
        children_fitness = []

        for child in children:
            child = mutate(child)
            mutated_children.append(child)
            children_fitness.append(fitness(child))
        
        # top_indexes = sorted(range(len(children_fitness)), key=lambda i: children_fitness[i][-2])
        top_indexes = sorted(range(len(children_fitness)), key=lambda i: children_fitness[i])[-2:]

        father = mutated_children[top_indexes[0]]
        mother = mutated_children[top_indexes[1]]

        father_fitness = children_fitness[top_indexes[0]]
        mother_fitness = children_fitness[top_indexes[1]]

    if father_fitness == 28:
        if father not in solutions:
            solutions.append(father)

    if mother_fitness == 28:
        if mother not in solutions:
            solutions.append(mother)

for s in solutions:
    p = []
    board = chess.Board()
    board.clear()
    for i in s:
        p1 = "Q7"
        if i == 0:
            p1 = "Q7"
        if i != 0 and i != 7:
            p1 = str(i) + "Q" + str(7 - i)
        elif i == 7:
            p1 = "7Q"
        p.append(p1)

    fen = "{}/{}/{}/{}/{}/{}/{}/{} w KQkq - 0 6".format(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7])

    board.set_fen(fen)
    display(board)