class Auto:
    marca = "Ford"

    def __init__(self, modelo: str):
        self.modelo = modelo
        self.acelerando = False

    def acelerar(self, valor: bool) -> None:
        self.acelerando = valor

class AutoInverso(Auto):
    def __init__(self, modelo: str):
        super().__init__(modelo)

    def acelerar(self, valor: bool):
        print(super().acelerar(not valor))

print(Auto.marca)
auto = Auto("Focus")
print(auto.modelo)
print(auto.marca)


print(id(Auto.marca))
print(id(auto.marca))

auto2 = Auto("Fiesta")

print(id(auto.modelo))
print(id(auto2.modelo))
print(id(auto2.marca))


auto = AutoInverso('Fiesta')
print(auto.acelerando)
auto.acelerar(False)
print(auto.acelerando)
