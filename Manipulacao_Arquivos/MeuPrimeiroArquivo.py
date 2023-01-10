# arquivo = open("primeiro_arquivo.txt", "w")
#
# arquivo.write("Meu primerio arquivo")
#
# arquivo.close()

# with open("primeiro_arquivo.txt", "a") as arquivo:
#     arquivo.write("\nTeste")

with open("primeiro_arquivo.txt", "r") as arquivo:
    # conteudo = arquivo.read()
    # print(conteudo)

    for linha in arquivo.readlines():
        print(linha)