import math

def area_circulo(raio):
    return math.pi * raio ** 2

# Teste a função
raio = 5
area = area_circulo(raio)
print(f"A área do círculo com raio {raio} é {area:.2f}")
