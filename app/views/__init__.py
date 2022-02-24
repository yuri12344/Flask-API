from flask import Flask


def init_app(app: Flask):

    # Signup Client
    from app.views.signups import bp_signup_client
    app.register_blueprint(bp_signup_client)

    # Signup Company
    from app.views.signups import bp_signup_company
    app.register_blueprint(bp_signup_company)

    # Login
    from app.views.login import bp_login
    app.register_blueprint(bp_login)

    # Logout
    from app.views.login import bp_logout
    app.register_blueprint(bp_logout)

