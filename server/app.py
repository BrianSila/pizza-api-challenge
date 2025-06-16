from flask import Flask
from .config import db
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

from .controllers.restaurant_controller import restaurant_cntrl
from .controllers.pizza_controller import pizza_cntrl
from .controllers.restaurant_pizza_controller import restaurant_pizza_cntrl

app.register_blueprint(restaurant_cntrl)
app.register_blueprint(pizza_cntrl)
app.register_blueprint(restaurant_pizza_cntrl)

if __name__ == '__main__':
    app.run(port=5555, debug=True)