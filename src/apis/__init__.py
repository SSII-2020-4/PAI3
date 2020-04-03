from flask_restplus import Api
from .api_client import api as api_client

api = Api(
    title="PAI3",
    description="Simulación de intercambio de mensajes entre un cliente y servidor usando SSL1.3",
    version="1.0"
)

api.add_namespace(api_client)