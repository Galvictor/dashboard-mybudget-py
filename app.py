import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.express as px
import pandas as pd
import sass
from components.sidebar import create_sidebar

# Compilar SCSS
compiled_css = sass.compile(filename="assets/custom.scss")
with open("assets/custom.css", "w") as f:
    f.write(compiled_css)

# Carregar tema do Dash Bootstrap Templates
load_figure_template("minty")  # só afeta gráficos Plotly

# App Dash
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, "/assets/custom.css"]
)

# Dados exemplo
df = pd.DataFrame({
    "Categoria": ["Alimentação", "Transporte", "Lazer"],
    "Valor": [200, 150, 100]
})

fig = px.bar(df, x="Categoria", y="Valor", title="Exemplo de Gráfico")

# Layout
app.layout = dbc.Container([
    # Conteúdo principal com sidebar
    dbc.Row([
        # Sidebar (lado esquerdo)
        dbc.Col(create_sidebar(), width=3, className="pe-0"),
        
        # Conteúdo principal (lado direito)
        dbc.Col([
            dbc.Row([
                dbc.Col(dcc.Graph(figure=fig))
            ], className="mb-4"),
            dbc.Row([
                dbc.Col(
                    html.Div([
                        html.H4("Tabela de Exemplo"),
                        dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
                    ])
                )
            ])
        ], width=9)
    ])
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)
