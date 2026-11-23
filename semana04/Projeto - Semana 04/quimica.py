# Desafio Adicional: Criada uma função (composicao_percentual) que calcula e apresenta a 
# composição percentual de cada elemento na massa molar total.

from formula import interpretar_formula

INDICE_SIMBOLO_DO_ELEMENTO=0
INDICE_QUANTIDADE_DE_ATOMOS=1
INDICE_MASSA_ATOMICA=1
INDICE_NOME_ELEMENTO=0

def  criar_tabela_periodica():
    """
    Parâmetros: (nenhum)
    Retorna: Dicionário
    Retorna um objeto de dicionário com todos os elementos da tabela periódica.
    Para cada elemento, a chave do dicionário deve ser o símbolo do elemento.
    O valor contém uma lista em que o primeiro item é o nome do elemento e o segundo é a massa atômica.
    """
    dic_da_tabela_periodica = {
    # símbolo: [nome, massa_atomica]
    "Ac": ["Actínio", 227],
    "Ag": ["Prata", 107.8682],
    "Al": ["Alumínio", 26.9815386],
    "Ar": ["Argônio", 39.948],
    "As": ["Arsênio", 74.9216],
    "At": ["Astato", 210],
    "Au": ["Ouro", 196.966569],
    "B": ["Boro", 10.811],
    "Ba": ["Bário", 137.327],
    "Be": ["Berílio", 9.012182],
    "Bi": ["Bismuto", 208.9804],
    "Br": ["Bromo", 79.904],
    "C": ["Carbono", 12.0107],
    "Ca": ["Cálcio", 40.078],
    "Cd": ["Cádmio", 112.411],
    "Ce": ["Cério", 140.116],
    "Cl": ["Cloro", 35.453],
    "Co": ["Cobalto", 58.933195],
    "Cr": ["Crômio", 51.9961],
    "Cs": ["Césio", 132.9054519],
    "Cu": ["Cobre", 63.546],
    "Dy": ["Disprósio", 162.5],
    "Er": ["Érbio", 167.259],
    "Eu": ["Európio", 151.964],
    "F": ["Flúor", 18.9984032],
    "Fe": ["Ferro", 55.845],
    "Fr": ["Frâncio", 223],
    "Ga": ["Gálio", 69.723],
    "Gd": ["Gadolínio", 157.25],
    "Ge": ["Germânio", 72.64],
    "H": ["Hidrogênio", 1.00794],
    "He": ["Hélio", 4.002602],
    "Hf": ["Háfnio", 178.49],
    "Hg": ["Mercúrio", 200.59],
    "Ho": ["Hólmio", 164.93032],
    "I": ["Iodo", 126.90447],
    "In": ["Índio", 114.818],
    "Ir": ["Irídio", 192.217],
    "K": ["Potássio", 39.0983],
    "Kr": ["Kriptônio", 83.798],
    "La": ["Lantânio", 138.90547],
    "Li": ["Lítio", 6.941],
    "Lu": ["Lutécio", 174.9668],
    "Mg": ["Magnésio", 24.305],
    "Mn": ["Manganês", 54.938045],
    "Mo": ["Molibdênio", 95.96],
    "N": ["Nitrogênio", 14.0067],
    "Na": ["Sódio", 22.98976928],
    "Nb": ["Nióbio", 92.90638],
    "Nd": ["Neodímio", 144.242],
    "Ne": ["Neônio", 20.1797],
    "Ni": ["Níquel", 58.6934],
    "Np": ["Neptúnio", 237],
    "O": ["Oxigênio", 15.9994],
    "Os": ["Ósmio", 190.23],
    "P": ["Fósforo", 30.973762],
    "Pa": ["Protactínio", 231.03588],
    "Pb": ["Chumbo", 207.2],
    "Pd": ["Paládio", 106.42],
    "Pm": ["Promécio", 145],
    "Po": ["Polônio", 209],
    "Pr": ["Praseodímio", 140.90765],
    "Pt": ["Platina", 195.084],
    "Pu": ["Plutônio", 244],
    "Ra": ["Rádio", 226],
    "Rb": ["Rubídio", 85.4678],
    "Re": ["Rênio", 186.207],
    "Rh": ["Ródio", 102.9055],
    "Rn": ["Radônio", 222],
    "Ru": ["Rutênio", 101.07],
    "S": ["Enxofre", 32.065],
    "Sb": ["Antimônio", 121.76],
    "Sc": ["Escândio", 44.955912],
    "Se": ["Selênio", 78.96],
    "Si": ["Silício", 28.0855],
    "Sm": ["Samário", 150.36],
    "Sn": ["Estanho", 118.71],
    "Sr": ["Estrôncio", 87.62],
    "Ta": ["Tântalo", 180.94788],
    "Tb": ["Térbio", 158.92535],
    "Tc": ["Tecnécio", 98],
    "Te": ["Telúrio", 127.6],
    "Th": ["Tório", 232.03806],
    "Ti": ["Titânio", 47.867],
    "Tl": ["Tálio", 204.3833],
    "Tm": ["Túlio", 168.93421],
    "U": ["Urânio", 238.02891],
    "V": ["Vanádio", 50.9415],
    "W": ["Tungstênio", 183.84],
    "Xe": ["Xenônio", 131.293],
    "Y": ["Ítrio", 88.90585],
    "Yb": ["Itérbio", 173.054],
    "Zn": ["Zinco", 65.38],
    "Zr": ["Zircônio", 91.224]
    }
    return dic_da_tabela_periodica

def calcular_massa_molar(lista_quantidade_simbolos, dic_da_tabela_periodica):
    """
    Parâmetros: lista_quantidade_simbolos, dic_da_tabela_periodica
    Retorna: float
    Calcule e retorne a massa molar total de todos os elementos listados em lista_quantidade_simbolos.
    Percorra os itens na lista_quantidade_simbolos utilizando um loop.
    Para cada item na lista, use o símbolo do elemento para procurar a massa atômica do elemento no dicionário dic_da_tabela_periodica.
    Multiplique a massa atômica do elemento pela quantidade de átomos do elemento (da lista_quantidade_simbolos) e adicione isso à massa total.
    Retorne a massa total.
    """
    massa_molar_total = 0
    for simbolo in lista_quantidade_simbolos:
        if simbolo[INDICE_SIMBOLO_DO_ELEMENTO] in dic_da_tabela_periodica:
            elemento = dic_da_tabela_periodica[simbolo[INDICE_SIMBOLO_DO_ELEMENTO]]
            massa_atomica = elemento[INDICE_MASSA_ATOMICA]
        massa_molar_total += massa_atomica * simbolo[INDICE_QUANTIDADE_DE_ATOMOS]
    return massa_molar_total

def composicao_percentual(massa_molar_total, lista_quantidade_simbolos, dic_da_tabela_periodica):
    """
    Parâmetros: massa_molar_total, lista_quantidade_simbolos, dic_da_tabela_periodica
    Retorna: (nenhum)
    Calcula e apresenta a composição percentual de cada elemento na massa molar total. 
    """
    for simbolo in lista_quantidade_simbolos:
        if simbolo[INDICE_SIMBOLO_DO_ELEMENTO] in dic_da_tabela_periodica:
            elemento = dic_da_tabela_periodica[simbolo[INDICE_SIMBOLO_DO_ELEMENTO]]
            massa_atomica = elemento[INDICE_MASSA_ATOMICA]
            nome_elemento = elemento[INDICE_NOME_ELEMENTO]
            composicao = (massa_atomica * simbolo[INDICE_QUANTIDADE_DE_ATOMOS]) / massa_molar_total * 100
        print(f"{nome_elemento} --> {composicao:.2f}%")

def main():
    """
    Parâmetros: (nenhum)
    Retorna: (nenhum)
    Solicita ao usuário uma fórmula química.
    Solicita ao usuário o tamanho da amostra em gramas.
    Chama criar_tabela_periodica para obter uma lista de elementos na fórmula.
    Chama a função interpretar_formula e armazena o dicionário retornado na variável.
    Chama calcular_massa_molar para calcular a massa molar. Passa o dicionário da tabela periódica e a lista de elementos retornados das funções anteriores.
    Exibe a massa molar.
    Calcula o número de mols na amostra.
    Exibe o número de mols.
    """
    formula_amostra = input("Insira a fórmula molecular da amostra: ").upper()
    massa_amostra = float(input("Insira a massa em gramas da amostra: "))
    dic_da_tabela_periodica = criar_tabela_periodica()
    lista_quantidade_simbolos = interpretar_formula(formula_amostra, dic_da_tabela_periodica)
    massa_molar_total = calcular_massa_molar(lista_quantidade_simbolos, dic_da_tabela_periodica)
    print(f"{massa_molar_total:.5f} gramas/mol")
    numero_de_mols = massa_amostra / massa_molar_total
    print(f"{numero_de_mols:.5f} mols")
    print("-------------- Composição Percentual --------------")
    composicao_percentual(massa_molar_total, lista_quantidade_simbolos, dic_da_tabela_periodica)

if __name__ == "__main__":
  main()

