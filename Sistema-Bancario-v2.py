print("""
******************************************************
*                                                    *
*                 SISTEMA BANCÁRIO                   *
*                      v 2.0                         *
*                                                    *
******************************************************
""")


def menu():
    menu = """
    ********************* MENU ********************

    SELECIONE A OPERAÇÃO:

    ----------------- TRANSAÇÕES ------------------

    [D] - DEPÓSITO || [S] - SAQUE || [E] - EXTRATO

    ----------------- CADASTRO --------------------
    
    [CR] - CRIAR USUÁRIO || [CC] - CRIAR CONTA

    ---------- ADMINISTRAÇÃO DE CONTAS ------------
    obs: Area restrita do administrador do banco.
    Acesso com id e senha: (adm - 12345678)

    [L]  -   LISTA DE CONTAS ABERTAS

    -----------------------------------------------

    [x] -  SAIR
  
    ***********************************************

    Operação =>    """

    return input(menu)

# Função depósito
def deposito(saldo_conta, valor_deposito, extrato, /):
    if valor_deposito > 0: # Condição para aceitar apenas depósitos maiores que 0
        saldo_conta += valor_deposito # Adiciona o depósito ao saldo da conta
        extrato += f"Operação Cred.:      Depósito    R$ {valor_deposito:.2f}\n" # Adiciona a operção ao extrato
        print(f"\n\nDepósito no valor R$ {valor_deposito} realizado com sucesso.\n\n") # Mensagem de operação bem sucedida

    else:
        print("\n\nOperação Invalida! Verifique o valor e tente novamente.") # Mensagem de erro

    return saldo_conta, extrato

# Função saque
def saque(*,saldo_conta, valor_saque, extrato, saque_maximo, quantidade_saque, limite_quantidade_saque_diario):
    if valor_saque > saque_maximo: # Condição verifica se o saqu é menor ou igual a 500.00
        print("\n\nValor excede limite R$ 500.00!\n\n") # Mensagem de erro

    elif quantidade_saque >= limite_quantidade_saque_diario: # Condição verifica se esta dentro dos 3 saques permitidos diáriamente
        print("\n\nSua conta excedeu o limite de saques diário!\n\n") # mensagem de erro

    elif saldo_conta >= valor_saque and valor_saque <= saque_maximo: # Condição verifica se o saldo da conta permite o saque e a quantidade de saques
        saldo_conta -= valor_saque # Diminui o saldo da conta
        extrato += f"Operação Deb.:       Saque       R$ {valor_saque:.2f}\n" # Adiciona a operação ao extrato

        print(f"\n\nSaque no valor R$ {valor_saque} realizado com sucesso.\n\n") # Mensagem de operação bem sucedida
        print(f"QUANTIDADES DE SAQUES AUTORIZADOS RESTANTES {limite_quantidade_saque_diario - quantidade_saque}")

    else:
        print("\n\nSaldo insuficiente para saque.\n\n") # Mensagem de erro

    return saldo_conta, extrato

def extrato_bancario(saldo_conta, /, *, extrato): # Função exibe o extrato
    print("\n*" * 58)
    print("                  EXTRATO BANCÁRIO                      ")
    print("*" * 58)
    print("Não existe movimentações nesta conta." if not extrato else extrato)
    print(f"Saldo da Conta:              R$ {saldo_conta:.2f}")
    print("*" * 58)


def cria_novo_usuario(usuarios): # Função cria usuário
    cpf = int(input("\nInforme o CPF (apenas os números): ")) # Inseri o cpf para o novo usuário
    consulta_usuario = filtro_usuario(cpf, usuarios) # Consulta se o cpf está cadastrado

    if consulta_usuario:
        print("\n\nUSUÁRIO JÁ EXISTE!\n\n") # Retorno caso cpf já conste na base de dados

        return
    
    nome_novo_usuario = input("Informe o nome completo: ") # Inserie o nome do novo usuário
    data_de_nacimento_novo_usuario = input("Informe a data de nascimento (dd-mm-aaaa): ") # Inserie a data de nascimento
    endereco_novo_usuario = input("Informe o endereço (logadoro, nº - bairro - cidade/UF): ") # Inserie o endereço

    usuarios.append({"Nome": nome_novo_usuario, "CPF": cpf, "Data_nascimento": data_de_nacimento_novo_usuario, "Endereço": endereco_novo_usuario}) # Adiciona o novo usuário no conjunto de dados

    print("\n\n****** USUÁRIO CRIADO COM SUCESSO! ******\n\n") # Mensagem de finalização do processo


def filtro_usuario(cpf, usuarios): # Filtro de usuários
    consulta_usuario = [usuario for usuario in usuarios if usuario.get("CPF") == cpf] # Laço para consulta de cpf cadastrado
    
    return consulta_usuario[0] if consulta_usuario else None

def cria_nova_conta(agencia, n_conta, usuarios, contas): # Função para criar nova conta
    cpf = int(input("\nInforme o CPF (apenas os números): ")) # Inseri cpf
    consulta_usuario = filtro_usuario(cpf, usuarios)

    for usuario in contas:
        if usuario["Usuário"] == consulta_usuario:
            print("\n\nJÁ EXISTE CONTA PARA ESSE CPF!")

            return
    
    if consulta_usuario:
        nova_conta = {"Agencia": agencia, "Conta": n_conta, "Usuário": consulta_usuario}
        print("\n\n****** CONTA CRIADA COM SUCESSO! ******\n\n")

    else:
        print("\n\nUSUÁRIO NÃO ENCONTRADO! VEIRIFIQUE O CPF E TENTE NOVAMENTE!\n\n")

    return nova_conta
    
def listar_contas(contas): # Função cria lista de contas
    for conta in contas: # Laço lê todas as contas criadas e retorna na tela
        exibe = f"""\n
            Agência: {conta["Agencia"]}
            Conta:   {conta["Conta"]}
            Titular: {conta["Usuário"]["Nome"]}
            CPF:     {conta["Usuário"]["CPF"]}
        """
        print("*" * 50)
        print(exibe)

def main():
    saldo_conta = 0
    limite_quantidade_saque_diario = 3
    quantidade_saque = 0
    saque_maximo = 500.00
    extrato = ""
    agencia = "0001"
    usuarios = []
    lista_contas = []

    while True:
        opcao = menu()

        if opcao == "d": 
            valor_deposito = float(input("\nInforme o valor do depósito: ")) 

            saldo_conta, extrato = deposito(saldo_conta, valor_deposito, extrato) 

        elif opcao == "s": 
            valor_saque = float(input("\nInforme o valor do saque: "))

            saldo_conta, extrato = saque(saldo_conta= saldo_conta,
                                         valor_saque= valor_saque,
                                         extrato= extrato,
                                         saque_maximo= saque_maximo,
                                         quantidade_saque= quantidade_saque,
                                         limite_quantidade_saque_diario= limite_quantidade_saque_diario)
            
            quantidade_saque += 1

        elif opcao == "e": # Exibi extrato
            extrato_bancario(saldo_conta, extrato= extrato) 

        elif opcao == "cr": 
            cria_novo_usuario(usuarios= usuarios)

        elif opcao == "cc":
            n_conta = len(lista_contas)
            n_conta += 1
            conta = cria_nova_conta(agencia= agencia, n_conta= n_conta, contas= lista_contas, usuarios= usuarios)

            if conta:
                lista_contas.append(conta)

        elif opcao == "l":
            adm   = str(input("\nAdministrador: "))
            senha = int(input("\nSenha: "))

            if adm == "adm" and senha == 12345678:
                listar_contas(contas= lista_contas)
            
            else:
                print("\n\nID OU SENHA INVÁLIDOS!\n\n")

        elif opcao == "x":
            break
        
        else:
            print("\n\nOPÇÃO INVALIDA!\n\n")

main()