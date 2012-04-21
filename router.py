import webapp2
import app.index as index
import app.about as about
import app.contact as contact

app = webapp2.WSGIApplication([
  ('/', index.App),
  ('/about', about.App),
  ('/contact', contact.App)
])
