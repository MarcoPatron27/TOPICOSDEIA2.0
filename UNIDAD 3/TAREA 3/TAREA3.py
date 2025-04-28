"""
import random

# Función objetivo (puedes cambiarla por la que necesites)
def funcion_objetivo(x):
    return x**2

# Clase Particula
class Particula:
    def __init__(self, limites):
        self.posicion = random.uniform(limites[0], limites[1])
        self.velocidad = random.uniform(-1, 1)
        self.mejor_posicion = self.posicion
        self.valor = funcion_objetivo(self.posicion)
        self.mejor_valor = self.valor

    def actualizar_velocidad(self, mejor_posicion_global, w=0.5, c1=2, c2=2):
        r1 = random.random()
        r2 = random.random()
        cognitivo = c1 * r1 * (self.mejor_posicion - self.posicion)
        social = c2 * r2 * (mejor_posicion_global - self.posicion)
        self.velocidad = w * self.velocidad + cognitivo + social

    def actualizar_posicion(self, limites):
        self.posicion += self.velocidad
        #Limites
        self.posicion = max(min(self.posicion, limites[1]), limites[0])
        #Eva
        self.valor = funcion_objetivo(self.posicion)
        if self.valor < self.mejor_valor:
            self.mejor_posicion = self.posicion
            self.mejor_valor = self.valor

# Clase Enjambre
class Enjambre:
    def __init__(self, num_particulas, limites):
        self.particulas = [Particula(limites) for _ in range(num_particulas)]
        self.mejor_posicion_global = self.particulas[0].mejor_posicion
        self.mejor_valor_global = self.particulas[0].mejor_valor
        self.limites = limites
        self.actualizar_mejor_global()

    def actualizar_mejor_global(self):
        for particula in self.particulas:
            if particula.mejor_valor < self.mejor_valor_global:
                self.mejor_valor_global = particula.mejor_valor
                self.mejor_posicion_global = particula.mejor_posicion

    def ejecutar(self, iteraciones):
        for i in range(iteraciones):
            for particula in self.particulas:
                particula.actualizar_velocidad(self.mejor_posicion_global)
                particula.actualizar_posicion(self.limites)
            self.actualizar_mejor_global()
            print(f"Iteración {i+1}: Mejor valor global = {self.mejor_valor_global:.4f} en posición = {self.mejor_posicion_global:.4f}")

# Parámetros
limites = (-10, 10)
num_particulas = 1
iteraciones = 5

# Ejecutar PSO
enjambre = Enjambre(num_particulas, limites)
enjambre.ejecutar(iteraciones)
"""
import random
import math

# Función de distancia total para el Agente Viajero
def funcion_objetivo(ruta, ciudades):
    distancia = 0
    for i in range(len(ruta)):
        ciudad_origen = ciudades[ruta[i]]
        ciudad_destino = ciudades[(ruta[(i + 1) % len(ruta)])]
        distancia += math.dist(ciudad_origen, ciudad_destino)
    return distancia

# Clase Partícula
class Particula:
    def __init__(self, ciudades):
        self.ciudades = ciudades
        self.posicion = list(range(len(ciudades)))
        random.shuffle(self.posicion)
        self.velocidad = []
        self.mejor_posicion = self.posicion.copy()
        self.valor = funcion_objetivo(self.posicion, ciudades)
        self.mejor_valor = self.valor

    def mover_particula(self):
        for (i, j) in self.velocidad:
            self.posicion[i], self.posicion[j] = self.posicion[j], self.posicion[i]

    def evaluar_particula(self):
        valor_actual = funcion_objetivo(self.posicion, self.ciudades)
        if valor_actual < self.mejor_valor:
            self.mejor_valor = valor_actual
            self.mejor_posicion = self.posicion.copy()

    def actualizar_velocidad(self, mejor_posicion_global, w=0.5, c1=1.5, c2=1.5):
        nueva_velocidad = []

        # Comparar con mejor personal
        for i in range(len(self.posicion)):
            if self.posicion[i] != self.mejor_posicion[i]:
                j = self.posicion.index(self.mejor_posicion[i])
                nueva_velocidad.append((i, j))
                self.posicion[i], self.posicion[j] = self.posicion[j], self.posicion[i]

        # Comparar con mejor global
        for i in range(len(self.posicion)):
            if self.posicion[i] != mejor_posicion_global[i]:
                j = self.posicion.index(mejor_posicion_global[i])
                nueva_velocidad.append((i, j))
                self.posicion[i], self.posicion[j] = self.posicion[j], self.posicion[i]

        self.velocidad = nueva_velocidad

# Clase Enjambre
class Enjambre:
    def __init__(self, num_particulas, ciudades):
        self.particulas = [Particula(ciudades) for _ in range(num_particulas)]
        self.ciudades = ciudades
        self.mejor_posicion_global = self.particulas[0].mejor_posicion.copy()
        self.mejor_valor_global = self.particulas[0].mejor_valor
        self.evaluar_enjambre()

    def mover_enjambre(self):
        for particula in self.particulas:
            particula.actualizar_velocidad(self.mejor_posicion_global)
            particula.mover_particula()

    def evaluar_enjambre(self):
        for particula in self.particulas:
            particula.evaluar_particula()
            if particula.mejor_valor < self.mejor_valor_global:
                self.mejor_valor_global = particula.mejor_valor
                self.mejor_posicion_global = particula.mejor_posicion.copy()

    def ejecutar(self, iteraciones):
        for i in range(iteraciones):
            self.mover_enjambre()
            self.evaluar_enjambre()
            print(f"Iteración {i+1}: Mejor distancia global = {self.mejor_valor_global:.4f}")
            print(f"Ruta: {self.mejor_posicion_global}")

# Datos del problema (coordenadas de las ciudades)
ciudades = [
    (0, 0),
    (1, 5),
    (5, 2),
    (6, 6),
    (8, 3)
]

# Parámetros
num_particulas = 10
iteraciones = 20

# Ejecutar PSO para TSP
enjambre = Enjambre(num_particulas, ciudades)
enjambre.ejecutar(iteraciones)

