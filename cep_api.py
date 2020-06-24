import json
import requests
# consumindo o api rest do via cep

cep = int(input("Digite um cep: ").strip())

url = 'https://viacep.com.br/ws/'+ str(cep) +'/json/' # url/uri do json (web services)
payload = {}
headers = {}
resultado = ''
requisicao = requests.request('GET',url,data = payload, headers = headers)
print(requisicao.status_code) # 200 Ok
json_response = json.loads(requisicao.text)
print(json_response) 
