agenda = {
    "Leticia": "85 99999-9998",
    "Matheus": "88 98989-3333"
}


def adicionarContato(nome: str, telefone: str) -> None:
    agenda[nome] = telefone
    print("Contato adicionado com sucesso!")


def editarContato(nome: str, telefone: str) -> None:
    if nome in agenda:
        agenda[nome] = telefone
        print('Telefone alterado com sucesso!')
    else:
        print("Contato não existe!")


def buscarContato(nome: str) -> None:
    if nome in agenda:
        print(f"Nome: {nome}")
        print(f"Telefone: {agenda[nome]}")
    else:
        print('Contato não existe')


def deletarContato(nome: str) -> None:
    if nome in agenda:
        del agenda[nome]
        print('Contato removido com sucesso!')
    else:
        print('Contato não existe!')


def listarTodos() -> None:
    print(agenda)


while True:
    print("---- AGENDA TELEFONICA ----")
    opcao = int(input("1 - Adicionar contato \n"
                      "2 - Editar contato \n"
                      "3 - Buscar contato \n"
                      "4 - Deletar contato \n"
                      "5 - Listar todos \n"
                      "6 - Sair \n"
                      "Selecione uma opção: "))

    if opcao == 1:
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone: ')
        adicionarContato(nome, telefone)

    elif opcao == 2:
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o novo telefone: ')
        editarContato(nome, telefone)

    elif opcao == 3:
        nome = input('Digite o nome do contato: ')
        buscarContato(nome)

    elif opcao == 4:
        nome = input('Digite o nome do contato: ')
        deletarContato(nome)

    elif opcao == 5:
        listarTodos()

    elif opcao == 6:
        break

