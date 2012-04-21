from utils import ChezzHandler

class Register(ChezzHandler):

    def get(self):
        self.render("views/register.html")
