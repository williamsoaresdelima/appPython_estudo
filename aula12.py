import requests

def rotorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    # print(dados_pokemon)
    return (dados_pokemon)

def retorna_response(url):
    response = requests.get(url)
    return response.text

get_url = retorna_response('https://www.google.com.br');
print(get_url)