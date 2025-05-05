menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair
=> """

# Função de depósito (positional only)
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função de saque (keyword only)
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

# Função extrato (positional and keyword only)
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")

# Função para criar um usuário
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

# Função para criar conta bancária
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado. Conta não criada.")

# Função para listar contas
def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência: {conta['agencia']}
        Conta: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print(linha)

# Função para buscar usuário pelo CPF
def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

# --------- INICIALIZAÇÃO DO SISTEMA ---------
AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
contador_contas = 1

# Criando 3 usuários fictícios
usuarios.append({
    "nome": "Maria Silva",
    "data_nascimento": "10-01-1990",
    "cpf": "12345678901",
    "endereco": "Rua das Flores, 10 - Centro - Curitiba/PR"
})
usuarios.append({
    "nome": "João Souza",
    "data_nascimento": "22-05-1985",
    "cpf": "98765432100",
    "endereco": "Av. Brasil, 200 - Jardim - São Paulo/SP"
})
usuarios.append({
    "nome": "Ana Lima",
    "data_nascimento": "15-08-1995",
    "cpf": "11122233344",
    "endereco": "Rua da Paz, 50 - Bairro Novo - Recife/PE"
})

# Criando contas fictícias
contas.append({"agencia": AGENCIA, "numero_conta": 1, "usuario": usuarios[0]})
contas.append({"agencia": AGENCIA, "numero_conta": 2, "usuario": usuarios[1]})
contas.append({"agencia": AGENCIA, "numero_conta": 3, "usuario": usuarios[2]})
contador_contas = 4

# ------------- LOOP PRINCIPAL ----------------
while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "nc":
        conta = criar_conta(AGENCIA, contador_contas, usuarios)
        if conta:
            contas.append(conta)
            contador_contas += 1

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "q":
        print("Saindo... Obrigado por usar nosso banco!")
        break

    else:
        print("Operação inválida, por favor selecione novamente.")
