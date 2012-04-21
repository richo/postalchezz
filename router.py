import webapp2
import app.index as index

app = webapp2.WSGIApplication([('/', index.App)])
