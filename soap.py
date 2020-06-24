from zeep import Client

# para instalar pacotes use pip install nome_do_pacote
# para utlizar webservices em wsdl (XML)
client = Client('http://soapclient.com/xml/soapresponder.wsdl')
# Method1 é um metodo do webservices da client soap
result = client.service.Method1('Eai', 'Shake your body baby so para mim')
print(result)  # Agora vamos consumir imprimindo o retorno da API !!!
