nome = input("qual é seu email?: ")
codigo = int(input("qual o codigo secret?: "))

if nome == "admins" and codigo == 999:
    print("acesso ao servidor liberado. Sistema online.")
else:
    print("falha na autenticação. Alerta de segurança ligado!")