def create_user(usuarios):
    cpf = input('Informe seu CPF: ')
    usuario = filter_user(cpf, usuarios)
    if usuario:
        print(f'Usuario Cadastrado com o cpf: {usuario}!')

    nome = input('Nome Completo: ')
    data_nsc = input('Data de Nascimento (dd/mm/yyy): ')
    endereco = input('Logradouro (rua, numero - bairro - cidade/estado): ')
    print('Usuario cadastrado com sucesso!')

    return usuarios.append({'nome': nome, 'cpf': cpf, 'nascimento': data_nsc, 'endereco': endereco})

def create_account(usuario, conta, agencia, name):
    cpf = input('Informe seu CPF: ')
    verification = filter_user(cpf, usuario)

    numero = 0
    for item in conta:
        if item:
            numero += 1
        numero = 1

    if verification:
        nome = filter_user(usuario, name)
        print('Conta criada com suceso!')
        return conta.append({'nome': nome, 'numero_conta': numero, 'agencia': agencia, 'saldo': '0.0'}), nome

def filter_name(usuario, name):
    for index, nome in enumerate(usuario):
        if usuario[index]['nome'] == name:
            name = usuario[index]['nome']
    return name
def filter_user(cpf, list):
    for item in list:
        if cpf == item['cpf']:
            return cpf
        return None

def menu_account(user, name):
    for index, nome in enumerate(user):
        print(f'''
        [{index}] - {nome['nome']}
        ''')
    option = input(': ')
    for index, nome in enumerate(user):
        if int(option) == index:
            name = user[index]['nome']
    return name

def menu(name):
    print(f'''
    Bem-vindo(a) {name}
    
    [0] - Deposito
    [1] - Sacar
    [2] - Extrato
    
    [3] - Criar Usuário
    [4] - Alterar Usuário
    [5] - Criar conta
    
    [X] - Sair
    ''')
    return input(': ')

def deposito(name, conta, valor, extrato):
    for index, item in enumerate(conta):
        if conta[index]['nome'] == name:
            saldo = conta[index]['saldo']
            conta[index]['saldo'] = (float(saldo) + valor)
            print("Valor Depositado com Sucesso! ")
            return extrato.append({'tipo': 'Deposito', 'valor': valor})

def saque(name, conta, valor, extrato, limite):
    for index, item in enumerate(conta):
        if conta[index]['nome'] == name:
            saldo = conta[index]['saldo']
            if float(saldo) <= 0:
                print(f'Saldo insuficiente: R${saldo}')
            else:
                conta[index]['saldo'] = (float(saldo) - valor)
                print("Valor saque com Sucesso! ")
                limite -= 1
                return extrato.append({'tipo': 'Saque', 'valor': valor}), limite

def extratos(nome, conta, extrato):
    for index, item in enumerate(conta):
        if conta[index]['nome'] == nome:
            print(f'''
        Conta: {nome}
        Saldo: {conta[index]['saldo']}
        Transações:
                ''')
    for item in extrato:
        tipo = item['tipo']
        valor = item['valor']
        print(f'''
        {tipo}: R${valor:.2f}
        ''')
def screen():
    LIMITE_DIARIO = 3
    AGENCIA = '0001'
    limite = '500'

    extrato = []
    usuarios = []
    contas = []
    name = ''

    create_user(usuarios)
    nome = create_account(usuario=usuarios, conta=contas, agencia=AGENCIA, name=name)

    conta_nome = menu_account(usuarios, name)
    while True:
        name_ = []
        option = menu(name_ or conta_nome)
        if option == '0':
            valor = float(input('Valor do Deposito: '))
            deposito(conta_nome, contas, valor, extrato)

        elif option == '1':
            valor = float(input('Valor do Saque: '))
            if valor <= 500:
                saque(conta_nome, contas, valor, extrato, LIMITE_DIARIO)
            else:
                print('Valor maximo de R$ 500,00')

        elif option == '2':
            extratos(conta_nome, contas, extrato)

        elif option == '3':
            create_user(usuarios)

        elif option == '4':
            another_use = menu_account(usuarios, name_)

        elif option == '5':
            create_account(usuario=usuarios, conta=contas, agencia=AGENCIA, name=name)

        elif option == 'x':
            print('Até logo!')
            break








screen()