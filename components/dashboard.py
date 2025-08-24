import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px
import pandas as pd

def create_dashboard():
    """
    Cria o componente principal do dashboard.
    Esta função retorna o conteúdo principal da aplicação.
    """
    
    # Dados exemplo
    df = pd.DataFrame({
        "Categoria": ["Alimentação", "Transporte", "Lazer"],
        "Valor": [200, 150, 100]
    })

    fig = px.bar(df, x="Categoria", y="Valor", title="Exemplo de Gráfico")

    # Conteúdo principal do dashboard
    dashboard = dbc.Col([
        # Gráfico
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(figure=fig)
                    ])
                ], className="shadow-sm")
            ])
        ], className="mb-4"),
        
        # Tabela
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        html.H4("Tabela de Exemplo", className="mb-0")
                    ]),
                    dbc.CardBody([
                        dbc.Table.from_dataframe(
                            df, 
                            striped=True, 
                            bordered=True, 
                            hover=True,
                            className="table-sm"
                        )
                    ])
                ], className="shadow-sm")
            ])
        ])
    ], width=9)
    
    return dashboard

# Para testar o componente isoladamente
if __name__ == "__main__":
    print("Este arquivo deve ser importado, não executado diretamente.")
    print("Use: from components.dashboard import create_dashboard")
