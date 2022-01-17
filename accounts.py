from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager

class User():
    def __init__(self):
        self.db