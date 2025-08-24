# Módulo components
# Este arquivo torna a pasta components um módulo Python

from .sidebar import create_sidebar
from .dashboard import create_dashboard

__all__ = ['create_sidebar', 'create_dashboard']
