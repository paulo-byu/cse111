import csv


def ler_dicionario(nome_arquivo, indice_coluna_chave):
    """
    Parâmetros filename, indice_coluna_chave
    Tipo de Retorno: Dicionário
    A função retorna um dicionário de produtos.
    """
    dicionario = {}
    with open(nome_arquivo, "rt", encoding="utf-8") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        next(leitor)

        for linha in leitor:
            chave = linha[indice_coluna_chave]

            dicionario[chave] = linha

        return dicionario

def main():
    INDICE_ID = 0
    INDICE_NOME = 1
    INDICE_PRECO = 2
    INDICE_QUANTIDADE = 1
    dic_produtos = ler_dicionario("produtos.csv", INDICE_ID)

    print("Todos os Produtos")
    print(dic_produtos)

    print("Itens Pedidos")
    with open("pedido.csv", "rt", encoding="utf-8") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        next(leitor)
    
        for linha in leitor:
            id_produto = linha[INDICE_ID]
            produto = dic_produtos[id_produto]
            nome_produto = produto[INDICE_NOME]
            preco_produto = float(produto[INDICE_PRECO])
            quantidade_produto = int(linha[INDICE_QUANTIDADE])
            print(f"{nome_produto}: {quantidade_produto} @ {preco_produto}")

    


if __name__ == "__main__":
    main()