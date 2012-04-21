from utils import ChezzHandler

class Contact(ChezzHandler):

    def get(self):
        self.render("views/contact.html")
