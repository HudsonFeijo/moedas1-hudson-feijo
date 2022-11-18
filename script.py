import requests
import pandas as pd
import plotly.express as px

# Faz a requisição para a API
req = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,CNY-BRL')
req_disc = req.json() 

# Inclui o valor das moedas nas variaveis
dollar = req_disc['USDBRL']['bid']
euro = req_disc['EURBRL']['bid']
yuan = req_disc['CNYBRL']['bid']

# Cria um DataFrame e adiciona os valores das moeda
tab = pd.DataFrame(data=[[float(dollar)],[float(euro)],[float(yuan)]], index=['Dollar', 'Euro','Yuam'], columns=['Valor'])

# Cria o grafico com os valores
graphic = px.bar(tab, x=tab.index, y='Valor')
graphic.show()
