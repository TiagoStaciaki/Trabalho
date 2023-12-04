from . import Animal

class Treinador(Animal):
    def __init__(self, nome, idade, sexo, EXP):
        super().__init__(nome)
        self.idade = idade
        self.sexo = sexo
        self.EXP = EXP

    def __str__(self):
        return f'Nome: {self.nome:<10} Idade: {self.idade:<10} Sexo: {self.sexo:<10} Experiencia: {self.EXP}'