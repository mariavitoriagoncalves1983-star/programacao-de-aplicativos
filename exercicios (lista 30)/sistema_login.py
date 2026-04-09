secreta = ["12345"]
tentativas = 0
acertou = False 

while tentativas < 3 and not acertou:
    palpite = input("digite uma senha: ")
    
    if palpite in secreta:
        print("Parabéns, você acertou!")
        acertou = True
    else:
        print("Errou!")
    
    tentativas += 1
if not acertou:
    print("Acesoo bloqueado.")
    print("A senha era:", secreta)