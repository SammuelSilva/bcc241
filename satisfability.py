"""
    TP 2 - PAA
    Marcos Pontes e Sammuel Ramos

    Arquivo: satisfability.py

    Resolve o problema de satisfabilidade de FNC
"""
import os
from copy import copy

# Clause(x=0, y=1, z=-1) ==> (neg x V y)
class Clause:
    def __init__(self, values, start='a'):
        key = ord(start)
        self.variables = dict()
        for var in values:
            self.variables[chr(key)] = var
            key += 1

    def __getitem__(self, key):
        return self.variables[key]

    def __repr__(self):
        return f"Clause<{self.variables}>"

    def __str__(self):
        return f"Clause<{self.variables}>"

    def __copy__(self):
        return type(self)(self.variables.values())

def read_input(f):
    n_variables = -1
    clauses = []
    if os.path.exists(f):
        with open(f, "r") as file:
            n_variables = int(file.readline())
            for line in file:
                clause = Clause([int(i) for i in line.split(" ") if i != "\n"])
                clauses.append(clause)
    return n_variables, clauses


class SatisfabilitySolver:
    def __init__(self, n_variables, clauses):
        self.clauses = clauses
        self.n_variables = n_variables
        self.best_solution = None

    def satisfability_backtracking(self, solution, ord=97):
        index = chr(ord) # converte para caractere

        if self.is_complete(solution):
            print(f"Gerou solução={solution}")
            self.best_solution = copy(solution)
        else:
            for i in [0, 1]:
                solution.variables[index] = i # atribuo falso | verdadeiro
                if self.is_consistent(solution):
                    self.satisfability_backtracking(solution, ord+1)
                solution.variables[index] = -1 # backtrack


    def satisfability(self):
        solution = Clause(n_variables*[-1]) # começa com atribuição vazia
        self.satisfability_backtracking(solution)
        return self.best_solution

    def is_complete(self, solution):
        return all([var != -1 for var in solution.variables.values()]) # se eu ja atribui valores para todas as variaveis

    def is_consistent(self, solution):
        
        for clause in self.clauses:
            variables = []
            for key, var in clause.variables.items():
                if solution[key] == -1:
                    variables.append(None) # ainda nao tem valores atribuidos

                if var == 0:
                    variables.append(not bool(solution[key]))
                if var == 1:
                    variables.append(bool(solution[key]))                    

            if None not in variables and not any(variables): # aplica o 'ou' na lista
                return False
    
        return True


if __name__ == "__main__":
    n_variables, clauses = read_input("./satisfability2.txt")
    solver = SatisfabilitySolver(n_variables, clauses)
    solution = solver.satisfability()
    print(solution)
