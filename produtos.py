class Bolacha:
    def __init__(self, marca, sabor, preco):
        self.marca = marca
        self.sabor = sabor
        self.preco = preco
    def imprima(self):
        print(f"Marca: {self.marca} \n Sabor: {self.sabor} \n preço: {self.preco}")

class Salgados(Bolacha):
    def __init__(self, marca, sabor, preco, tipo):
        # Chama o construtor da classe pai
        super().__init__(marca, sabor, preco)
        self.tipo = tipo  # atributo novo só da classe Salgos

    # Pode usar os métodos herdados ou sobrescrever
    def imprima(self):
        super().imprima()  # reaproveita o da classe Bolacha
        print(f"Tipo: {self.tipo}")