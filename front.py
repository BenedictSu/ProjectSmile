import urllib
import webapp2
import jinja2
import os
import datetime

from google.appengine.api import users

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

# This part for the Home Page
class HomePage(webapp2.RequestHandler):
    """ Handler for the front page."""

    def get(self):
        template = jinja_environment.get_template('Home.html')
        self.response.out.write(template.render())

class MainPage(webapp2.RequestHandler):
    # Main page for those logged in

    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            template_values = {
                'user_mail': users.get_current_user().email(),
                'logout': users.create_logout_url(self.request.host_url),
            }
            template = jinja_environment.get_template('Main.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(self.request.host_url)
			
class AntonymPage(webapp2.RequestHandler):
    # Antonym Template for those logged in

    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            template_values = {
                'user_mail': users.get_current_user().email(),
                'logout': users.create_logout_url(self.request.host_url),
            }
            template = jinja_environment.get_template('AntonymTemplate.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(self.request.host_url)
			
class SimplePage(webapp2.RequestHandler):
    # Simple Template for those logged in

    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            template_values = {
                'user_mail': users.get_current_user().email(),
                'logout': users.create_logout_url(self.request.host_url),
            }
            template = jinja_environment.get_template('SimpleTemplate.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(self.request.host_url)
			
app = webapp2.WSGIApplication([('/', HomePage),
							   ('/main', MainPage),
							   ('/antonym', AntonymPage),
							   ('/simple', SimplePage)],
                              debug=True)
