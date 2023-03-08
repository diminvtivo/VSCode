#pandas e openpyxl (integração excel), twillio (sms)
import pandas as pd, openpyxl
from twilio.rest import Client

#Config Twilio
account_sid = "AC031d27031542a5044b08edc6f74d0a74"
auth_token  = "8b71ee2ec815d88d84fd62500ebcc2af"
client = Client(account_sid, auth_token)

# integrar 6 arquivos excel no código
lista_meses = ["janeiro", "março", "abril", "maio", "junho"] #toda lista no Python fica entre []

# Pra cada arquivo
    #verificar se valor na coluna de Vendas é maior que 55k
for i in lista_meses:
    tabela_vendas = pd.read_excel(f"{i}.xlsx")
    # Se valor for maior que 55k, enviar sms
    #com nome, mês e valor das vendas

    if (tabela_vendas["Vendas"] >= 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] >= 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] >= 55000, "Vendas"].values[0]
        print(f"No mês de {i} um vendedor bateu a meta. Vendedor: {vendedor}, Vendas: R${vendas}")
        message = client.messages.create(
        to="+5511983927204", 
        from_="+16413213680",
        body=f"No mês de {i} um vendedor bateu a meta. Vendedor: {vendedor}, Vendas: R${vendas}")
print(message.sid)

# Senão, continuar rodando código (não fazer nada)