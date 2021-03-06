from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from db import db
from resources.user import UserRegister, UserLogin, User


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'  # could do app.config['JWT_SECRET_KEY'] if we prefer
api = Api(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
