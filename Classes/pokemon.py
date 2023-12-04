from . import Animal

class Pokemon(Animal):
    def __init__(self, nome, N_pokedex, HP_Total, HP_Atual, iniciativa, tipo1, tipo2, nome_ataque1, valor_ataque1, nome_ataque2, valor_ataque2):
        super().__init__(nome)
        self.__N_pokedex = N_pokedex
        self.__HP_Total = HP_Total
        self.__HP_Atual = HP_Atual
        self.__iniciativa = iniciativa
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.nome_ataque1 = nome_ataque1
        self.valor_ataque1 = valor_ataque1
        self.nome_ataque2 = nome_ataque2
        self.valor_ataque2 = valor_ataque2

    def get_HPTotal(self):
        return self.__HP_Total
    
    def get_HPAtual(self):
        return self.__HP_Atual
    
    def get_Iniciativa(self):
        return self.__iniciativa
    
    def get_NPokedex(self):
        return self.__N_pokedex
    
    def set_HPTotal(self, HPTotal):
        self.__HP_Total = HPTotal

    def set_HPAtual(self, HPAtual):
        self.__HP_Atual = HPAtual

    def set_iniciativa(self, iniciativa):
        self.__iniciativa = iniciativa
    
    def set_NPokedex(self, N_pokedex):
        self.__N_pokedex = N_pokedex
    
    def __str__(self):
        return f'Nome: {self.nome:<10} Número pokedex: {self.get_NPokedex():<10} Iniciativa: {self.get_Iniciativa():<10} \nHP total: {self.get_HPTotal():<10} HP atual: {self.get_HPAtual():<10} \nTipo 1: {self.tipo1:<10} Tipo 2: {self.tipo2:<10}\nNome do ataque 1: {self.nome_ataque1:<10} Valor do ataque 1: {self.valor_ataque1:<10}\nNome do ataque 2: {self.nome_ataque2:<10} Valor do ataque 2: {self.valor_ataque2}'