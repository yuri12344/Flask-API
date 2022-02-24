from flask import Flask
# Importante apenas para typehint
# Importando para termos conexão com o banco de dados
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db
    # from app.models.service_catalog_model import ServiceCatalogModel
    # from app.models.signup_client_model import ClientModel

