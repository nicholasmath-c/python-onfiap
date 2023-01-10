def perguntar():
    return input("O que deseja realizar?\n" +
                 "<I> - Para Inserir um usuário\n" +
                 "<P> - Para Pesquisar um usuário\n" +
                 "<E> - Para Excluir um usuário\n" +
                 "<L> - Para Listar um usuário: ").upper()

def inserirUsuario(val):
    chave = input("Digite o login: ").upper()
    nome = input("Digite o nome: ").upper()
    data = input("Digite a última data de acesso: ")
    estacao = input("Qual a última estação acessada: ").upper()
    val[chave] = [nome, data, estacao]

def pesquisarUsuario(val):
    chave = input("Insira o login do usuário que deseja listar: ").upper()
    print("/// AQUI ESTÁ O RESULTADO DA SUA BUSCA -> ",
          val.get(chave),
          "\n")

def excluirUsuario(val):
    chave = input("Insira o login do usuário que deseja excluir: ").upper()
    del val[chave]
    print("Usuário excluído!\n")
def listarUsuario(val):
    for chave, valor in val.items():
        print("Objeto.......")
        print("Login: ", chave)
        print("Dados: ", valor)

