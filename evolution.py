from __future__ import annotations
from random import choices, random, randint, shuffle

from playfair import Playfair
from settings import ALPHABET, KEEP_FITTEST

def new_solution_from_a(
        a: Solution,
        b: Solution,
        split: int,
        mutate: float,
    ) -> Solution:
    """Creates a new solution using A as the primary parent.
    
    The first `split` characters from A are used to create the new solution,
    the remaining characters are taken from B in order unless already selected
    from A.

    Args:
        a: The primary parent solution
        b: The secondary parent solution
        split: The index to split the key at
        mutate: The probability of a mutation
    Returns:
        Solution: A new child solution
    """
    a_key = a.key[:split]
    b_key = ""
    for c in b.key:
        if c not in a_key:
            b_key += c
    new_key = list(a_key + b_key)
    # Mutate the new key
    for i in range(len(new_key)):
        if random() < mutate:
            # Select another index, excluding itself to swap with
            swap_i = (i + randint(1, 24)) % 25
            new_key[i], new_key[swap_i] = new_key[swap_i], new_key[i]
    return Solution("".join(new_key))

def tournament_select(population: list[Solution], tournament_size: int = 2) -> Solution:
    """
    Select a solution from the given population using tournament selection
    """
    # Return the solution with the highest fitness
    solutions = choices(population, k=tournament_size)
    solutions.sort(key=lambda x: x.score)
    return solutions[-1]

class Solution(Playfair):

    def compute_score(self, cipher, target) -> None:
        count = 0
        decrypted = self.decrypt(cipher)
        for i in range(len(target)):
            count += int(decrypted[i] == target[i])
        self.score = count / len(target)

    def cross(self, other: Solution, mutate: float) -> list[Solution]:
        # Get a random split point
        split = randint(1, 23)
        return [
            new_solution_from_a(self, other, split, mutate),
            new_solution_from_a(other, self, split, mutate),
        ]

def random_key():
    alphabet = list(ALPHABET)
    shuffle(alphabet)
    return "".join(alphabet)

class Simulation:

    def __init__(self, population_size: int, mutate: float = 0.1, max_generations: int = 1000):
        self.max_generations = max_generations
        self.population_size = population_size
        self.mutate = mutate
        self.population = [
                Solution(random_key())
                for i in range(population_size)
        ]

    def go(self, cipher_text, plain_text):
        generation = 0
        while generation < self.max_generations:
            generation += 1
            for s in self.population:
                s.compute_score(cipher_text, plain_text)
            self.population.sort(key=lambda x: x.score)
            if self.population[-1].score == 1:
                print()
                print("SOLUTION FOUND!")
                print(str(self.population[-1]))
                print(self.population[-1].decrypt(cipher_text))
                return
            print(f"Generation: {generation}, Fitness: {self.population[-1].score:.4f}", end='\r')
            if KEEP_FITTEST:
                new_population = self.population[-KEEP_FITTEST:]
            for i in range((self.population_size // 2) - KEEP_FITTEST):
                parent_a = tournament_select(self.population)
                parent_b = tournament_select(self.population)
                children = parent_a.cross(parent_b, self.mutate)
                new_population += children
            self.population = new_population
        for s in self.population:
            s.compute_score(cipher_text, plain_text)
        self.population.sort(key=lambda x: x.score)
        print()
        print("Best:")
        print(str(self.population[-1]))
        print(self.population[-1].decrypt(cipher_text))

