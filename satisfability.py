"""
    TP 2 - PAA
    Marcos Pontes e Sammuel Ramos

    Arquivo: satisfability.py

    Resolve o problema de satisfabilidade de FNC
"""
import os
from collections import namedtuple

Clause = namedtuple('Clause', ['x', 'y', 'z'])

def read_input(f, start):
    n_variables = -1
    variables = []
    if os.path.exists(f):
        with open(f, "r") as file:
            n_variables = int(file.readline())
            for line in file:
                clause = Clause(*[int(i) for i in line.split(" ") if i != "\n"])
                variables.append(clause)
    return n_variables, variables


if __name__ == "__main__":
    n_variables, variables = read_input("./satisfability.txt", start='a')
    print(n_variables, variables)
