from utils import ChezzHandler

class Contact(ChezzHandler):
    title = "> Contact"

    def get(self):
        self.render("views/contact.html")
