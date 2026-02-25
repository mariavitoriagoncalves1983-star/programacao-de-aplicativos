poder_de_ataque = int(input("digite o teu pode de ataque "))
poder_de_defesa_do_vilao = int(input("digite os pontos de defesa do vilao "))

dano = poder_de_ataque - poder_de_defesa_do_vilao
if dano <= 0:
    print("o vilao bloqueou o ataque! Dano: 0")
elif dano > 0:
    print("ataque critico! voce causou dano ao vilao de ", dano)