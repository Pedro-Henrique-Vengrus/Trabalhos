class Funcionario:
    def __init__(self, nome, id_func, salario_base):
        self.nome = nome
        self.id_func = id_func
        self.salario_base = salario_base

    def calcular_bonus(self):
        return self.salario_base * 0.10

    def exibir_informacoes(self):
        print(f"Funcionário: {self.nome} (ID: {self.id_func})")
        print(f"Salário Base: R${self.salario_base:.2f}")
        print(f"Bônus: R${self.calcular_bonus():.2f}")
        print("-" * 40)


class Gerente(Funcionario):
    def __init__(self, nome, id_func, salario_base):
        super().__init__(nome, id_func, salario_base)

    def calcular_bonus(self):
        return self.salario_base * 0.20


fnc1 = Funcionario("MAgali", 101, 3000)
fnc2 = Funcionario("Cebolinha", 102, 2500)
g1 = Gerente("Douglas", 201, 8000)

fnc1.exibir_informacoes()
fnc2.exibir_informacoes()
g1.exibir_informacoes()
