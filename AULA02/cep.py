import requests as rqt

cep = input("Digite seu CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = rqt.get(url)
resposta = dados.json()




print(f"""
Você mora na {resposta["logradouro"]}, 
no bairo {resposta["bairro"]}, 
na cidade {resposta["localidade"]}
 """ )