menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite_valor_saque = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    print("Por favor, selecione uma das opções a seguir.")
    
    opcao = int(input(menu))

    if opcao == 1:
        
        print("Depósito")
        
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print('Depósito realizado com sucesso!\n')
        else:
            print("A operação falhou! O valor informado é inválido.\n")
    
    elif opcao == 2:
        
        print("Saque")

        if numero_saques < LIMITE_SAQUES:
            
            valor = float(input("Informe o valor que deseja sacar: "))

            if valor <= saldo:

                if valor <= limite_valor_saque:

                    saldo-= valor
                    numero_saques += 1
                    extrato += f'Saque: - R$ {valor:.2f}\n'
                    print("Saque realizado com sucesso!\n")
            
                else:
                    print("Limite de valor por saque excedido.\n")
            
            else:
                print("Saldo insuficiente.\n")

        else:
            print("Limite diário de saques excedido.\n")

    
    elif opcao == 3:

        print("\n=============== Extrato ===============\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print("\n=======================================\n")
    
    elif opcao == 4:

        print("Obrigado por utilizar nossos serviços!\n")
        
        break
    
    else:
        
        print("Opção inválida! Por favor, selecione uma opção válida.\n")

