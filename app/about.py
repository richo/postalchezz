from utils import ChezzHandler

class About(ChezzHandler):
    title = "> About"

    def get(self):
        self.render("views/about.html")
