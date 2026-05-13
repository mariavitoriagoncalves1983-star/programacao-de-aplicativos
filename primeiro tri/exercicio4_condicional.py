temperatura = float(input("qual a temperatura atual?: "))

if temperatura >= 80:
    print("PERIGO! desligando servidor por aquecimento!")
elif temperatura >= 50:
    print("Alerta: ventoinhas ligadas no máximo!")
elif temperatura < 50:
    print("temperatura estável! sistema operando normalmente!")