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



class Proceso:

    def _init_(self,env):
        self.cpu = simpy.Resource(env, capacity = 1)
        self.memoria = simpy.Container(env,init=100, capacity = 100)



def Simulacion(env, nombre, inicio, mem, instrucciones, respuesta):

    yield env,timeout(llegada)
    print('%s inicio a procesar en tiempo %d'%(nombre, env.now))

    yield simular.memoria.get(mem)

    while instrucciones > 0:
        with simular.cpu.request() as req:
            yield req
            intrucciones = instrucciones - 3

            if respuesta == 1:
                print ("Proceso %s entra a IO en tiempo %d"%(nombre,env.now))
                yield env.timeout(15)
                print ("Proceso %s sale de IO en tiempo %d"%(nombre,env.now))

    yield simular.memoria.put(mem)
    print("Proceso %s termino en tiempo %d"%(nombre, env.now))
  

# Elementos de Simpy antes de comenzar a trabaajar
env = simpy.Environment()
memoria = simpy.Container(env, init = 100, capacity = 100)
cpu     = simpy.Resource(env, capacity = 1)
IO     = simpy.Resource(env, capacity = 1)


#*******************************
simular = Proceso(env)
#*******************************



#Datos que se necesitan para cada proceso

RANDOM_SEED = 42            # ESTO EN REALIDAD NO SIRVE, HAY QUE CHEQUEAR
random.seed(RANDOM_SEED)    #EL EJEMPLO DE DOUGLAS Y COMO LO USO

intervalo = 10
contador = 1

# How many programs the CPU is gonna work
totalProcesses =  25;


#se crean la cantidad necesaria de procesos segun el numero propuesto arriba
while contador <= totalProcesses:
    instrucciones  = random.randint(1,10)
    mem            = random.randint(1,10)
    respuesta      = random.randint(1,2)

    #el intervalo sirve para lambda = (1.0/intervalo) que nos dara
    #una secuencia de numeros del 0 al infinito, la cual siempre
    #se repetira si es ingresado el mismo numero al principio
    
    inicio = random.expovariate(1.0/intervalo)

    #Finalmente se crea, con los argumentos anteriores, un nuevo proceso
    env.process(Simulacion(env, "Proceso %d"%contador, inicio, mem , instrucciones, respuesta))
    contador = contador + 1

#iniciar hasta que se acaben los procesos
env.run()


