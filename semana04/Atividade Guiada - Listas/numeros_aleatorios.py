import random

def main():
    numeros = [16.2, 75.1, 52.3]
    print(f"Números {numeros}")

    anexar_numeros_aleatorios(numeros)
    print(f"Números: {numeros}")

    anexar_numeros_aleatorios(numeros, 5)
    print(f"Números: {numeros}")

    lista_palavras = []

    anexar_palavras_aleatorias(lista_palavras)
    print(f"Palavras: {lista_palavras}")

    anexar_palavras_aleatorias(lista_palavras, 3)
    print(f"Palavras: {lista_palavras}")


def anexar_numeros_aleatorios(lista_numeros, quantidade=1):
    for _ in range(quantidade):
        numero_aleatorio = random.uniform(0, 100)
        arredondado = round(numero_aleatorio, 1)
        lista_numeros.append(arredondado)

def anexar_palavras_aleatorias(lista_palavras, quantidade=1):
    candidatas = ["banana", "abacaxi", "maça", "carro", "robô", "carreta", "sol", "lua", "estrela"]

    for _ in range(quantidade):
        palavra = random.choice(candidatas)
        lista_palavras.append(palavra)

if __name__ == "__main__":
    main()

