from utils import ChezzHandler

class About(ChezzHandler):

    def get(self):
        self.render("views/about.html")
