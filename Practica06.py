# Declara una lista de cadenas
aves = ["Loro gris", "Paloma de diamante", "C�ctel"]

print("Los valores de la lista antes de insertar:")

# Itera sobre la lista para imprimir los valores
for ave in aves:
    print(ave, end=", ")  # Agrega una coma y un espacio entre elementos

print("\n")

# Agrega tres valores al final de la lista utilizando el m�todo append()
aves.append("Mayna")
aves.append("Periquitos")
aves.append("Cacatua")

print("Los valores de la lista despu�s de insertar:")

# Itera sobre la lista para imprimir los valores
for ave in aves:
    print(ave, end=", ")  # Agrega una coma y un espacio entre elementos

print("\n")