import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px
import pandas as pd
from components.sidebar import create_sidebar

def create_layout():
    """
    Cria o layout principal do dashboard.
    Esta função retorna o layout completo da aplicação.
    """
    
    # Dados exemplo
    df = pd.DataFrame({
        "Categoria": ["Alimentação", "Transporte", "Lazer"],
        "Valor": [200, 150, 100]
    })

    fig = px.bar(df, x="Categoria", y="Valor", title="Exemplo de Gráfico")

    # Layout principal
    layout = dbc.Container([
        # Conteúdo principal com sidebar
        dbc.Row([
            # Sidebar (lado esquerdo)
            dbc.Col(create_sidebar(), width=3, className="pe-0"),
            
            # Conteúdo principal (lado direito)
            dbc.Col([
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
        ])
    ], fluid=True, className="")
    
    return layout

# Para testar o layout isoladamente
if __name__ == "__main__":
    print("Este arquivo deve ser importado, não executado diretamente.")
    print("Use: from index import create_layout")
