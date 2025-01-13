import random

def advinha():
    tentativa = 1
    
    while True:
        chute = int(input("Digite um número: "))
        if chute >= 0 or chute <= 100:
            if chute == num_advinhar:
                tentativa += 1
                break
            elif chute < num_advinhar:
                print("O número é maior!")
                tentativa += 1
            else:
                print("O número é menor!")
                tentativa += 1
        else:
            print("Valor inválido! Tente novamente.")

    print(f"Acertou o número {num_advinhar} em {tentativa} tentativas!")


print("Tente adivinhar o número gerado entre 0 e 100")

num_advinhar = random.randint(0,100)
# print(num_advinhar)
advinha()