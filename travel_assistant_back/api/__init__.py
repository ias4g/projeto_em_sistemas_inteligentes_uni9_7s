"""
Módulo de API do Travel Assistant.
Este módulo contém as rotas e modelos da API REST.
"""

from .routes import router
from .models import Query, Response

__all__ = ['router', 'Query', 'Response']
