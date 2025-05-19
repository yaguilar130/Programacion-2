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
    def __init__(self, genero, obra, anuncio):
        self.genero = genero
        self.obra = obra
        self.anuncio = anuncio

# a. 
artista1 = Artista("Pablo Picasso", "12345678", 40)
artista2 = Artista("Frida Kahlo", "87654321", 30)

obra1 = Obra("Guernica", "Óleo", artista1)
obra2 = Obra("Las dos Fridas", "Óleo", artista2)

anuncio1 = Anuncio(1, 50000)
anuncio2 = Anuncio(2, 30000)

pintura1 = Pintura("Surrealismo", obra1, anuncio1)
pintura2 = Pintura("Realismo", obra2, anuncio2)

# b. 
artistas = [pintura1.obra.artista, pintura2.obra.artista]
promedio_experiencia = sum(a.años_experiencia for a in artistas) / len(artistas)
print(f"Promedio de años de experiencia: {promedio_experiencia}")

# c. 
def incrementar_precio(nombre_artista, incremento):
    for pintura in [pintura1, pintura2]:
        if pintura.obra.artista.nombre == nombre_artista:
            pintura.anuncio.precio += incremento
            print(f"Nuevo precio de {pintura.obra.titulo}: {pintura.anuncio.precio}")


incrementar_precio("Pablo Picasso", 10000)