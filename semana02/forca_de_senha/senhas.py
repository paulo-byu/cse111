#
#

MINUSCULAS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
MAIUSCULAS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITOS = ["0","1","2","3","4","5","6","7","8","9"]
ESPECIAIS = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

def procurar_palavra(palavra, nome_do_arquivo, maiusculas_e_minusculas = False):
    """
    Esta função lê um arquivo (informado pelo parâmetro nome_do_arquivo), em que cada linha contém uma única palavra.
    Se a palavra passada no parâmetro palavra corresponder a uma palavra no arquivo, a função retornará True; caso contrário, retornará False.
    Se o parâmetro maiusculas_e_minusculas for True, a comparação será feita com distinção entre maiúsculas e minúsculas.
    Se for False, a comparação será feita sem distinção entre maiúsculas e minúsculas (comportamento padrão).
    Por padrão, o parâmetro maiusculas_e_minusculas deve ser False.
    Parâmetros: palavra, nome_do_arquivo, maiusculas_e_minusculas
    Tipo de Retorno: Booleano (True ou False)
    """    
    with open(nome_do_arquivo, 'r', encoding='utf-8') as palavras_arquivo:
        for linha in palavras_arquivo:
            palavra_linha = linha.strip()
            if maiusculas_e_minusculas == True:
                if palavra == palavra_linha:
                    return True
            else:
                if palavra.lower() == palavra_linha.lower():
                    return True
    return False

def palavra_tem_caractere(palavra, lista_caracteres):
    """
    Esta função percorre cada caractere da string passada no parâmetro palavra para verificar se ele está presente na lista de caracteres informada no parâmetro lista_caracteres.
    Se algum caractere da palavra estiver na lista de caracteres, a função retornará True.
    Se nenhum caractere da palavra estiver na lista, a função retornará False.
    Parâmetros: palavra, lista_caracteres
    Tipo de Retorno: Booleano (True ou False)
    """
    for letra in palavra:
        for caracter in lista_caracteres:
            if letra == caracter:
                return True
    return False

def calcular_complexidade(palavra):
    """
    Esta função cria um valor numérico que representa a complexidade da senha com base nos tipos de caracteres que o parâmetro palavra contém.
    Um ponto de complexidade é atribuído para cada tipo de caractere presente na palavra.
    A função chama palavra_tem_caractere para verificar cada um dos quatro tipos de caracteres: Minúscula, Maiúscula, Dígitos e Especial.
    Se a palavra contiver esse tipo de caractere, um ponto será adicionado à classificação de complexidade. Como existem quatro tipos de caracteres, a classificação de complexidade variará de 0 a 4.
    O valor 0 será retornado apenas se a palavra estiver vazia ou contiver apenas caracteres que não pertençam a nenhuma das listas acima.
    Parâmetros: palavra
    Tipo de Retorno: Inteiro
    """
    contador = 0
    tem_minuscula = palavra_tem_caractere(palavra, MINUSCULAS)
    if tem_minuscula:
        contador += 1
    tem_maiuscula = palavra_tem_caractere(palavra, MAIUSCULAS)
    if tem_maiuscula:
        contador += 1
    tem_digito = palavra_tem_caractere(palavra, DIGITOS)
    if tem_digito:
        contador += 1
    tem_especial = palavra_tem_caractere(palavra, ESPECIAIS)
    if tem_especial:
        contador += 1
    return contador

def validar_senha(senha, comprimento_min = 10, comprimento_forte = 16):
    """
    A função validar_senha verifica os requisitos de comprimento, chama calcular_complexidade para calcular a complexidade da senha e então determina a força final com base nos requisitos do usuário.
    Ela deve exibir as mensagens definidas nos requisitos e retornar a força da senha como um número de 0 a 5.
    O parâmetro comprimento_min deve ter um valor padrão de 10. O parâmetro comprimento_forte deve ter um valor padrão de 16.
    Parâmetros: senha, comprimento_min, comprimento_forte
    Tipo de Retorno: Inteiro
    """
    palavra_no_dicionario = procurar_palavra(senha,"dicionario.txt")
    if palavra_no_dicionario:
        print("A senha está no dicionário e não é segura.")
        return 0
    senhas_comuns = procurar_palavra(senha,"senhas_mais_comuns.txt",True)
    if senhas_comuns:
        print("A senha é comumente usada e não é segura.")
        return 0
    tamanho_palavra = len(senha)
    if tamanho_palavra < comprimento_min:
        print("A senha é muito curta e não é segura.")
        return 1
    elif tamanho_palavra >= comprimento_forte:
        print("A senha é longa, o compprimento supera a complexidade e é uma boa senha.")
        return 5
    complexidade = calcular_complexidade(senha)
    return complexidade + 1

def main():
    """
    Fornece o loop de entrada do usuário. O loop solicita ao usuário uma senha para teste.
    Se a senha for qualquer coisa diferente de "q" ou "Q", chame a função validar_senha e informe os resultados ao usuário.
    Se o usuário digitar "q" ou "Q", sai do programa.
    """
    while True:
        senha = input("Por favor, digite a senha: ")
        if senha == "Q" or senha == "q":
            break
        else:
            forca_senha = validar_senha(senha)
            print(f"Força: {forca_senha}")

if __name__ == "__main__":
    main()