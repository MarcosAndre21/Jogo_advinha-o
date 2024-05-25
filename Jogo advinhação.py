import random

def jogar_adivinhacao():
    numero_secreto = random.randint(1,100)
    tentativas = 0
    acertou = False

    print(" Seja Bem-vindo ao nosso jogo de adivinhação") 
    print("Hmmmmm!! Estou pensando em um número de 1 a 100. Que número acha que é?")

    while not acertou:
        try:
            chute = int(input("Digite seu palpite: "))
            tentativas+=1
            
            if chute < 1 or chute > 100:
                print("Por Favor, digite um número entre 1 e 100.")
            elif chute < numero_secreto:
                print("número muito baixo! Tente novamente!")
            elif chute > numero_secreto:
                print("numero muito alto! Tente novamente!")
            else: 
                print(f"Parabéns, você acertou o número secreto é {numero_secreto} em {tentativas}! ")
                acertou=True
        except ValueError:
            print("Digite um número válido! O número deve ser inteiro!")   
def main():
    jogar_novamente = True
    while jogar_novamente:
        jogar_adivinhacao()
        resposta = input ("Você gostaria de jogar novamente? [s/n]: ") 
        if resposta != "s": 
            jogar_novamente = False
            print("obrigado por jogar, até a proxima!")
if __name__ == "__main__":
    main()
