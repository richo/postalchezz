from utils import ChezzHandler

class Login(ChezzHandler):

    def get(self):
        self.render("views/login.html")
