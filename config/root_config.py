from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from flask.logging import default_handler

from .load_env import NAME
def configName(app: Flask):
    app.name = NAME

def dataBase(app: Flask):...

def log_default(app: Flask):
    
    app.logger.removeHandler(default_handler)
    
    app.logger.setLevel(logging.INFO)
    file_handler = RotatingFileHandler("app.log", maxBytes=100000, backupCount=3)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    file_handler.setLevel(logging.INFO)    
    app.logger.addHandler(file_handler)
    
    # adiciona logs de requests no arquivo de log
    
    # werkzeug_logger = logging.getLogger("werkzeug")
    # werkzeug_logger.setLevel(logging.INFO)
    # werkzeug_logger.addHandler(file_handler)
    
         
def registrar_bluePrint(app: Flask):...

lista_config = []
lista_config.append(dataBase)
lista_config.append(log_default)
lista_config.append(registrar_bluePrint)
lista_config.append(configName)

