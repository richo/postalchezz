import webapp2
import app.index as index
import app.about as about
import app.contact as contact

app = webapp2.WSGIApplication([('/', index.App)])
app = webapp2.WSGIApplication([('/about', about.App)])
app = webapp2.WSGIApplication([('/contact', contact.App)])
