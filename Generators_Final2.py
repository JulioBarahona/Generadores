# coding=utf-8

#Julio Barahona , 141206
#Diego Castaneda
#Semana 8
#UVG

import simpy
import random
from math import *

class SistemaOperativo:
    def __init__(self,env):
        self.cpu = simpy.Resource(env, capacity = 2)
        self.memoria= simpy.Container(env,init=100, capacity = 100)
        self.average = 0
        
        # How many programs the CPU is gonna work
        totalProcesses = 25
        contador = 1
        intervalo = 10

        while contador <= totalProcesses:
            instrucciones = random.randint(1, 10)
            mem = random.randint(1, 10)
            respuesta = random.randint(1, 2)

            # el intervalo sirve para lambda = (1.0/intervalo) que nos dara
            # una secuencia de numeros del 0 al infinito, la cual siempre
            # se repetira si es ingresado el mismo numero al principio

            inicio = random.expovariate(1.0 / intervalo)

            # Finalmente se crea, con los argumentos anteriores, un nuevo proceso
            contador = contador + 1
            env.process(self.Simulacion(env, "Proceso %d"%contador, inicio, mem , instrucciones, respuesta))



    def Simulacion(self, env, nombre, inicio, mem, instrucciones, respuesta):

        yield env.timeout(inicio)
        tiempoInicial = env.now
        print('%s inicio a procesar en tiempo %d'%(nombre, env.now))

        yield self.memoria.get(mem)

        while instrucciones > 0:
            with self.cpu.request() as req:
                yield req
                instrucciones = instrucciones - 3

                if respuesta == 1:
                    print ("Proceso %s entra a IO en tiempo %d"%(nombre,env.now))
                    yield env.timeout(15)
                    print ("Proceso %s sale de IO en tiempo %d"%(nombre,env.now))

        yield simular.memoria.put(mem)
        tiempoFinal = env.now
        promedio = (tiempoFinal - tiempoInicial)/2
        self.average = self.average + promedio
        print("Proceso %s termino en tiempo %d, con promedio %d"%(nombre, env.now, promedio))
        


# Elementos de Simpy antes de comenzar a trabaajar
env = simpy.Environment()

#*******************************
simular = SistemaOperativo(env)
#*******************************


#iniciar hasta que se acaben los procesos
env.run()
promedial = simular.average
resultado  = promedial/25
print ("El promedio de tiempos de los procesos es de %d"%resultado)
