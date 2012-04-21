import webapp2
import app.index as index
import app.about as about

app = webapp2.WSGIApplication([('/', index.App)])
app = webapp2.WSGIApplication([('/about', about.App)])
