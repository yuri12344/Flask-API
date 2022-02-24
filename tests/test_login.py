from app import create_app 
from flask import json
# Importante apenas para typehint
# Importando para termos conexão com o banco de dados



def test_add():    
    given = {
    "name": "Joe Doe",
    "email": "joedoe@gmail.com",
    "password": "Min 3 character max 15",
    "phone": "00-000000000",
    "address": "Rua Henrique Anxieta",
    "city": "Sao Paulo",
    "state": "SP",
    "cpf/cnpj": "000.000.000-00",
    "schedule": "seg - sex 8 - 18",
    "description": "Descrição da sua empresa"
    }    
    response = app.test_client().post(
        '/signup/company',
        data=json.dumps(given),
        content_type='application/json',
    )

    assert response.status_code == 200