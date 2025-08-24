class Bolacha:
    def __init__(self, marca, sabor, preco):
        self.marca = marca
        self.sabor = sabor
        self.preco = preco
    def imprima(self):
        print(f"Marca: {self.marca} \n Sabor: {self.sabor} \n preço: {self.preco}")