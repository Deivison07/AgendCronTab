from flask import Flask
from config.root_config import lista_config
from routes.routes import adicionar_rota


def startApp():
    app = Flask(__name__)
    
    #build config
    for config in lista_config:
        config(app)
    
    #build routes
    adicionar_rota(app)
    return app



