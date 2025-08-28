menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

saldo = 0
limite_valor_saque = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print('Depósito realizado com sucesso!')
        else:
            print("A operação falhou! O valor informado é inválido.")
    
    elif opcao == 2:
        print("Saque")
    
    elif opcao == 3:
        print("\nExtrato\n")
        print(extrato)
    
    elif opcao == 4:
        print("Obrigado por utilizar nossos serviços!")
        break
    
    else:
        print("Opção inválida! Por favor, selecione uma opção válida.")

