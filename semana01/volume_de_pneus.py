# Desafios adicionais e melhorias: Ao pedir a largura, perfil e diâmetro do pneu, 
# é feito laços para receber valores padrões. Os valores padrões são sugeridos.

import math
from datetime import datetime

larguras_comuns = [165, 175, 185, 195, 205, 215, 225, 235, 245, 255]
perfis_comuns = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
diametros_comuns = [13, 14, 15, 16, 17, 18, 19, 20, 21]

largura = 0
perfil = 0
diametro = 0

while True:
    print(f"Larguras comuns: {larguras_comuns}")
    largura = int(input("Digite a largura do pneu em mm (por exemplo: 205): "))
    if largura in larguras_comuns:
        print()
        break

while True:
    print(f"Perfis Comuns: {perfis_comuns}")
    perfil = int(input("Digite o perfil do pneu (por exemplo: 60): "))
    if perfil in perfis_comuns:
        print()
        break

while True:
    print(f"Diâmetros Comuns: {diametros_comuns}")
    diametro = int(input("Digite o diâmetro da roda em polegadas (por exemplo: 15): "))
    if diametro in diametros_comuns:
        print()
        break

data_e_hora_atuais = datetime.now()
data_pura = data_e_hora_atuais.date()

volume = (math.pi * math.pow(largura, 2) * perfil * (largura * perfil + 2540 * diametro)) / math.pow(10, 10)

print(f"O volume aproximado é de {volume:.2f} litros")

with open("volumes.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{data_pura}, {largura}, {perfil}, {diametro}, {volume:.2f}\n")


