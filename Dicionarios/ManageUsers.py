from Dicionarios.Funcoes import *

usuarios = {}
opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserirUsuario(usuarios)
    if opcao == "P":
        pesquisarUsuario(usuarios)
    if opcao == "E":
        excluirUsuario(usuarios)
    if opcao == "L":
        listarUsuario(usuarios)

    opcao = perguntar()
