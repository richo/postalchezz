import webapp2

from templite import Templite

class ChezzHandler(webapp2.RequestHandler):
    templates = {}

    def render(self, view_path, **context):
        context.update({"self": self})
        template = self.get_template(view_path)

        content = template(context)

        # XXX Kludge?
        # if view_path[-5:] == ".haml":
        #     content = dehamlinate(content)

        self.response.out.write(content)

    def get_template(self, view_path):
        if view_path not in self.templates:
            self.templates[view_path] = Templite.from_file(view_path)
        return self.templates[view_path]
