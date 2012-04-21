import webapp2

from templite import Templite

# TODO This could potentially be just a getter instead of a decorator.
# \BENCHMARK
def preload_template(func):
    """ Ensures that the specified view is already compiled and exists in
    the templates hash"""
    def _(self, view_path):
        if view_path not in self.templates:
            self.templates[view_path] = Templite.from_file(view_path)

        return func(self, view_path)
    return _

class ChezzHandler(webapp2.RequestHandler):
    templates = {}

    @preload_template
    def render(self, view_path):
        content = self.templates[view_path](self = self)

        # XXX Kludge?
        # if view_path[-5:] == ".haml":
        #     content = dehamlinate(content)

        self.response.out.write(content)
