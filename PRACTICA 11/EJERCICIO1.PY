class Artista:
    def __init__(self, nombre, ci, años_experiencia):
        self.nombre = nombre
        self.ci = ci
        self.años_experiencia = años_experiencia

class Obra:
    def __init__(self, titulo, material, artista):
        self.titulo = titulo
        self.material = material
        self.artista = artista

class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio

class Pintura:
    def __init__(self, genero, obra, anuncio=None):
        self.genero = genero
        self.obra = obra
        self.anuncio = anuncio

# a. 
artista1 = Artista("Pablo Picasso", "12345678", 40)
artista2 = Artista("Frida Kahlo", "87654321", 30)

obra1 = Obra("Guernica", "Óleo", artista1)
obra2 = Obra("Las dos Fridas", "Óleo", artista2)

anuncio1 = Anuncio(1, 50000)

pintura_con_anuncio = Pintura("Surrealismo", obra1, anuncio1)
pintura_sin_anuncio = Pintura("Realismo", obra2)

# b. 
artistas = [pintura_con_anuncio.obra.artista, pintura_sin_anuncio.obra.artista]
artista_con_mas_experiencia = max(artistas, key=lambda a: a.años_experiencia)
print(f"El artista con más años de experiencia es: {artista_con_mas_experiencia.nombre}")

# c. 
anuncio2 = Anuncio(2, 30000)
pintura_sin_anuncio.anuncio = anuncio2

monto_total = (
    pintura_con_anuncio.anuncio.precio +
    pintura_sin_anuncio.anuncio.precio
)

print(f"Monto total de venta de ambas pinturas: {monto_total}")