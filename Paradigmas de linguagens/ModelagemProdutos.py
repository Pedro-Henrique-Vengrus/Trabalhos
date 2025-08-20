class Produto:
    def __init__(self, nome, preco_unitario, quantidade):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade

    def exibir_detalhes(self):
        print(f"Produto: {self.nome}")
        print(f"Preço Unitário: R${self.preco_unitario:.2f}")
        print(f"Quantidade em Estoque: {self.quantidade}")
        print(f"Valor Total em Estoque: R${self.calcular_valor_total():.2f}")
        print("-" * 40)

    def calcular_valor_total(self):
        return self.preco_unitario * self.quantidade


pdt1 = Produto("Notebook", 2000.00, 5)
pdt2 = Produto("Mouse", 20.00, 20)
pdt3 = Produto("Teclado", 80.00, 15)

pdt1.exibir_detalhes()
pdt2.exibir_detalhes()
pdt3.exibir_detalhes()
