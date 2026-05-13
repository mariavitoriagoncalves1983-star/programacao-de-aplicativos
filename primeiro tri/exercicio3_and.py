nivel = int(input("fale teu nivel atual: "))
esferas = float(input("fale a quantidades de esferas coletadas: "))

if nivel >= 20 and esferas >= 50:
    print("habilidade super salto desbloqueado!")
elif nivel < 20 and esferas < 50:
    print("requisitos insuficientes para nova habilidade.")
elif nivel >= 20 and esferas < 50:
    print("requisitos insuicientes para nova habilidade.")
elif nivel < 20 and esferas >= 50:
    print("requisitos insufficientes para nova habilidade.")