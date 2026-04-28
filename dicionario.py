meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "AURA" : "A energia interna do corpo"
            "BOT" : 
            "NUB" : 
            }
word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")
if word in meme_dict.keys():
    # O que devemos fazer se a palavra for encontrada?
    print(meme_dict[word])
else:
    # O que devemos fazer se a palavra não for encontrada?
    print("Essa palavra ainda não está no dicionário")
