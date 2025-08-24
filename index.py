from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# import from folders
from app import app
from components import sidebar, dashboard

# =========  Layout  =========== #
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            sidebar.layout
        ], md=3),

        dbc.Col([
            html.Div(id="page-content")
        ], md=9),
    ])

], fluid=True, style={"padding": "0px"}, className="dbc")


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/" or pathname == "/dashboard":
        return dashboard.layout

    # Página padrão (404)
    return html.Div([
        html.H1("404 - Página não encontrada", className="text-center"),
        html.P("A página que você está procurando não existe.")
    ], className="text-center mt-5")


if __name__ == '__main__':
    app.run(debug=True)
