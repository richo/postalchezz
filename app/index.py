from utils import ChezzHandler

class Index(ChezzHandler):

    def get(self):
        self.render("views/index.html")
