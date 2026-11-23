import csv



def main():
    INDICE_ID = 0
    INDICE_NOME = 1

    dic_estudantes = ler_dicionario("estudantes.csv", INDICE_ID)

    id_usuario = input("Por favor, digite um número de identificação (xx-xxx-xxxx): ")

    id_usuario = id_usuario.replace("-", "")

    if id_usuario not in dic_estudantes:
        print("Estudante inexistente")
    else:
        valor = dic_estudantes[id_usuario]
        nome = valor[INDICE_NOME]
        print(nome)

def ler_dicionario(nome_arquivo, indice_coluna_chave):
    dicionario = {}
    with open(nome_arquivo, "rt", encoding="utf-8") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        next(leitor)

        for linha in leitor:
            chave = linha[indice_coluna_chave]

            dicionario[chave] = linha

        return dicionario

if __name__ == "__main__":
    main()