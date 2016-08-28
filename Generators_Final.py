# coding=utf-8
"""
Julio Barahona , 141206
Diego Castañeda
Semana 8
UVG
"""
import simpy
import random
from math import *

# How many programs the CPU is gonna work
totalProcesses =  25;
arrayProcesses = []

# fills the array with aleatory memory requirements
for i in range (0,totalProcesses):
    arrayProcesses.append(int(random.randint(1,10)))
    i = i + 1

#shows array of random numbets (0,10), REMOVE?
print arrayProcesses


# Generates random memory requeired for a new program, takes away the local memory
# Random 1-10
def newArrayOfPrograms(arrayOfProccesses,numberOfPrograms):


    while (i<numberOfPrograms):
        #generates random integer from 1 to 10
        yield null

# Process thats is run by CPU
# random 1-10
def ready():
    return null

# Can handl eonly 3 instructions
# Each instructions takes an X time (mutiplier of the memory needed)
#
def running():
    return null