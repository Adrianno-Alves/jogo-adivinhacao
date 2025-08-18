import random

def jogo():
    print("🎲 Bem-vindo ao jogo da Adivinhação 🎲")
    print("O computador vai pensar em um número entre 1 e 100...")

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            acertou = True
        elif palpite < numero_secreto:
            print("O número é MAIOR. Tente novamente!")
        else:
            print("O número é MENOR. Tente novamente!")

if __name__ == "__main__":
    jogo()
