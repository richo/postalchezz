from utils import ChezzHandler

class Login(ChezzHandler):
    title = "> Login"

    def get(self):
        self.render("views/login.html")
