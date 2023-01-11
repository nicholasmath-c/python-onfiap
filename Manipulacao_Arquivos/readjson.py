import json

with open("bd.json", "r") as arq_json:
    dic = json.load(arq_json)
    for chave, dados in dic.items():
        print(chave + " | " + str(dados))
