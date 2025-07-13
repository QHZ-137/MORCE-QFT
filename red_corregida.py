

import math

phi = (1 + 5**0.5) / 2

# Nodos originales
nodos_originales = {
    1: (1, 1, 1),
    2: (1, 1, -1),
    3: (1, -1, 1),
    4: (1, -1, -1),
    5: (-1, 1, 1),
    6: (-1, 1, -1),
    7: (-1, -1, 1),
    8: (-1, -1, -1),
    9:  (0, 1/phi,  phi),
    10: (0, -1/phi, -phi),
    11: (1/phi,  phi, 0),
    12: (-1/phi, -phi, 0)
}

nodos_corregidos = nodos_originales.copy()
angle_rad = math.radians(70.5288)

r = math.sqrt((1/phi)**2 + (phi)**2)
new_y = math.sin(angle_rad) * r
new_z = math.cos(angle_rad) * r
nodos_corregidos[9] = (0, new_y, new_z)
nodos_corregidos[10] = (0, -new_y, -new_z)

new_x = math.sin(angle_rad) * r
new_y2 = math.cos(angle_rad) * r
nodos_corregidos[11] = (new_x, new_y2, 0)
nodos_corregidos[12] = (-new_x, -new_y2, 0)

def vector_to_geo(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)
    lat = math.asin(z / r) * (180 / math.pi)
    lon = math.atan2(y, x) * (180 / math.pi)
    return lat, lon

def dot_product(a, b):
    return sum(x*y for x, y in zip(a, b))

def magnitude(v):
    return math.sqrt(sum(x*x for x in v))

def angle_between(v1, v2):
    dp = dot_product(v1, v2)
    mag1 = magnitude(v1)
    mag2 = magnitude(v2)
    cos_theta = dp / (mag1 * mag2)
    cos_theta = min(1, max(-1, cos_theta))
    return math.degrees(math.acos(cos_theta))

print("\nCOMPARATIVA DE COORDENADAS:")
for i in range(9, 13):
    lat_old, lon_old = vector_to_geo(*nodos_originales[i])
    lat_new, lon_new = vector_to_geo(*nodos_corregidos[i])
    print(f"\nNodo {i}:")
    print(f"  Original → Lat: {lat_old:.4f}°, Lon: {lon_old:.4f}°")
    print(f"  Corregido → Lat: {lat_new:.4f}°, Lon: {lon_new:.4f}°")

print("\nNUEVOS ÁNGULOS ENTRE PARES:")
pares = [(9, 10), (11, 12)]
for a, b in pares:
    angle = angle_between(nodos_corregidos[a], nodos_corregidos[b])
    print(f"Nodos {a} y {b}: {angle:.4f} grados")

print("\nCOORDENADAS PARA GOOGLE EARTH:")
for i in range(1, 13):
    lat, lon = vector_to_geo(*nodos_corregidos[i])
    print(f"Nodo {i}: {lat:.5f}, {lon:.5f}")
