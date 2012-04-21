from utils import ChezzHandler
import models

class Register(ChezzHandler):

    def get(self):
        self.render("views/register.html")

    def post(self):
        required_feilds = ["email", "password"]
        for field in required_feilds:
          if not self.request.get(field):
            return self.render("views/register.html", invalid = True)

        new_user = models.user.new(
            email=self.request.get("email"),
            password=self.hash(self.request.get("password"))
        )

        if not new_user:
            return self.render("views/register.html", username_taken=True)

        self.render("views/about", username=new_user.email)

    ## def post





