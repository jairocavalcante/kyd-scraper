import webapp2

class KydIndex(webapp2.RequestHandler):
    def get(self):
        f = open('scraps.yaml')
        self.response.write(f.read())

app = webapp2.WSGIApplication([
    ('/', KydIndex)
], debug=True)
