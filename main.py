import json #...(Importar a biblioteca JSON)

#...(Função para exibir o menu principal)
def menu_principal():

    print("\n\n------- MENU PRINCIPAL --------\n")
    print("1) Gerenciar Estudantes")
    print("2) Gerenciar Professor")
    print("3) Gerenciar Disciplinas")
    print("4) Gerenciar Turmas")
    print("5) Gerenciar Matriculas")
    print("6) SAIR.\n")
    op = int(input("informe a opção desejada: "))
    return op

#...(Função para exibir menu de opções)
def menu_opcoes(opcadastral):

    print(f"----> {opcadastral} OPÇÕES <----")
    print("1) Adicionar")
    print("2) Listar")
    print("3) Atualizar")
    print("4) Deletar")
    print("5) VOLTAR AO MENU PRINCIPAL")
    ac = int(input("informe a opção desejada: "))
    return ac

#...(Função para incluir no cadastro)
def incluir_cadastro(opcadastral):

    print(f"\n\n--> ADICIONAR UM {opcadastral} <--")
    codigo = int(input(f"\n-- Atribua um código ao {opcadastral}: "))
    nome = input(f"\nInforme o nome do {opcadastral}: ")

    #...(Indentifica se a entidade preicsa cadastrar CPF)
    cpf = ''
    if opcadastral not in ['Disciplinas', 'Matriculas', 'Turmas']:
        cpf = input(f"Informe o CPF do {opcadastral}: ")

    # ...(Dicionario que sera adiconada as informações cadastrais)
    dic = {'codigo': codigo, 'nome': nome, 'cpf': cpf, 'tipo': opcadastral}

    data = carregar_dados()
    data.append(dic)
    salvar_dados(data)
    print(f"\n\n-- {opcadastral} adicionado com sucesso! --\n\n")
    input("Pressione ENTER para continuar")


 #...(Função para listar dados já cadastrados)
def listar_cadastro(opcadastral):

    print(f"\n\n--->  Lista de {opcadastral}  <---")
    data = carregar_dados()
    found = False

    # ...(Verificação se a opção a ser listada é de professores ou estudantes)
    if opcadastral in ['Estudante', 'Professor']:
        print("ID\tNOME\tCPF")
    else:  #...(Se não for, não exibira o CPF na impressão)
        print("ID\tNOME")

    # ...(Verificador de que 'tipo' de entidade se trata)
    for cd in data:
        if cd.get('tipo') == opcadastral:
            found = True
            print(f"{cd['codigo']}\t{cd['nome']}", end="")
            if 'cpf' in cd and opcadastral in ['Estudante', 'Professor']:
                print(f"\t{cd['cpf']}")
            else:
                print("")

    #...(Se não houver ninguem cadastrado exibira essa mensagem)
    if not found:
        print(f"\n\nNão há {opcadastral} cadastrado(as)... \n")

    input("Pressione ENTER para continuar.")

#...(Função para editar cadastro)
def editar_cadastro(opcadastral):

    print("\n\n ==EDITAR==\n")
    data = carregar_dados()
    codigo_atualizar = int(input(f"Informe o código associado o(a) {opcadastral} para editar as "
                                 f"informações cadastrais: "))

    #...(Verifica se é necessário exibir a opção de alterar CPF dependendo de que entidade se trata)
    encontrou = False
    for i in data:
        if 'tipo' not in i:
            continue
        if i['codigo'] == codigo_atualizar and i['tipo'] == opcadastral:
            print(f"\nDados atuais {opcadastral}:")
            print(f"Código: {i['codigo']}")
            print(f"Nome: {i['nome']}")
            if 'cpf' in i and opcadastral not in ['Disciplinas', 'Matriculas', 'Turmas']:
                print(f"CPF: {i['cpf']}")
                novo_cpf = input("Insira um novo CPF (Ou pressione ENTER para manter o mesmo): ")
                if novo_cpf:
                    i['cpf'] = novo_cpf
                    print("\n- CPF atualizado com sucesso! -\n")
                else:
                    print("\n- Mantendo o mesmo CPF! -\n")
            else:
                print("")
            novo_nome = input("\n\nInsira um novo nome (Ou pressione ENTER para manter o mesmo): ")
            i['nome'] = novo_nome if novo_nome else i['nome']
            print(f"\n{opcadastral} atualizado com sucesso!")
            encontrou = True
            salvar_dados(data)
            break
    if not encontrou:
        print(f"- {opcadastral} não encontrado(a). Tente novamente.")

    input("\n-- Pressione ENTER para continuar --")

#...(Função para excluir do cadastro)
def excluir_cadastro(opcadastral):

    print("\n\n ==EXCLUSÃO==\n")
    data = carregar_dados()
    codigo = int(input(f"Informe o código de {opcadastral} que deseja remover: "))

    encontrou = False
    for i in data:
        if 'tipo' not in i:
            continue
        if i['codigo'] == codigo and i['tipo'] == opcadastral:
            data.remove(i)
            encontrou = True
            break

    if encontrou:
        salvar_dados(data)
        print(f"-- [{opcadastral} removido(a) com sucesso! --")
    else:
        print(f"-- [{opcadastral} não encontrado(a)! --")

    input("\n-- Pressioner ENTER para continuar --")

#...(Função para carregar dados do arquivo JSON, se existir)
def carregar_dados():
    try:
        with open('dados.json', 'r') as arquivo:
            data = json.load(arquivo)
    except FileNotFoundError:
        data = []
    return data

#...(Função para salvar dados no arquivo JSON)
def salvar_dados(data):
    with open('dados.json', 'w') as arquivo:
        json.dump(data, arquivo)


#...(Operações do menu principal)
op = 1
while op != 6:
    op = menu_principal()
    opcadastral = ""
    if op == 1:
        opcadastral = "Estudante"
    elif op == 2:
        opcadastral = "Professor"
    elif op == 3:
        opcadastral = "Disciplinas"
    elif op == 4:
        opcadastral = "Turmas"
    elif op == 5:
        opcadastral = "Matriculas"
    elif op == 6:
        print("\n\n --> Salvando cadastro  <--")
        break
    else:
        print("\n\n-- Opção incorreta --\n\n")
        input("-- Pressione ENTER para continuar --")
        continue

    # ...(Operaçoes do menu de opções)
    ac = 1
    while ac != 5:
        ac = menu_opcoes(opcadastral)
        if ac == 1:
            incluir_cadastro(opcadastral)
        elif ac == 2:
            listar_cadastro(opcadastral)
        elif ac == 3:
            editar_cadastro(opcadastral)
        elif ac == 4:
            excluir_cadastro(opcadastral)
        elif ac == 5:
            break
        else:
            print("\n\n-- Opção Incorrenta! --\n\n")
            input("\n-- Pressione ENTER para continuar. --")
            continue
print("Encerrando...")
