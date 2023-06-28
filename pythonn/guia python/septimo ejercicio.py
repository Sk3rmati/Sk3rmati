nombres = ["Matias", "Cristian", "Diego", "Manolo", "Parra"]
edades = [18, 19, 36, 99, 45]

informacion= nombres + edades

informacion = tuple((zip(nombres, edades)))
print(informacion)