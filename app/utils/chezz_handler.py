import os
import webapp2

import hashlib

from templite import Templite

from google.appengine.api import users

class ChezzHandler(webapp2.RequestHandler):
    templates = {}
    users = users

    def render(self, view_path, layout="standard", **context):
        header_path = os.path.join("views", "layouts", layout, "header.html")
        footer_path = os.path.join("views", "layouts", layout, "footer.html")

        self.response.out.write(self.include(header_path, **context))
        self.response.out.write(self.include(view_path, **context))
        self.response.out.write(self.include(footer_path, **context))

    def include(self, view_path, **context):

        context.update({"self": self})
        template = self.get_template(view_path)

        content = template(context)

        # XXX Kludge?
        # if view_path[-5:] == ".haml":
        #     content = dehamlinate(content)

        return content

    def get_template(self, view_path):
        if view_path not in self.templates:
            self.templates[view_path] = Templite.from_file(view_path)
        return self.templates[view_path]

    def is_active(self, cls):
        return self.__class__.__name__.lower() == cls

    def logged_in(self):
        return self.request.get("logged_in") or False

    def hash(self, data):
        hasher = hashlib.sha512()
        hasher.update(data)
        return hasher.hexdigest()

    def current_user(self):
        return users.get_current_user()
