from flask import Blueprint, request, current_app
from flask.json import jsonify
from app.models.client import UserModel
from app.services.signups_verifications import ClientDataSignupVerification, CompanyDataSignUpVerification


bp_signup_client = Blueprint('bp_signup_client', __name__, url_prefix='/signup')
@bp_signup_client.route('/client', methods=['POST'])
def signup_comp():
    checked_data = ClientDataSignupVerification(request.get_json()).__dict__

    if checked_data['can_register'] == False:
        return checked_data

    if UserModel.query.filter_by(email=checked_data['try_register']['email']).first():
        return jsonify({"message": "Email allready taken"})

    if checked_data['can_register'] == True:
        user_data = checked_data['try_register']

        client = UserModel( 
            iscompany="False",
            name=user_data["name"],
            email=user_data["email"],
            password=user_data['password'],
            phone=user_data["phone"],
            address=user_data["address"],
            city=user_data["city"],
            state=user_data["state"]
        )
        try:
            session = current_app.db.session
            session.add(client)
            session.commit()
            return {"status": "User created"}
        except Exception as e:
            return {"status": str(e.__dict__["orig"])}


bp_signup_company = Blueprint('bp_signup_company', __name__, url_prefix='/signup')
@bp_signup_company.route('/company', methods=['POST'])
def signup_comp():

    checked_data = CompanyDataSignUpVerification(request.get_json()).__dict__
    if checked_data['can_register'] == False:
        return checked_data


    if UserModel.query.filter_by(email=checked_data['try_register']['email']).first():
        return jsonify({"message": "Email allready taken"})


    if checked_data['can_register'] == True:
        user_data = checked_data['try_register']

        company = UserModel(
            iscompany="True",
            name=user_data["name"],
            email=user_data["email"],
            password=user_data['password'],
            phone=user_data["phone"],
            address=user_data["address"],
            city=user_data["city"],
            state=user_data["state"],
            cpf_cnpj=user_data["cpf/cnpj"],
            schedule=user_data["schedule"],
            description=user_data["description"],
        )

        try:
            session = current_app.db.session
            session.add(company)
            session.commit()
            return {"status": "User created"}
        except Exception as e:
            return {"status": str(e.__dict__["orig"])}
