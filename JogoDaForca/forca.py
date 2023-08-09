import random
from forca_palavras import lista_palavras
from forca_art import logo, estagio

palavra_escolhida = random.choice(lista_palavras)
palavra_lenght = len(palavra_escolhida)

fim_do_jogo = False
vidas = 6

print(logo)

# Testar o código
# print(f'AEEE, a solução é {palavra_escolhida}.')

# Criando os espaços em branco
display = []
for _ in range(palavra_lenght):
    display += "_"

while not fim_do_jogo:
    palpite = input("Advinhe uma letra: ").lower()

    # Checando a letra escolhida
    for position in range(palavra_lenght):
        letra = palavra_escolhida[position]
        if letra == palpite:
            display[position] = letra
            print(f"A letra '{palpite}' está na palavra.\nVocê acertou.")

    # Checar se o usuário errou
    if palpite not in palavra_escolhida:
        print(f"A letra '{palpite}' não está na palavra.\nVocê perdeu uma vida.")
        
        vidas -= 1
        if vidas == 0:
            fim_do_jogo = True
            print("Você Perdeu.")

    # Junta todos os elementos da lista e transforma em uma String.
    print(f"{' '.join(display)}")

    # Checa se o usuário acertou todas as letras
    if "_" not in display:
        fim_do_jogo = True
        print("Voce Venceu.")

    print(estagio[vidas])
