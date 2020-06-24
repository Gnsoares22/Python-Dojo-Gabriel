from requests import request, get
import json #pip --version  versão do gerenciador de pacotes do python || pip freeze - lista todos modulos instalados atualmente

# ele carregou o json da api covid-19 (consumiu a API) e depois carregou o json numa variavel utilizando a lib json
url = 'https://covid19-brazil-api.now.sh/api/report/v1/brazil'
headers = {}
payload = {}
response = request('GET', url, data=payload, headers=headers)
print(response.status_code) # 200 OK 
json_dados = json.loads(response.text) 
print(json_dados)
print("\n" + str(json_dados['data']['recovered'])) #acessando as chaves da API json


print("*" * 40) ##Exemplo 2

resposta = get("https://viacep.com.br/ws/01001000/json/")
print(resposta.status_code) # 200
json_dados_cep = resposta.json()
print(json_dados_cep)
print("Logradouro: " + json_dados_cep["logradouro"])


### Exemplo 3 puxando todo HTML da página 

def retorna_response(url):
    response = get(url)
    return response.text

if __name__ == '__main__':
    try:
        response = retorna_response('http://www.levellearn.com.br/')
        print(response)
    except Exception as e:
        print("Erro: " + str(e))