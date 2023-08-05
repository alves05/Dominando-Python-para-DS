print("""
******************************************************
*                                                    *
*                 SISTEMA BANCÁRIO                   *
*                      v 2.0                         *
*                                                    *
******************************************************
""")

# Função menu de opções
def menu():
    menu = """
    SELECIONE A OPERAÇÃO DESEJADA:                 
    
    [au] -  Acessar Usuário
    [ac] -  Acessar Conta
    [nu] -  Criar Novo Usuário
    [nc] -  Criar Nova Conta
    [lc] -  Listar Contas
    [d]  -  Depósito
    [s]  -  Saque
    [e]  -  Extrato da Conta

    [f]  -  Fechar Operação
    
    Operação => """

    return input(menu)

# Função depósito
def deposito(saldo_conta, valor_deposito, extrato):
    if valor_deposito > 0: # Condição para aceitar apenas depósitos maiores que 0
        saldo_conta += valor_deposito # Adiciona o depósito ao saldo da conta
        extrato += f"Operação C:      Depósito    R$ {valor_deposito:.2f}\n" # Adiciona a operção ao extrato
        print(f"Depósito no valor R$ {valor_deposito} realizado com sucesso") # Mensagem de operação bem sucedida

    else:
        print("Operação Invalida! Por favor, verifique o valor do depósito e tente novamente.") # Mensagem de erro

    return saldo_conta, extrato

# Função saque
def saque(saldo_conta, valor_saque, extrato, saque_maximo, quantidade_saque, limite_quantidade_saque_diario):
    if valor_saque > saque_maximo: # Condição verifica se o saqu é menor ou igual a 500.00
        print("Transação não autorizada! Valor excede limite de R$ 500.00 por saque, tente novamente.") # Mensagem de erro

    elif quantidade_saque == limite_quantidade_saque_diario: # Condição verifica se esta dentro dos 3 saques permitidos diáriamente
        print("Transação não autorizada! Sua conta excedeu o limite de saques diário.") # mensagem de erro

    elif saldo_conta >= valor_saque and valor_saque <= saque_maximo: # Condição verifica se o saldo da conta permite o saque e a quantidade de saques
        saldo_conta -= valor_saque # Diminui o saldo da conta
        quantidade_saque += 1 # Adiciona a quantidade de saques
        extrato += f"Operação D:      Saque       R$ {valor_saque:.2f}\n" # Adiciona a operação ao extrato

    else:
        print("Transação não autorizada! Saldo indisponível, verifique o saldo da sua conta e tente novamente.") # Mensagem de erro

    return saldo_conta, extrato

def extrato_bancario(saldo_conta, extrato): # Função exibe o extrato
    print("*" * 58)
    print("                EXTRATO CONTA BANCÁRIA                    ")
    print("*" * 58)
    print("Não existe movimentações nesta conta." if not extrato else extrato)
    print(f"Saldo da Conta:              R$ {saldo_conta:.2f}")
    print("*" * 58)


def cria_novo_usuario(usuarios): # Função cria usuário
    cpf = int(input("Informe o CPF (apenas os números): ")) # Inseri o cpf para o novo usuário
    consulta_usuario = filtro_usuario(cpf, usuarios) # Consulta se o cpf está cadastrado

    if consulta_usuario:
        print("Já existe uma conta cadastrada com esse CPF. Por favor verifique seus dados.") # Retorno caso cpf já conste na base de dados

        return
    
    nome_novo_usuario = input("Informe o nome completo: ") # Inserie o nome do novo usuário
    data_de_nacimento_novo_usuario = input("Informe a data de nascimento (dd-mm-aaaa): ") # Inserie a data de nascimento
    endereco_novo_usuario = input("Informe o endereço (logadoro, nº - bairro - cidade/UF): ") # Inserie o endereço

    usuarios.append({"Nome": nome_novo_usuario, "CPF": cpf, "Data_nascimento": data_de_nacimento_novo_usuario, "Endereço": endereco_novo_usuario}) # Adiciona o novo usuário no conjunto de dados

    print("****** USUÁRIO CRIADO COM SUCESSO! ******") # Mensagem de finalização do processo


def filtro_usuario(cpf, usuarios): # Filtro de usuários
    consulta_usuario = [usuario for usuario in usuarios if usuario["CPF"] == cpf] # Laço para consulta de cpf cadastrado
    
    return consulta_usuario[0] if consulta_usuario else None

def cria_nova_conta(agencia, n_conta, usuarios): # Função para criar nova conta
    cpf = int(input("Informe o CPF (apenas os números): ")) # Inseri cpf
    consulta_usuario = filtro_usuario(cpf, usuarios) # Consulta o cpf para adicionar a nova conta

    if consulta_usuario: # Condição para criar nova conta
        nova_conta = {"Agencia": agencia, "Conta": n_conta, "Usuário": consulta_usuario}
        print("****** CONTA CRIADA COM SUCESSO! ******")

        return nova_conta
    
    print("Usuário com CPF não cadastrado!") # mensagem de erro caso o cpf não esteja cadastrado

def lista_contas(contas): # Função cria lista de contas
    for conta in contas: # Laço lê todas as contas criadas e retorna na tela
        exibe = f"""
            Agência: {conta["Agencia"]}
            Conta:   {conta["Conta"]}
            Titular: {conta["Usuário"]["Nome"]}
        """
        print("*" * 50)
        print(exibe)
        print("*" * 50)

def main(): # Função para execução do programa
    # Variáveis
    saldo_conta = 0
    limite_quantidade_saque_diario = 3
    quantidade_saque = 0
    saque_maximo = 500.00
    extrato = ""
    agencia = "0001"
    usuarios = []
    contas = []

    # Início do laço
    while True:
        opcao = menu()

        if opcao == "d": # Início condicional "depósito"
            valor_deposito = float(input("Informe o valor do depósito: ")) # Entrada do valor do depósito

            saldo_conta, extrato = deposito(saldo_conta= saldo_conta,
                                            valor_deposito= valor_deposito,
                                            extrato= extrato) # Criando depósito

        elif opcao == "s": # Início condicional "saque"
            valor_saque = float(input("Informe o valor do saque: ")) # Entrada do valor do saque

            saldo_conta, extrato = saque(saldo_conta= saldo_conta,
                                          valor_saque= valor_saque, 
                                          extrato= extrato,
                                          saque_maximo= saque_maximo,
                                          quantidade_saque= quantidade_saque,
                                          limite_quantidade_saque_diario= limite_quantidade_saque_diario) # Criando saque

        elif opcao == "e": # Exibi extrato
            extrato_bancario(saldo_conta= saldo_conta, extrato= extrato) # Criando extrato

        elif opcao == "nu": 
            cria_novo_usuario(usuarios= usuarios) # Criando usuário

        elif opcao == "nc":
            n_conta = len(contas)
            n_conta += 1
            conta = cria_nova_conta(agencia= agencia, n_conta= n_conta, usuarios= usuarios) # Criando conta

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            lista_contas(contas) # Listando contas

        elif opcao == "f": # Finaliza o programa
            break
        
        else:
            print("Operação Invalida! Por favor, verifique as opções no menu e selecione uma opção válida.") # Mensagem de erro

main()