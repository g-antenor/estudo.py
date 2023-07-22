menu = '''
    
    [0] - Depositar
    [1] - Sacar
    [3] - Extrato
        
'''
valor_conta = 500.00
LIMITE_DIARIO = 3
depositos = []
saques = []

while True == True:
    option = input(menu.center(20, '#'))
    if option == '0':
        deposito = input('Valor do Deposito: ')
        depositos = float(deposito)
        valor_conta += float(deposito)
        print(f'Saldo Atual: R${valor_conta:.2f}')

    elif option == '1':
        if LIMITE_DIARIO > 0:
            saque = input('Valor do Saque: ')
            saque = float(saque)
            if (valor_conta - saque) <= -1:
                print(f'Saldo insuficiente: {valor_conta:.2f}')
            elif saque <= 500:
                saques = float(saque)
                valor_conta -= float(saque)
                print(f'Saldo Atual: R${valor_conta:.2f}')
                LIMITE_DIARIO -= 1
            else:
                print('Apenas saques com valor maximo de R$500,00')
        else:
            print(f'Limite de saque diario: {LIMITE_DIARIO}')

    elif option == '3':
        if depositos == [] and saques == []:
            print(f"""        
                    Depositos: R$0,00
                    Saques: R$0,00

                    Saldo Atual: R${valor_conta:.2f}
                    """)
        elif depositos:
            print(f"""        
                    Depositos: R${depositos:.2f}
                    Saques: R$0,00

                    Saldo Atual: R${valor_conta:.2f}
                    """)
        if saques:
            print(f"""        
                    Depositos: R$0,00
                    Saques: R${saques:.2f}

                    Saldo Atual: R${valor_conta:.2f}
                    """)
        else:
            print(f"""        
                    Depositos: {depositos:.2f}
                    Saques: {saques:.2f}

                    Saldo Atual: R${valor_conta:.2f}
                    """)
        break
    elif LIMITE_DIARIO == 0:
        print('Até logo, Volte sempre!')