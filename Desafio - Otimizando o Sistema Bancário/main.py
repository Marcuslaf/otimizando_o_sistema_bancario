import textwrap

def exibir_mensagem(titulo: str, mensagem: str) -> None:
    print(f"\n================ {titulo} ================")
    print(mensagem)
    print("==========================================")

def depositar(contas: list, cpf: str, valor: float) -> None:
    if valor <= 0:
        exibir_mensagem("ERRO", "Operação falhou! O valor informado é inválido.")
        return
    
    conta_encontrada = None
    for conta in contas:
        if conta['usuario']['cpf'] == cpf:
            conta_encontrada = conta
            break
    
    if not conta_encontrada:
        exibir_mensagem("ERRO", "Conta não encontrada para o CPF informado.")
        return
    
    conta_encontrada['saldo'] += valor
    conta_encontrada['extrato'].append(f"Depósito: R$ {valor:.2f}")
    exibir_mensagem("DEPÓSITO", f"Depósito de R$ {valor:.2f} realizado com sucesso na conta {conta_encontrada['numero_conta']}!")

def sacar(contas: list, cpf: str, valor: float, limite: float, limite_saques: int) -> None:
    conta_encontrada = None
    for conta in contas:
        if conta['usuario']['cpf'] == cpf:
            conta_encontrada = conta
            break
    
    if not conta_encontrada:
        exibir_mensagem("ERRO", "Conta não encontrada para o CPF informado.")
        return
    
    if valor > conta_encontrada['saldo']:
        exibir_mensagem("ERRO", "Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        exibir_mensagem("ERRO", "Operação falhou! O valor do saque excede o limite.")
    elif conta_encontrada['numero_saques'] >= limite_saques:
        exibir_mensagem("ERRO", "Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta_encontrada['saldo'] -= valor
        conta_encontrada['extrato'].append(f"Saque: R$ {valor:.2f}")
        conta_encontrada['numero_saques'] += 1
        exibir_mensagem("SAQUE", f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        exibir_mensagem("ERRO", "Operação falhou! O valor informado é inválido.")

def exibir_extrato(contas: list, cpf: str) -> None:
    conta_encontrada = None
    for conta in contas:
        if conta['usuario']['cpf'] == cpf:
            conta_encontrada = conta
            break
    
    if not conta_encontrada:
        exibir_mensagem("ERRO", "Conta não encontrada para o CPF informado.")
        return
    
    extrato_texto = "\n".join(conta_encontrada['extrato']) if conta_encontrada['extrato'] else "Não foram realizadas movimentações."
    exibir_mensagem("EXTRATO", f"Conta: {conta_encontrada['numero_conta']}\nAgência: {conta_encontrada['agencia']}\nTitular: {conta_encontrada['usuario']['nome']}\n\n{extrato_texto}\n\nSaldo: R$ {conta_encontrada['saldo']:.2f}")

def criar_usuario(usuarios: list) -> None:
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        exibir_mensagem("ERRO", "Usuário já cadastrado!")
        return
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, número - bairro - cidade/estado): ")
    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    exibir_mensagem("SUCESSO", "Usuário criado com sucesso!")

def criar_conta(usuarios: list, contas: list, agencia: str) -> None:
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    if not usuario:
        exibir_mensagem("ERRO", "Usuário não encontrado, crie um usuário primeiro.")
        return
    numero_conta = len(contas) + 1
    contas.append({
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": [],
        "numero_saques": 0
    })
    exibir_mensagem("SUCESSO", f"Conta criada com sucesso! Agência: {agencia}, Conta: {numero_conta}")

def listar_contas(contas: list) -> None:
    if not contas:
        exibir_mensagem("LISTA DE CONTAS", "Nenhuma conta cadastrada.")
        return
    for conta in contas:
        exibir_mensagem("CONTA", f"Agência: {conta['agencia']}\nConta: {conta['numero_conta']}\nTitular: {conta['usuario']['nome']}\nCPF: {conta['usuario']['cpf']}\nSaldo: R$ {conta['saldo']:.2f}")

def menu_principal() -> str:
    return textwrap.dedent("""
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Criar Usuário
        [5] Criar Conta
        [6] Listar Contas
        [7] Sair
    => """)

def main() -> None:
    LIMITE_SAQUE = 500
    LIMITE_SAQUES_DIARIOS = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"
    
    while True:
        opcao = input(menu_principal())
        if opcao == "1":
            cpf = input("Informe o CPF do titular da conta: ")
            valor = float(input("Informe o valor do depósito: "))
            depositar(contas, cpf, valor)
        elif opcao == "2":
            cpf = input("Informe o CPF do titular da conta: ")
            valor = float(input("Informe o valor do saque: "))
            sacar(contas, cpf, valor, LIMITE_SAQUE, LIMITE_SAQUES_DIARIOS)
        elif opcao == "3":
            cpf = input("Informe o CPF do titular da conta: ")
            exibir_extrato(contas, cpf)
        elif opcao == "4":
            criar_usuario(usuarios)
        elif opcao == "5":
            criar_conta(usuarios, contas, AGENCIA)
        elif opcao == "6":
            listar_contas(contas)
        elif opcao == "7":
            break
        else:
            exibir_mensagem("ERRO", "Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()