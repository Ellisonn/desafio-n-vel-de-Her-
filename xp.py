# Variável para armazenar os heróis e suas experiências (XP)
herois = [
    {"nome": "gilball 1", "xp": 950},
    {"nome": "treck 2", "xp": 1500},
    {"nome": "digterd 3", "xp": 3200},
    {"nome": "madrog 4", "xp": 6000},
    {"nome": "ludigaar 5", "xp": 7200},
    {"nome": "diirk 6", "xp": 8500},
    {"nome": "nordfek 7", "xp": 9500},
    {"nome": "teckdir 8", "xp": 10500}
]

# Função para determinar a classificação com base no XP
def classificar_heroi(xp):
    if xp < 1000:
        return "Ferro"
    elif 1001 <= xp <= 2000:
        return "Bronze"
    elif 2001 <= xp <= 5000:
        return "Prata"
    elif 5001 <= xp <= 7000:
        return "Ouro"
    elif 7001 <= xp <= 8000:
        return "Platina"
    elif 8001 <= xp <= 9000:
        return "Ascendente"
    elif 9001 <= xp <= 10000:
        return "Imortal"
    else:
        return "Radiante"

# Função para salvar as informações no arquivo de texto
def salvar_informacoes(herois):
    with open("herois.txt", "w") as file:
        for heroi in herois:
            nome = heroi["nome"]
            xp = heroi["xp"]
            classificacao = classificar_heroi(xp)
            file.write(f"Nome: {nome}\n")
            file.write(f"XP: {xp}\n")
            file.write(f"Classificação: {classificacao}\n")
            file.write("="*40 + "\n")

# Chamar a função para salvar as informações
salvar_informacoes(herois)

print("As informações dos heróis foram salvas no arquivo 'herois.txt'.")
