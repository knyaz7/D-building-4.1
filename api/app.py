from flask import Flask, request, send_file
from flask_cors import CORS
from database import db
from Controllers.UserController import *
from Controllers.ThemeController import *
from Controllers.MessageController import *
from Controllers.ApplicationController import *
from Controllers.AutoCreditController import *
from Controllers.ConsumerCreditController import *
from Controllers.MortgageController import *
from Controllers.CurrencyExchangeController import *
from Controllers.ContributionController import *
from Controllers.TransactionController import *
from Controllers.AudioController import *

app = Flask(__name__)
CORS(app) # Включаем поддержку CORS для всего приложения

# Настройка подключения к базе данных MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@db:5432/dbuild'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Роуты пользователя
app.route('/api/users/', methods=['GET'])(get_users)
app.route('/api/users/<int:item_id>', methods=['GET'])(get_user)
app.route('/api/users/', methods=['POST'])(add_user)
app.route('/api/users/<int:item_id>', methods=['PUT'])(update_user)

# Роуты темы
app.route('/api/themes/', methods=['GET'])(get_themes)
app.route('/api/themes/<int:item_id>', methods=['GET'])(get_theme)
app.route('/api/themes/', methods=['POST'])(add_theme)
app.route('/api/themes/<int:item_id>', methods=['PUT'])(update_theme)

# Роуты сообщений
app.route('/api/messages/', methods=['GET'])(get_messages)
app.route('/api/messages/<int:item_id>', methods=['GET'])(get_message)
app.route('/api/messages/', methods=['POST'])(add_message)

# Роуты заявок
app.route('/api/applications/', methods=['GET'])(get_applications)
app.route('/api/applications/<int:item_id>', methods=['GET'])(get_application)
app.route('/api/applications/', methods=['POST'])(add_application)
app.route('/api/applications/<int:item_id>', methods=['PUT'])(update_application)

# Роуты автокредитов
app.route('/api/autocredits/', methods=['GET'])(get_autocredits)
app.route('/api/autocredits/<int:item_id>', methods=['GET'])(get_autocredit)
app.route('/api/autocredits/', methods=['POST'])(add_autocredit)
app.route('/api/autocredits/<int:item_id>', methods=['PUT'])(update_autocredit)

# Роуты потребительских кредитов
app.route('/api/consumercredits/', methods=['GET'])(get_consumercredits)
app.route('/api/consumercredits/<int:item_id>', methods=['GET'])(get_consumercredit)
app.route('/api/consumercredits/', methods=['POST'])(add_consumercredit)
app.route('/api/consumercredits/<int:item_id>', methods=['PUT'])(update_consumercredit)

# Роуты потребительских кредитов
app.route('/api/mortgages/', methods=['GET'])(get_mortgages)
app.route('/api/mortgages/<int:item_id>', methods=['GET'])(get_mortgage)
app.route('/api/mortgages/', methods=['POST'])(add_mortgage)
app.route('/api/mortgages/<int:item_id>', methods=['PUT'])(update_mortgage)

# Роуты обмена валюты
app.route('/api/currencyexchanges/', methods=['GET'])(get_currencyexchanges)
app.route('/api/currencyexchanges/<int:item_id>', methods=['GET'])(get_currencyexchange)
app.route('/api/currencyexchanges/', methods=['POST'])(add_currencyexchange)
app.route('/api/currencyexchanges/<int:item_id>', methods=['PUT'])(update_currencyexchange)

# Роуты вклада
app.route('/api/contributions/', methods=['GET'])(get_contributions)
app.route('/api/contributions/<int:item_id>', methods=['GET'])(get_contribution)
app.route('/api/contributions/', methods=['POST'])(add_contribution)
app.route('/api/contributions/<int:item_id>', methods=['PUT'])(update_contribution)

# Роуты переводов
app.route('/api/transactions/', methods=['GET'])(get_transactions)
app.route('/api/transactions/<int:item_id>', methods=['GET'])(get_transaction)
app.route('/api/transactions/', methods=['POST'])(add_transaction)
app.route('/api/transactions/<int:item_id>', methods=['PUT'])(update_transaction)

app.route('/api/converttexttoaudio/', methods=['POST'])(convert_text_to_audio)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
