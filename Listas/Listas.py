inventario=[]
resposta="S"
while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(input("Valor: "))
    inventario.append(input("Número Serial: "))
    inventario.append(input("Departamento: "))
    resposta=input("Digite \"S\" para continuar: ").upper()

for x in inventario:
    print(x)