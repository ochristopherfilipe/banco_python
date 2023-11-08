# Inicializa o saldo inicial e a variável de controle do programa.
saldo = 0
iniciar = True

# Loop principal para a aplicação bancária.
while iniciar:
    # Exibe as opções do menu.
    print("[1] - Saldo | [2] Depositar | [3] Saque | [4] Encerrar")
    selecionado = int(input())

    # Opção 1: Verificar o saldo.
    if selecionado == 1:
        print(f"O seu saldo é R$: {saldo}")

    # Opção 2: Depositar dinheiro.
    elif selecionado == 2:
        valor_depositado = int(input("Digite o valor a depositar: "))
        saldo += valor_depositado
        print(f"O novo saldo é R$: {saldo}")

    # Opção 3: Sacar dinheiro.
    elif selecionado == 3:
        valor_a_retirar = int(input("Digite o valor a sacar: "))
        if valor_a_retirar <= saldo:
            saldo -= valor_a_retirar
            print(f"Saque efetuado com sucesso! E o saldo atualizado é R$: {saldo}")
        else:
            print("Saque não permitido, saldo insuficiente")

    # Opção 4: Encerrar o programa.
    elif selecionado == 4:
        iniciar = False

    # Opção inválida.
    else:
        print("Opção inválida. Escolha novamente.")

    # Pergunta se o usuário deseja realizar outra operação.
    encerrar = int(input("Deseja realizar outra operação? [1 - SIM] | [2 - NÃO]: "))
    if encerrar != 1:
        iniciar = False
