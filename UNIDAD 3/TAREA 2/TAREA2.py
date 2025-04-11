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
