import random
import math

ciudades = [
    "Gerona", "Barcelona", "Zaragoza", "Bilbao", "Celta", "Vigo", "Valladolid",
    "Madrid", "Jaen", "Sevilla", "Granada", "Albacete", "Murcia", "Valencia"
]

coordenadas = {
    'Gerona': (9, 9),
    'Barcelona': (8, 8),
    'Zaragoza': (6, 7),
    'Bilbao': (4, 9),
    'Celta': (1, 8),
    'Vigo': (1, 7),
    'Valladolid': (3, 7),
    'Madrid': (4, 6),
    'Jaen': (3, 4),
    'Sevilla': (2, 3),
    'Granada': (4, 3),
    'Albacete': (5, 5),
    'Murcia': (6, 4),
    'Valencia': (7, 6)
}

distancias = {
    ("Gerona", "Barcelona"): 100,
    ("Barcelona", "Zaragoza"): 296,
    ("Zaragoza", "Bilbao"): 324,
    ("Bilbao", "Celta"): 378,
    ("Celta", "Vigo"): 171,
    ("Vigo", "Valladolid"): 356,
    ("Valladolid", "Celta"): 235,
    ("Valladolid", "Madrid"): 193,
    ("Valladolid", "Zaragoza"): 390,
    ("Madrid", "Zaragoza"): 190,
    ("Madrid", "Albacete"): 251,
    ("Madrid", "Jaen"): 411,
    ("Jaen", "Valladolid"): 411,
    ("Jaen", "Sevilla"): 125,
    ("Sevilla", "Granada"): 211,
    ("Granada", "Jaen"): 207,
    ("Granada", "Albacete"): 244,
    ("Albacete", "Murcia"): 150,
    ("Murcia", "Valencia"): 241,
    ("Valencia", "Barcelona"): 349,
    ("Zaragoza", "Valencia"): 290,
    ("Zaragoza", "Albacete"): 215,
    ("Murcia", "Granada"): 257,
    ("Valencia", "Albacete"): 191
}

def distancia_geografica(ciudad1, ciudad2):
    x1, y1 = coordenadas[ciudad1]
    x2, y2 = coordenadas[ciudad2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def costo_ruta(ruta):
    costo = 0
    for i in range(len(ruta)):
        origen = ruta[i]
        destino = ruta[(i + 1) % len(ruta)]
        if (origen, destino) in distancias:
            d = distancias[(origen, destino)]
        elif (destino, origen) in distancias:
            d = distancias[(destino, origen)]
        else:
            d = 9999

        d += distancia_geografica(origen, destino) * 150
        costo += d
    return costo

def crear_poblacion(tamano):
    return [random.sample(ciudades, len(ciudades)) for _ in range(tamano)]

def seleccion(poblacion):
    torneo = random.sample(poblacion, 5)
    return min(torneo, key=costo_ruta)

def cruce(p1, p2):
    a, b = sorted(random.sample(range(len(p1)), 2))
    hijo = [None] * len(p1)
    hijo[a:b] = p1[a:b]
    pos = b
    for ciudad in p2:
        if ciudad not in hijo:
            while hijo[pos % len(p1)] is not None:
                pos += 1
            hijo[pos % len(p1)] = ciudad
    return hijo

def mutacion(ruta, prob=0.2):
    if random.random() < prob:
        a, b = random.sample(range(len(ruta)), 2)
        ruta[a], ruta[b] = ruta[b], ruta[a]
    return ruta

def algoritmo_genetico(tamano_poblacion=100, generaciones=500):
    poblacion = crear_poblacion(tamano_poblacion)
    mejor = min(poblacion, key=costo_ruta)

    for _ in range(generaciones):
        nueva_poblacion = []
        for _ in range(tamano_poblacion):
            padre1 = seleccion(poblacion)
            padre2 = seleccion(poblacion)
            hijo = cruce(padre1, padre2)
            hijo = mutacion(hijo)
            nueva_poblacion.append(hijo)
        poblacion = nueva_poblacion
        mejor_actual = min(poblacion, key=costo_ruta)
        if costo_ruta(mejor_actual) < costo_ruta(mejor):
            mejor = mejor_actual
    return mejor

mejor_ruta = algoritmo_genetico()
print("Ruta óptima:")
for ciudad in mejor_ruta:
    print(ciudad, end=" -> ")
print(mejor_ruta[0])
print("Costo total:", round(costo_ruta(mejor_ruta), 2))