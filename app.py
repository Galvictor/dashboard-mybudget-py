import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import sass

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

app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True
server = app.server
