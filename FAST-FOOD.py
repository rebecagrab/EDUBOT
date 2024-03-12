import os # importar o módulo 'os' para usar funcionalidades dependentes do sistema operacional
import sys # importar o módulo 'sys' para a função de encerrar o programa

def dinheiro(total_pedido):
    valor_pago = float(input('\nDigite o valor pago em dinheiro:'))
    if valor_pago < total_pedido:
        print('Valor insuficiente. Por favor, pague o valor correto')
        dinheiro(total_pedido)
    else:
        troco = valor_pago - total_pedido
        (print(f'\nPagamento de R${total_pedido:.2f} realizado com sucesso! '))
        (print(f'Troco: R${troco:.2f}'))
        print(f'Aproveite sua refeição!')
        sys.exit()

def pagamento(total_pedido):
    print("\nOpções de pagamento:")
    print("[1] - Crédito")
    print("[2] - Débito")
    print("[3] - Dinheiro")
    print("[4] - Pix")

    opcao_pagamento = input("\nEscolha a forma de pagamento: ")
    if opcao_pagamento == '1':
        print(f'\nPagamento de R${total_pedido:.2f} realizado com sucesso.')
        print(f'Aproveite sua refeição!')
        sys.exit()
    elif opcao_pagamento == '2':
        print(f'\nPagamento de R${total_pedido:.2f} realizado com sucesso.')
        print(f'Aproveite sua refeição!')
        sys.exit()
    elif opcao_pagamento == '3':
        dinheiro(total_pedido)
    elif opcao_pagamento == '4':
        print(f'\nPor favor, transfira o valor de R${total_pedido:.2f} para a conta informada.')
        print(f'Aproveite sua refeição!')
        sys.exit()
    else:
        print('Opção de pagamento inválida. Por favor, escolhar uma das opções listadas.')
        pagamento(total_pedido)

def calcular_total(item_menu, adicional):
    precos = {
        'X-burguer': 10.00,
        'X-salada': 7.00,
        'batata frita': 15.00,
        'queijo': 1.50,
        'bacon': 2.00,
        'molho especial': 2.00
    }

    # inicialize o total com o preço do item principal
    total = precos[item_menu]

    #adicione o preço do adicional se houver
    if adicional: 
        total += precos[adicional]
    return total

def confirmar_pedido(nome, item_menu, adicional):
    # Calcula o total do pedido
    total_pedido = calcular_total(item_menu, adicional)

    # Constrói a mensagem de confirmação com base nos itens selecionados
    mensagem = f"Seu pedido é {item_menu}"
    if adicional:
        mensagem += f" com adicional de {adicional}"
    
    mensagem += f". O total é R${total_pedido:.2f}. Confirma?"
    
    # Pergunta ao usuário se ele confirma o pedido
    confirmacao = input(f"{mensagem} [S/N]: ").strip().lower() # remove espaços em branco e converte caracteres para minusculas
    
    # Verifica a resposta do usuário
    if confirmacao == "s":
        total_pedido = calcular_total(item_menu, adicional)
        pagamento(total_pedido) 
    elif confirmacao == "n":
        print("Pedido cancelado.")
        sys.exit()
    else:
        print("Por favor, responda com S (sim) ou N (não).")
        return confirmar_pedido(nome, item_menu, adicional)  # Chama a função novamente se a resposta do usuário for inválida

def adicionais(nome, item_menu):
    while True:
        # Oferecer os adicionais
        adicionais = input(f'{os.linesep}{nome}, o que gostaria de adicionar?{os.linesep}[1] - queijo (R$1.50){os.linesep}[2] - bacon (R$2.00){os.linesep}[3] - molho especial (R$2.00){os.linesep}[4] - Nada.{os.linesep}')
        
        continuar_adicionais = processar_adicionais(adicionais, nome, item_menu)
        if not continuar_adicionais: 
            break

def processar_adicionais(adicionais, nome, item_menu):
    if adicionais == '1':
        confirmar_pedido(nome, item_menu, "queijo")      
    elif adicionais == '2':
        confirmar_pedido(nome, item_menu, "bacon")
    elif adicionais == '3':
        confirmar_pedido(nome, item_menu, "molho especial")
    elif adicionais == '4':
        confirmar_pedido(nome, item_menu, "")  # Nenhum adicional selecionado
    else:
        print('Digite apenas uma das opções acima.') 
        return True  # Continuar oferecendo opções de adicionais

def processar_menu(menu, nome):
    # função para processar a resposta do usuário e imprimir uma mensagem correspondente
    # cada resposta será impressa com o nome do usuário
    if menu == '1':
        print(f'{os.linesep}{nome}, você selecionou o X-burguer, gostaria de algum adicional?{os.linesep}')
        add = input(f'{os.linesep}[1] - Sim.{os.linesep}[2] - Não.{os.linesep}')
        if add == '1':
            adicionais(nome, 'X-burguer') # chamando a função 'adicionais' com a infomação escolhida do menu
        elif add == '2':
            confirmar_pedido(nome, 'X-burguer', "")  # Nenhum adicional selecionado
    elif menu == '2':
        print(f'{os.linesep}{nome}, você selecionou o X-salada, gostaria de algum adicional?{os.linesep}')
        add = input(f'{os.linesep}[1] - Sim.{os.linesep}[2] - Não.{os.linesep}')
        if add == '1':
            adicionais(nome, 'X-salada')
        elif add == '2':
            confirmar_pedido(nome, 'X-salada', "")  # Nenhum adicional selecionado
    elif menu == '3':
        print(f'{os.linesep}{nome}, você selecionou o batata frita, gostaria de algum adicional?{os.linesep}')
        add = input(f'{os.linesep}[1] - Sim.{os.linesep}[2] - Não.{os.linesep}')
        if add == '1':
            adicionais(nome, 'batata frita')
        elif add == '2':
            confirmar_pedido(nome, 'batata frita', "")  # Nenhum adicional selecionado
    elif menu == '4':
        print(f'Até a próxima, {nome}!') # mensagem de despedida
        sys.exit() # fechar o programa
    else:
        print('Digite apenas uma das opções acima.') # mensagem de erro para entrada inválida
    return True

# função para iniciar o boot
def start():
    print(f'{os.linesep}Olá, bem-vindo ao nosso serviço de fast food!{os.linesep}') # mensagem de boas vindas
    nome = input('Para começar, por favor digite seu nome: ') # pedindo o nome do usuário para tornar o atendimento mais pessoal
    # inicia o loop
    while True:
        menu = input( #oferece o menu de opções
            f'O que gostaria de pedir, {nome}?{os.linesep}[1] - X- burger (R$10.00){os.linesep}[2] - X-salada (R$7.00){os.linesep}[3] - Batata frita (R$15.00){os.linesep}[4] - sair{os.linesep}')
        # processar o menu e verificar se o loop deve continuar
        continuar_menu = processar_menu(menu, nome)
        if not continuar_menu: # verifica se o retorno da função processar resposta é False
            break # interrompe o loop

if __name__ == '__main__':
    start() # chama a função start() quando o script é executado diretamente
