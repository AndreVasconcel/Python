def calcular_area_retangulo(base, altura):
    area = base*altura

    return area

base = float(input("Base: "))
altura = float(input("Altura: "))

print("A área é:", calcular_area_retangulo(base, altura))