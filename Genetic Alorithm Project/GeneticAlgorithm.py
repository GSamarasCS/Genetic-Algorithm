from random import *
from tkinter import *
from typing import *
from time import *

#basic keys
s_key = [1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1]
p_key = [1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1]

#variables
numPopulation = int
Population = []
Fitness = []
Parents = []
NewGeneration = []
NewFitness = []
BestKid = []
gencounter = 0

#spawning function -> spawns the first generation
def spawning(population: int):
    spawn_population = []
    for i in range(population):
        genome = []
        genome = choices([0,1], k=77)
        spawn_population.append(genome)
    return spawn_population

#fitness function -> calculates the fitness score of each kid of a generation
def fitness(population: Population, key: s_key):
    values = []
    for kid in population:
        value = 0
        for (n,m) in zip(kid,key) :
            if n == m:
                value += 1

        values.append(value)
    return values

#biased roulete function -> Choses 2 random parents from the generation, where parents with higher fitness have better chances to be selected 
def biased_roulete_selection(population: Population, fitness: Fitness):
    parents = choices(population, weights=fitness, k=2)
    while parents[0] == parents[1]:
        parents[1] = choices(population, weights=fitness, k=1)
    return parents

#singe point crossover function -> creates 2 new kids with the chosen parents from above
def single_point_crossover(parents: Parents):
    p = randint(1,76)
    child1 = parents[0][0:p] + parents[1][p:]
    child2 = parents[1][0:p] + parents[0][p:]
    children = [child1, child2]
    return children

#new generation function -> creates the new generation using the kids we made and elitism (keeps the 2 best kids from the previous generation)
def new_generation(population: Population, fitness: Fitness):
    newgeneration = []
    for i in range(int(len(population)/2 - 1)):
        parents = biased_roulete_selection(population,fitness)
        children = single_point_crossover(parents)
        newgeneration.append(children[0])
        newgeneration.append(children[1])
    newgeneration.append(population[fitness.index(max(fitness))])
    fitness.pop(fitness.index(max(fitness)))
    newgeneration.append(population[fitness.index(max(fitness))])
    return newgeneration

#mutation function -> A random chance to change a kid from the new generation in a random spot
def mutation(population: Population):
    for i in Population:
        n = randint(1,10)
        if n == 1:
            j = randrange(len(i))
            if i[j] == 1: i[j] = 0
            elif i[j] == 0: i[j] = 1
    return population

#create table function -> creates the representation of the kid with the highest fitness score of a generation
def create_table(bestkid: BestKid):
    n = 0
    height = 11
    width = 7
    for i in range(height):  # Rows
        for j in range(width):  # Columns
            if bestkid[n] == 1:
                b = Button(bframe, state='disabled', bg="black", padx=25, pady=10)
                b.grid(row=i, column=j)
            elif bestkid[n] == 0:
                b = Button(bframe, state='disabled', bg="white", padx=25, pady=10)
                b.grid(row=i, column=j)
            n += 1
            if n > 76: break

#excecute order s function -> function that excecutes the code to find the letter Σ, binded to the designated button
def excecute_order_s():
    s_key = [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
             0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1,
             1, 1, 1, 1, 1]
    Population = []
    Fitness = []
    Parents = []
    NewGeneration = []
    NewFitness = []
    gencounter = 0

    Population = spawning(100)
    Fitness = fitness(Population,s_key)

    gc = 0
    for i in range(10000):
        gencounter += 1
        gc += 1
        NewGeneration = mutation(new_generation(Population, Fitness))
        NewFitness = fitness(NewGeneration, s_key)
        if max(NewFitness) >= 77:
            BestKid = NewGeneration[NewFitness.index(max(NewFitness))]
            create_table(BestKid)
            gen_counter_s = Label(eframe, text="Generation: " + str(gencounter))
            gen_counter_s.grid(column=0, row=1)
            break
        else:
            Population = NewGeneration
            Fitness = NewFitness
            if gc == 50:
                gc = 0
                BestKid = NewGeneration[NewFitness.index(max(NewFitness))]
                create_table(BestKid)
                gen_counter_s = Label(eframe, text="Generation: " + str(gencounter))
                gen_counter_s.grid(column=0, row=1)
                Tk.update(bframe)
                Tk.update(eframe)
                sleep(0.5)
 
#excecute order p function -> function that excecutes the code to find the letter Π, binded to the designated button
def excecute_order_p():
    p_key = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1,
             0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0,
             0, 0, 0, 0, 1]

    Population = []
    Fitness = []
    Parents = []
    NewGeneration = []
    NewFitness = []
    gencounter = 0

    Population = spawning(100)
    Fitness = fitness(Population,p_key)

    gc = 0
    for i in range(10000):
        gencounter += 1
        gc += 1
        NewGeneration = mutation(new_generation(Population, Fitness))
        NewFitness = fitness(NewGeneration, p_key)
        if max(NewFitness) >= 77:
            BestKid = NewGeneration[NewFitness.index(max(NewFitness))]
            create_table(BestKid)
            gen_counter_p = Label(eframe, text="Generation: " + str(gencounter))
            gen_counter_p.grid(column=0, row=3)
            break
        else:
            Population = NewGeneration
            Fitness = NewFitness
            if gc == 50:
                gc = 0
                BestKid = NewGeneration[NewFitness.index(max(NewFitness))]
                create_table(BestKid)
                gen_counter_p = Label(eframe, text="Generation: " + str(gencounter))
                gen_counter_p.grid(column=0, row=3)
                Tk.update(bframe)
                Tk.update(eframe)
                sleep(0.5)
   
#Creation of the GUI for the application
root = Tk()
root.title('Genetic Algorithm')

#frames
bframe = LabelFrame(root, padx=10, pady=10)
bframe.grid( column=0, row=0, padx=10, pady=10)

eframe = LabelFrame(root, padx=10, pady=10)
eframe.grid(column=1, row=0)

#buttons
answer_s = Button(eframe, padx=40, pady=20, text="Φτιαξε Σ",command= excecute_order_s)
answer_s.grid(column=0, row=0)

answer_p = Button(eframe, padx=40, pady=20, text="Φτιαξε Π",command=excecute_order_p)
answer_p.grid(column=0, row=2)

#labels
gen_counter_s = Label(eframe, text= "Generation: " + str(gencounter))
gen_counter_s.grid(column=0, row=1)
gen_counter_p = Label(eframe, text= "Generation: " + str(gencounter))
gen_counter_p.grid(column=0, row=3)

#empty table creation
height = 11
width = 7
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Button(bframe, state='disabled', bg="white", padx=25, pady=10)
        b.grid(row=i, column=j)

#keeps the gui open untill someone shuts it down with the X button on the upper right corner
root.mainloop()