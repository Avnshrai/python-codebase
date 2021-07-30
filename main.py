import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello GIIT I am new version of the app')
app = webapp2.WSGIApplication([
    {'/',MainHandler)
], debug=True)
