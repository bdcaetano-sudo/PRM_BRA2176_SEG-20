import random

caracter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
tamanho_senha = int(input("Digite o tamanho da senha desejada"))
senha = ''

for i in range(tamanho_senha):
    senha= senha + random.choice(caracter)

print(f'A senha gerada é {senha}')