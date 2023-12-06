from . import Animal

class Treinador(Animal):
    def __init__(self, nome, idade, sexo, EXP, equipe):
        super().__init__(nome)
        self.idade = idade
        self.sexo = sexo
        self.EXP = EXP
        self.equipe = equipe

    def __str__(self):
        return f'Nome: {self.nome:<10} Idade: {self.idade:<10} Sexo: {self.sexo}\nExperiencia: {self.EXP:<10} Equipe: {self.equipe}'