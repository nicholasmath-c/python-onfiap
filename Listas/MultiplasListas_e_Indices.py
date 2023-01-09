equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for i in range(0, len(equipamentos)):
    print("\nEquipamento..: ", (i+1))
    print("Nome..: ", equipamentos[i])
    print("Valor..: ", valores[i])
    print("Serial..: ", seriais[i])
    print("Departamento..: ", departamentos[i])
