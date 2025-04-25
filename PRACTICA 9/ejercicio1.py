class Boletos:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio

class BoletoPalco(Boletos):
    def __init__(self, numero, precio):
        super().__init__(numero, precio)

class BoletoPlatea(Boletos):
    def __init__(self, numero, precio):
        super().__init__(numero, precio)

class BoletoGaleria(Boletos):
    def __init__(self, numero, precio):
        super().__init__(numero, precio)


def main():
    boleto1 = BoletoPalco(1, 150.0)
    boleto2 = BoletoPlatea(2, 100.0)
    boleto3 = BoletoGaleria(3, 25.0)

    print(f"Boleto Palco: Número {boleto1.numero}, Precio: {boleto1.precio}")
    print(f"Boleto Platea: Número {boleto2.numero}, Precio: {boleto2.precio}")
    print(f"Boleto Galería: Número {boleto3.numero}, Precio: {boleto3.precio}")

if __name__ == "__main__":
    main()