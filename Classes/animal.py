class Animal:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f'Nome: {self.nome:<10}'