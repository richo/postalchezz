from utils import ChezzHandler

class App(ChezzHandler):

    def get(self):
        self.render("views/index.html")
