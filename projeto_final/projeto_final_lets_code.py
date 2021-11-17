# Projeto Finale let's Code:
import requests

url = 'https://api.covid19api.com/dayone/country/brazil'
resposta = requests.get(url)
if resposta.status_code == 200:
    print(f'{resposta.status_code} = Sucesso!')
else:
    print('Not Found!')

# Retorna todos os dados da API:
dados_json = resposta.json()
print(dados_json[0])

# Só vou trabalhar com essas informações: 'Confirmed'(casos confirmados): 1, 'Deaths'(mortes): 0,
# 'Recovered'(Recuperados): 0, 'Active'(casos Ativos): 1, 'Date'(Data): '2020-02-26T00:00:00Z'
# Criar uma variavel para filtrar essas informações:
dados_filtrados = []

# Fazer um for para cada infroamção encontrada em dados_jason: vou adicionar em dados_filtrados:
for informacoes in dados_json:
    dados_filtrados.append([informacoes['Confirmed'], informacoes['Deaths'], informacoes['Recovered'], informacoes['Active'], informacoes['Date']])

# Colocando o cabeçalho :
dados_filtrados.insert(0, ['confirmados', 'obbitos', 'recuperados', 'ativos', 'data'])

# Excluindo o time zone que é 0 e não agrega em nada no projeto:
confirmado = 0
obitos = 1
recuperados = 2
ativos = 3
data = 4

# Excluindo o time zone que é 0 e não agrega em nada no projeto:
for linhas in range(1, len(dados_filtrados)):
    dados_filtrados[linhas][data] = dados_filtrados[linhas][data][:10]

# Colocando as informações abaixo do cabeçalho cada um referente a sua informação:
print(dados_filtrados[0])
for i in dados_filtrados[1:]:
    print(i)

print()
# DateTime: Data, hora, segundo e microsegundo:
import datetime as dt
print(dt.time(12, 6, 21, 7), 'Hora:minuto:segundo:microsegundo')
print('----')
print(dt.date(2021, 10, 30), 'Ano/mês/dia')
print('----')
print(dt.datetime(2021, 10, 30, 12, 6, 21, 7), 'Ano/mês/dia Hora:minuto:segundo:microsegundo')
print()

# Tipos de datas contadores de segundos:

natal = dt.date(2021, 12, 25)
reveillon = dt.date(2022, 1, 1)
print({reveillon - natal})
print(f'Faltam {(reveillon - natal).days} dias para o reveillon')
print(f'Faltam {(reveillon - natal).total_seconds()} segundos para o reveillon')
print(f'Faltam {(reveillon - natal).microseconds} microsegundos para o reveillon')
print()

# Transformando os dados da minha API em csv:
import csv
with open('brasil_covid.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(dados_filtrados)

# Altertando a data dos dados que é string para datetime:
for i in range(1, len(dados_filtrados)):
    dados_filtrados[i][data] = dt.datetime.strptime(dados_filtrados[i][data], '%Y-%m-%d')


# Colocando as informações abaixo do cabeçalho cada um referente a sua informação:
print(dados_filtrados[0])
for i in dados_filtrados[1:]:
    print(i)


# Criando uma função para construir os dados do eixo y:
def get_datasets(y, labels):
    # Condição para verificar se o primeiro valor que foi passado em y é um tipo lista ou um valor comum:
    if type(y[0]) == list:
        # se for uma lista eu vou inicializar uma variavel: que vai ser uma lista contendo os valores de 'y' e o 'label' respectivo de cada um delas.
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data': y[i]
            })
        return datasets
    else:
        return [
            {
                'label': labels[0],
                'data': y
            }
        ]


# Função para definir o titulo do gráfico:
def set_title(title=''):
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return {
        'title': title,
        'display': display
    }


# Função que cria o gráfico: que recebe todos os dicionarios:
def create_chart(x, y, labels, kind='bar', title=''):
    # Criar uma cariavel que recebe uma função
    datasets = get_datasets(y, labels)

    # Variavel Chave responsavel pela denifição do titulo e outras coisas referente essa API:
    options = set_title(title)

    # Criar o dicionario que representa o gráfico:
    chart = {
        'type': kind,
        'data': {
            'labels': x,
            'datasets': datasets
        },
        'options': options
    }
    return chart


# Função para fazer a requisição na API: retorno é binário
def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'
    requisicao = requests.get(f'{url_base}?c={str(chart)}')
    return requisicao.content


# Função para salvar a imagem:
def save_image(path, content):
    with open(path, 'wb') as image:
        image.write(content)


from PIL import Image
from IPython.display import display


# Função para mostrar a imagem
def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)


y_data_1 = []
for obs in dados_filtrados[1::10]:
    y_data_1.append(obs[confirmado])

y_data_2 = []
for obs in dados_filtrados[1::10]:
    y_data_2.append(obs[recuperados])

labels = ['Confirmados', 'Recuperados']

x = []

for obs in dados_filtrados[1::10]:
    x.append(obs[data].strftime('%d/%m/%a'))

chart = create_chart(x, [y_data_1, y_data_2], labels, title='Gráfico confirmado x recuperados')
chart_content = get_api_chart(chart)
save_image('meu-primeiro-grafico.png', chart_content)
display_image('meu-primeiro-grafico.png')

from urllib.parse import quote


# Gerar QR-CODE:
def get_api_qrcode(link):
    text = quote(link) # parsing do link para url
    url_base = 'https://quickchart.io/qr'
    resp = requests.get(f'{url_base}?text={text}')
    return resp.content


# Recuperar o link
url_base = 'https://quickchart.io/chart'
link = f'{url_base}?c={str(chart)}'
save_image('qr-code.png', get_api_qrcode(link))
display_image('qr-code.png')