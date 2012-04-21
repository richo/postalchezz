from utils import ChezzHandler

class Index(ChezzHandler):
    about = "> Index"

    def get(self):
        self.render("views/index.html")
