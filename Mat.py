MAX_INGRESSOS = 100
PRECO_INGRESSO = 10.0

ingressos_vendidos_comuns = 0
ingressos_vendidos_estudantes = 0

while True:
    print("Bem-vindo ao sistema de venda de ingressos!")
    print("1 - Comprar ingresso comum")
    print("2 - Comprar ingresso para estudante")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        if ingressos_vendidos_comuns + ingressos_vendidos_estudantes < MAX_INGRESSOS:
            ingressos_vendidos_comuns += 1
            print(f"Ingresso comum vendido! Preço: R${PRECO_INGRESSO}")
        else:
            print("Limite de ingressos alcançado!")
    elif opcao == 2:
        if ingressos_vendidos_comuns + ingressos_vendidos_estudantes < MAX_INGRESSOS:
            ingressos_vendidos_estudantes += 1
            print(f"Ingresso para estudante vendido! Preço: R${PRECO_INGRESSO / 2}")
        else:
            print("Limite de ingressos alcançado!")
    elif opcao == 3:
        print("Total de ingressos comuns vendidos:", ingressos_vendidos_comuns)
        print("Total de ingressos para estudantes vendidos:", ingressos_vendidos_estudantes)
        faturamento_total = (ingressos_vendidos_comuns + ingressos_vendidos_estudantes) * PRECO_INGRESSO
        print("Faturamento total: R$", faturamento_total)
        break
    else:
        print("Opção inválida! Tente novamente.")