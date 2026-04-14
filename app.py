#pip install flask python-dotenv mysql-connector-python
from flask import Flask, redirect, url_for, session, flash
from blueprints.books import noticias_bp
from blueprints.users import users_bp
from blueprints.categories import categories_bp
from blueprints.favorites import favorites_bp
from dotenv import load_dotenv
import os
from functools import wraps

load_dotenv()

app = Flask(__name__)
app.secret_key =  os.getenv("SECRET_KEY") # Necessário para usar o 'flash'


app.register_blueprint(noticias_bp)
app.register_blueprint(users_bp)
app.register_blueprint(categories_bp)
app.register_blueprint(favorites_bp)

@app.route("/")
def index():
    return redirect(url_for("users.cadastrar"))

if __name__ == "__main__":
    app.run(debug=True)
