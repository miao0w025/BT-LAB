# user.py
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def verify_login(self, username, password):
        return self.username == username and self.password == password
