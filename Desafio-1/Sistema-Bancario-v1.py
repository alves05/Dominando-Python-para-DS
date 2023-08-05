print("""
******************************************************
*                                                    *
*                 SISTEMA BANCÁRIO                   *
*                      v 1.0                         *
*                                                    *
******************************************************
""")

# Menu de opções
menu = """
Escolha uma operação abaixo:
                 
    [d] - Depósito
    [s] - Saque
    [e] - Extrato da Conta
    [f] - Fechar Operação
    
: """

# Variáveis
saldo_conta = 0
limite_quantidade_saque_diario = 3
quantidade_saque = 0
saque_maximo = 500.00
extrato = ""

# Início do laço
while True:
    opcao = input(menu)

    if opcao == "d": # Início condicional "depósito"
        operacao_deposito = float(input("Informe o valor do depósito: ")) # Entrada do valor do depósito

        if operacao_deposito > 0: # Condição para aceitar apenas depósitos maiores que 0
            saldo_conta += operacao_deposito # Adiciona o depósito ao saldo da conta
            extrato += f"Operação C:      Depósito    R$ {operacao_deposito:.2f}\n" # Adiciona a operção ao extrato

        else:
            print("Operação Invalida! Por favor, verifique o valor do depósito e tente novamente.") # Mensagem de erro

    elif opcao == "s": # Início condicional "saque"
        operacao_saque = float(input("Informe o valor do saque: ")) # Entrada do valor do saque

        if operacao_saque > saque_maximo: # Condição verifica se o saqu é menor ou igual a 500.00
            print("Transação não autorizada! Valor excede limite de R$ 500.00 por saque, tente novamente.") # Mensagem de erro

        elif quantidade_saque == limite_quantidade_saque_diario: # Condição verifica se esta dentro dos 3 saques permitidos diáriamente
            print("Transação não autorizada! Sua conta excedeu o limite de saques diário.") # mensagem de erro

        elif saldo_conta >= operacao_saque and operacao_saque <= saque_maximo: # Condição verifica se o saldo da conta permite o saque e a quantidade de saques
            saldo_conta -= operacao_saque # Diminui o saldo da conta
            quantidade_saque += 1 # Adiciona a quantidade de saques
            extrato += f"Operação D:      Saque       R$ {operacao_saque:.2f}\n" # Adiciona a operação ao extrato

        else:
            print("Transação não autorizada! Saldo indisponível, verifique o saldo da sua conta e tente novamente.") # Mensagem de erro

    elif opcao == "e": # Exibi extrato
        print("**********************************************************")
        print("                EXTRATO CONTA BANCÁRIA                    ")
        print("**********************************************************")
        print("Não existe movimentações nesta conta." if not extrato else extrato)
        print(f"Saldo da Conta:              R$ {saldo_conta:.2f}")
        print("**********************************************************")

    elif opcao == "f": # Finaliza o programa
        break
    
    else:
        print("Operação Invalida! Por favor, verifique as opções no menu e selecione uma opção válida.") # Mensagem de erro