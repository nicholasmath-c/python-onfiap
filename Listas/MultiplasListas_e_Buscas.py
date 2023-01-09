equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(input("Valor: "))
    seriais.append(input("Serial: "))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

busca = input("\nDigite o nome do equipamento que deseja buscar: ")

for i in range(0, len(equipamentos)):
    if busca == equipamentos[i]:
        print("Valor..: ", valores[i])
        print("Serial.: ", seriais[i])