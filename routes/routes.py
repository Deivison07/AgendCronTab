from flask import Flask
from service.home import home

def adicionar_rota(app: Flask):
    app.add_url_rule('/','home',home)


