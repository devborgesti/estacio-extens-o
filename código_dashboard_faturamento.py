import pandas as pd
import plotly.express as px
import numpy as np
from dash import Dash, dcc, html

# Criando o app Dash
app = Dash(__name__)

# Definir dias do mês (30 dias para este exemplo)
dias = [f'Dia {i}' for i in range(1, 31)]
regioes = ['Norte', 'Sul', 'Centro-Oeste']

# Gerar valores de faturamento para bovinos e cordeiros diariamente para cada região
np.random.seed(42)
faturamento_bovinos = {regiao: np.random.randint(5000, 20000, size=30) for regiao in regioes}
faturamento_cordeiros = {regiao: np.random.randint(2000, 8000, size=30) for regiao in regioes}

# Criando um DataFrame fictício para o mês
df = pd.DataFrame({
    'Dia': np.tile(dias, len(regioes)),  # Replicando os dias para cada região
    'Região': np.repeat(regioes, len(dias)),  # Replicando as regiões para cada dia
    'Faturamento Bovinos': np.concatenate([faturamento_bovinos[regiao] for regiao in regioes]),
    'Faturamento Cordeiros': np.concatenate([faturamento_cordeiros[regiao] for regiao in regioes])
})

# Somando o faturamento total de bovinos e cordeiros
df['Faturamento Total'] = df['Faturamento Bovinos'] + df['Faturamento Cordeiros']

# Criar o gráfico de faturamento total por dia, dividido por região
fig = px.bar(df, x='Dia', y='Faturamento Total', color='Região',
             title='Faturamento Diário por Região (Bovinos e Cordeiros)',
             labels={'Faturamento Total': 'Faturamento (R$)', 'Dia': 'Dia'},
             barmode='group')

# Layout do dashboard
app.layout = html.Div(children=[
    html.H1(children='Análise de Faturamento - Carapreta (Bovinos e Cordeiros)'),

    dcc.Graph(
        id='faturamento-graph',
        figure=fig
    )
])

# Rodar o app
if __name__ == '__main__':
    app.run_server(debug=True)
