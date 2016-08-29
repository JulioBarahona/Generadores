# coding=utf-8
"""
Julio Barahona , 141206
Diego Castañeda
Semana 8
UVG
"""
#import simpy
import random
from math import *

# How many programs the CPU is gonna work
totalProcesses =  25;
arrayProcesses = []

# Generates random memory requeired for a new program, takes away the local memory
# Random 1-10
def newArrayOfPrograms(numberOfPrograms):
   for i in numberOfPrograms:
        #generates random integer from 1 to 10
        yield random.randint(1,10)

for i in (newArrayOfPrograms(totalProcesses)):
    print i

# Process thats is run by CPU
# random 1-10
def ready():
    return null

# Can handl eonly 3 instructions
# Each instructions takes an X time (mutiplier of the memory needed)
#
def running():
    return null