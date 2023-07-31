
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config['SECRET_KEY'] = '315e2ad883082ffbb4c009a25323c300381e86e57f03b05fe1e2cd824a970318'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://doadmin:AVNS_WqlbQNhW6kkIyWdykb6@db-postgresql-ams3-55936-do-user-7460943-0.b.db.ondigitalocean.com:25060/cryptorates'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
# app.config['MAIL_SERVER'] = 'smtp.hostnet.nl'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'confirm@ticketty.pe'
# app.config['MAIL_PASSWORD'] = 'Coschon32!'
# app.config['MAIL_USERNAME'] = 'tickets@ticketty.pe'
# app.config['MAIL_PASSWORD'] = 'Tischick32!'
mail = Mail(app)
import lischib.routs
