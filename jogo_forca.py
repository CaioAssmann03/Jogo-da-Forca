"""
Jogo da Forca (Hangman) - Terminal
Jogo clássico onde o jogador tenta adivinhar uma palavra secreta
letra por letra, com um número limitado de tentativas.
"""

import random

PALAVRAS = [
    "python", "programacao", "computador", "internet", "desenvolvedor",
    "algoritmo", "variavel", "funcao", "biblioteca", "terminal",
]

DESENHOS_FORCA = [
    """
       -----
       |   |
       |
       |
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |   |
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |  /|
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |  /|\\
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |  /|\\
       |  /
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |  /|\\
       |  / \\
       |
    ---------
    """,
]

TENTATIVAS_MAXIMAS = len(DESENHOS_FORCA) - 1


def escolher_palavra():
    return random.choice(PALAVRAS).upper()


def mostrar_palavra_oculta(palavra, letras_corretas):
    return " ".join(letra if letra in letras_corretas else "_" for letra in palavra)


def jogar():
    palavra = escolher_palavra()
    letras_corretas = set()
    letras_erradas = set()
    tentativas_restantes = TENTATIVAS_MAXIMAS

    print("\n===== JOGO DA FORCA =====")
    print(f"A palavra tem {len(palavra)} letras. Você tem {TENTATIVAS_MAXIMAS} tentativas.\n")

    while tentativas_restantes > 0:
        erros = TENTATIVAS_MAXIMAS - tentativas_restantes
        print(DESENHOS_FORCA[erros])
        print("Palavra:", mostrar_palavra_oculta(palavra, letras_corretas))
        print("Letras erradas:", ", ".join(sorted(letras_erradas)) if letras_erradas else "nenhuma")

        if all(letra in letras_corretas for letra in palavra):
            print(f"\n🎉 Parabéns, você venceu! A palavra era: {palavra}\n")
            return

        chute = input("\nDigite uma letra: ").strip().upper()

        if len(chute) != 1 or not chute.isalpha():
            print("Digite apenas uma letra válida.\n")
            continue

        if chute in letras_corretas or chute in letras_erradas:
            print("Você já tentou essa letra.\n")
            continue

        if chute in palavra:
            letras_corretas.add(chute)
            print("✅ Letra correta!\n")
        else:
            letras_erradas.add(chute)
            tentativas_restantes -= 1
            print("❌ Letra errada!\n")

    print(DESENHOS_FORCA[TENTATIVAS_MAXIMAS])
    print(f"💀 Você perdeu! A palavra era: {palavra}\n")


if __name__ == "__main__":
    while True:
        jogar()
        continuar = input("Jogar novamente? (s/n): ").strip().lower()
        if continuar != "s":
            print("Até logo!")
            break
