import textwrap

#Funções do sistema

def exibir_menu():
    
    menu = """
    =============== MENU ===============
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tUsuários
    [5]\tCriar Conta
    [6]\tListar Contas
    [7]\tSair

    => """

    print("Por favor, selecione uma das opções a seguir.")
    
    return int(input(textwrap.dedent(menu)))


def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('Depósito realizado com sucesso!\n')
    else:
        print("A operação falhou! O valor informado é inválido.\n")
    
    return saldo, extrato
    

def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
        
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\nSaldo insuficiente.\n")
    
    elif excedeu_limite:
        print("Limite de valor por saque excedido.\n")
    
    elif excedeu_saques:
        print("Limite diário de saques excedido.\n")
    
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f'Saque: - R$ {valor:.2f}\n'
        print("\nSaque realizado com sucesso!\n")
    
    else:
        print("A operação falhou! O valor informado é inválido.")
    
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):

    print("\n=============== Extrato ===============\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print("\n=======================================\n")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário cadastrado com esse CPF.")
        return
        
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, n.º, bairro, cidade, sigla estado, CEP): ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        print("Usuário cadastrado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        ("\n Usuário não encontrado, processo de criação de conta encerrado.")    


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
                Agência:\t{conta['agencia']}
                Conta Corrente:\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
                """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():

    #Constantes
    LIMITE_SAQUES = 3
    AGENCIA = "001"

    #Variáveis
    saldo = 0
    limite_valor_saque = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:

        opcao = exibir_menu()


        if opcao == 1:

            print("Depósito")
        
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
    
        elif opcao == 2:

            print("Saque")

            valor = float(input("Informe o valor do saque: "))
        
            saldo, extrato = sacar(saldo=saldo,
                                   valor=valor,
                                   extrato=extrato,
                                   limite=limite_valor_saque,
                                   numero_saques=numero_saques,
                                   limite_saques=LIMITE_SAQUES)
       
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)
    
        elif opcao == 4:
            criar_usuario(usuarios)
    
        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
    
        elif opcao == 6:
            listar_contas(contas)
    
        elif opcao == 7:

            print("Obrigado por utilizar nossos serviços!\n")
        
            break
    
        else:
        
            print("Opção inválida! Por favor, selecione uma opção válida.\n")


main()