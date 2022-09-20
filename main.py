# Opções do Menu Principal #
def menu_principal_info():
    print('\n\t##########################################################', end='')
    print('\n\t===================== BANCO DE TODOS =====================')
    print('\t##########################################################')
    print('\n\t1 - Cadastrar Nova Conta\n\t2 - Encontra uma Conta')
    print('\t3 - Ver Contas\n\t0 - Sair\n')
    print('\t##########################################################')
    print('\t##########################################################')


# Opções Menu Secundario #
def menu_secundario_info():
    print('\n\t1 - Remover\n\t2 - Realizar Transferencia')
    print('\t3 - Exibir Saldo\n\t4 - Depositar\n\t0 - Sair')


# Lista das Contas #
contas_bancarias = []
# Contador dos Numeros das Contas #
num_contas = 0


# Função Criar uma Nova Conta #
def nova_conta(numero, titular, saldo):
    conta = {'numero': numero,
             'titular': titular,
             'saldo': saldo}
    return conta


# Função para Econtrar uma Conta #
def buscar_conta(numero):
    for conta in contas_bancarias:
        if conta['numero'] == numero:
            return conta


# Função para Imprimir uma Conta #
def imprimir_conta(conta):
    print('\t-----------------------------------')
    print('\tNumero: {}'.format(conta['numero']))
    print('\tTitular: {}'.format(conta['titular']))
    print('\tSaldo: R$ {:.2f}'.format(conta['saldo']))
    print('\t-----------------------------------')


# Função para Imprimir a lista de Contas #
def imprimir_contas(contas):
    for conta in contas:
        imprimir_conta(conta)


# Função para Realizar transferençias #
def transferir_valor(conta_saq, conta_dep, valor):
    if conta_saq['saldo'] >= valor:
        conta_saq['saldo'] -= valor
        conta_dep['saldo'] += valor
        print('\n\tTransferência Realizada com Sucesso!')
    else:
        print('\n\tSaldo Insuficiente!')


# Função para Depositar Valor #
def depositar(conta, valor):
    conta['saldo'] += valor


# Função para Valida um Valor Repassado #
def validar_valor(valor):
    if valor.isdigit():
        return int(valor)
    else:
        return None


# Menu Secundario #
def menu_secundario(conta):
    op = None
    while op != 0:
        menu_secundario_info()
        op = validar_valor(input('\n\tDigite a Opção: '))

        if op == 0:
            print('\n\tVOLTANDO...')
        elif op == 1:

            contas_bancarias.remove(conta)
            print('\n\tConta Removida com Sucesso!')
            op = 0

        elif op == 2:

            if len(contas_bancarias) >= 2:
                numero = validar_valor(input('\n\tDigite o Numero da Conta a Transferir: '))

                if numero is not None:
                    conta_dep = buscar_conta(numero)

                    if conta_dep is not None:
                        valor = float(input('\tDigite o Valor a Transferir: '))
                        transferir_valor(conta, conta_dep, valor)
                    else:
                        print('\n\tConta Não Encontrada!')
                else:
                    print('\n\tNumero da Conta Invalido!')
            else:
                print('\n\tNão Existe Contas para Transferir!')

        elif op == 3:

            print()
            imprimir_conta(conta)

        elif op == 4:

            valor = float(input('\n\tInforme o Valor a ser Depositado: '))
            depositar(conta, valor)
            print('\n\tValor Depositado com Sucesso!')

        else:
            print('\n\tOpção Invalida!')


# Menu principal #
def menu(numcontas):
    op = None
    while op != 0:
        menu_principal_info()
        op = validar_valor(input('\n\tDigite a Opção: '))

        if op == 0:
            print('\n\tSAINDO...')
        elif op == 1:

            titular = input('\n\tDigite o Nome do Titular: ')
            saldo = float(input('\tDigite o Saldo Inicial: '))
            numcontas += 1
            contas_bancarias.append(nova_conta(numcontas, titular, saldo))
            print('\n\tConta Cadastrada com Sucesso!')

        elif op == 2:

            if contas_bancarias:
                numero = validar_valor(input('\n\tDigite o Numero da Conta: '))

                if numero is not None:
                    conta = buscar_conta(numero)

                    if conta is not None:
                        print()
                        imprimir_conta(conta)
                        menu_secundario(conta)
                    else:
                        print('\n\tConta Não Encontrada!')
                else:
                    print('\n\tNumero da Conta Invalido!')
            else:
                print('\n\tNão há Contas Cadastradas!')

        elif op == 3:

            if contas_bancarias:
                print()
                imprimir_contas(contas_bancarias)
            else:
                print('\n\tNão há Contas Cadastradas!')

        else:
            print('\n\tOpção Invalida!')


menu(num_contas)
