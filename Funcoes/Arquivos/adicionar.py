import os

caminho = os.path.dirname(__file__) + '\\pokedex.csv'

def adicionarPokemon(pokemon):
    with open(caminho, 'a', encoding='utf-8') as arquivo:

        linha = pokemon.nome + ';' + str(pokemon.get_NPokedex()) + ';' + str(pokemon.get_HPTotal()) + ';' + str(pokemon.get_HPAtual()) + ';' + str(pokemon.get_Iniciativa()) + ';' + pokemon.tipo1 + ';' + pokemon.tipo2 + ';' + pokemon.nome_ataque1 + ';' + str(pokemon.valor_ataque1) + ';' + pokemon.nome_ataque2 + ';' + str(pokemon.valor_ataque2)
        arquivo.write(linha + '\n')
    
def lerPokedex():

    pokedexL = []

    with open(caminho, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            pokemon = linha.split(';')
            
            pokedex = {}

            pokedex['Nome'] = pokemon[0]
            pokedex['Número Pokedex'] = pokemon[1]
            pokedex['Iniciativa'] = pokemon[4]
            pokedex['HP total'] = pokemon[2]
            pokedex['HP atual'] = pokemon[3]
            pokedex['Tipo 1'] = pokemon[5]
            pokedex['Tipo 2'] = pokemon[6]
            pokedex['Nome do ataque 1'] = pokemon[7]
            pokedex['Valor do ataque 1'] = pokemon[8]
            pokedex['Nome do ataque 2'] = pokemon[9]
            pokedex['Valor do ataque 2'] = pokemon[10]
        
            pokedexL.append(pokedex)
        
        return pokedexL
    
def atualizarHP(pokemons, vindo):
    with open(caminho, 'r+', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

        for i, linha in enumerate(linhas):
            pokemon = linha.split(';')
            if int(pokemon[1]) == int(pokemons['Número Pokedex']):
                if vindo == 'batalha':
                    pokemon[3] = str(pokemons['HP atual'])
                    linhas[i] = ';'.join(pokemon)
                elif vindo == 'curar':
                    pokemon[3] = str(pokemons['HP total'])
                    linhas[i] = ';'.join(pokemon)

        arquivo.seek(0)
        arquivo.writelines(linhas)
        arquivo.truncate()
