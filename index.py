import dash_bootstrap_components as dbc
from dash import html
from components.sidebar import create_sidebar
from components.dashboard import create_dashboard

def create_layout():
    """
    Cria o layout principal do dashboard.
    Esta função retorna o layout completo da aplicação.
    """
    
    # Layout principal
    layout = dbc.Container([
        # Conteúdo principal com sidebar
        dbc.Row([
            # Sidebar (lado esquerdo)
            dbc.Col(create_sidebar(), width=3, className="pe-0"),
            
            # Conteúdo principal (lado direito)
            create_dashboard()
        ])
    ], fluid=True)
    
    return layout

# Para testar o layout isoladamente
if __name__ == "__main__":
    print("Este arquivo deve ser importado, não executado diretamente.")
    print("Use: from index import create_layout")
