import dash_bootstrap_components as dbc
from dash import html

# Definindo a sidebar usando dbc.Nav
layout = dbc.Nav([
    # Cabeçalho da sidebar
    html.H4("Hello World Sidebar", className="text-center mb-4 text-primary"),
    
    # Linha separadora
    html.Hr(),
    
    # Lista de navegação
    dbc.NavLink("🏠 Dashboard", href="/", active="exact", className="mb-2"),
    dbc.NavLink("📊 Gráficos", href="/graficos", active="exact", className="mb-2"),
    dbc.NavLink("📋 Tabelas", href="/tabelas", active="exact", className="mb-2"),
    dbc.NavLink("⚙️ Configurações", href="/config", active="exact", className="mb-2"),
    
    # Espaçamento no final
    html.Div(style={"height": "50px"}),
    
    # Rodapé da sidebar
    html.Div([
        html.Small("Dashboard MyBudget", className="text-muted"),
        html.Br(),
        html.Small("v1.0.0", className="text-muted")
    ], className="text-center mt-auto")
    
], 
# Propriedades da sidebar
vertical=True,           # Layout vertical
pills=True,              # Estilo de pílulas
className="bg-light",    # Cor de fundo
style={
    "width": "250px",    # Largura fixa
    "height": "100vh",   # Altura total da viewport
    "padding": "20px",   # Padding interno
    "border-right": "1px solid #dee2e6"  # Borda direita
})

# Exemplo de uso (para testar isoladamente)
if __name__ == "__main__":
    # Este bloco só executa se o arquivo for rodado diretamente
    print("Este arquivo deve ser importado, não executado diretamente.")
    print("Use: from components.sidebar import create_sidebar")
