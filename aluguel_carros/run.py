from main import EmpresaAluguelCarros


empresa_aluguel_carros = EmpresaAluguelCarros()

while True:
    print("\nEscolha uma opção:")
    print("1. Criar Carro")
    print("2. Listar Carros")
    print("3. Buscar Carro pela placa")
    print("4. Atualizar Carro")
    print("5. Deletar Carro")
    print("6. Sair")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")
        ano = (input("Digite o ano do carro: "))
        placa = input("Digite a placa do carro: ")
        preco_diaria = (input("Digite o preço da diária: "))
        disponivel = True
        empresa_aluguel_carros.criar_carro(marca, modelo, ano, placa, preco_diaria, disponivel)

    elif opcao == "2":
        lista_carros = empresa_aluguel_carros.listar_carros()
        for i in lista_carros:
            print(i)


    elif opcao == "3":
        placa_carro = input("Digite a placa do carro que deseja buscar: ")
        empresa_aluguel_carros.buscar_carro(placa_carro)


    elif opcao == "4":
        id_carro = input("Digite o ID do carro que deseja atualizar: ")
        marca = input("Digite a nova marca: ")
        modelo = input("Digite o novo modelo: ")
        ano = (input("Digite o ano do carro: "))
        placa = input("Digite a placa do carro:")
        preco_diaria = (input("Digite o novo preço da diária: "))
        disponivel = True
        empresa_aluguel_carros.atualizar_carro(id_carro, marca, modelo, ano, placa, preco_diaria, disponivel)

    elif opcao == "5":
        id_carro = input("Digite o ID do carro que deseja deletar: ")
        empresa_aluguel_carros.deletar_carro(id_carro)

    elif opcao == "6":
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
