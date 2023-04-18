import random

class Animal:
    def __init__(self, species):
        self.species = species
        self.energy = 100

    def eat(self):
        self.energy += 20

    def move(self):
        self.energy -= 10

    def reproduce(self):
        if self.energy >= 60:
            self.energy -= 60
            return Animal(self.species)
        else:
            return None

class AnimalWorld:
    def __init__(self, num_animals):
        self.animals = []
        for i in range(num_animals):
            species = random.choice(['lion', 'tiger', 'bear', 'wolf', 'elephant'])
            self.animals.append(Animal(species))

    def run_simulation(self):
        for i in range(10):
            for animal in self.animals:
                animal.move()
                animal.eat()
                baby = animal.reproduce()
                if baby is not None:
                    self.animals.append(baby)
