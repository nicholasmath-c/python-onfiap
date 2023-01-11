baseDados = []

with open("iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        baseDados.append(registro.split(","))

print(baseDados)

print(float(baseDados[0][0]) + float(baseDados[0][0]))