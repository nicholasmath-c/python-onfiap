def perguntar():
    return input("O que deseja realizar?\n" +
                 "<I> - Para Inserir um usuário\n" +
                 "<P> - Para Pesquisar um usuário\n" +
                 "<E> - Para Excluir um usuário\n" +
                 "<L> - Para Listar um usuário: ").upper()

def inserirUsuario(dicionario):
    chave = input("Digite o login: ").upper()
    nome = input("Digite o nome: ").upper()
    data = input("Digite a última data de acesso: ")
    estacao = input("Qual a última estação acessada: ").upper()
    dicionario[chave] = [nome, data, estacao]
    salvarUsuario(dicionario)

def pesquisarUsuario(dicionario):
    chave = input("Insira o login do usuário que deseja listar: ").upper()
    print("/// AQUI ESTÁ O RESULTADO DA SUA BUSCA -> ",
          dicionario.get(chave),
          "\n")

def excluirUsuario(dicionario):
    chave = input("Insira o login do usuário que deseja excluir: ").upper()
    del dicionario[chave]
    print("Usuário excluído!\n")
def listarUsuario(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto.......")
        print("Login: ", chave)
        print("Dados: ", valor)

def salvarUsuario(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))

