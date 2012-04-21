import webapp2
import app as chezz_app

app = webapp2.WSGIApplication([
  ('/',         chezz_app.Index),
  ('/about',    chezz_app.About),
  ('/contact',  chezz_app.Contact)
])
