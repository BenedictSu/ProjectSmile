import urllib
import webapp2
import jinja2
import os
import datetime

from google.appengine.ext import ndb
from google.appengine.api import users

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

# This part for the Home Page
class HomePage(webapp2.RequestHandler):
    """ Handler for the front page."""

    def get(self):
        template = jinja_environment.get_template('Home.html')
        self.response.out.write(template.render())

# Datastore definitions
class Persons(ndb.Model):
    # Models a person. Key is the email.
    next_item = ndb.IntegerProperty()  # item_id for the next item


class Items(ndb.Model):
    # Models an item with item_link, image_link, description, and date. Key is item_id.
    item_id = ndb.IntegerProperty()
    item_link = ndb.StringProperty()
    image_link = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)		
		
class MainPage(webapp2.RequestHandler):
    # Main page for those logged in
	
    def show(self):
    # Displays the page. Used by both get and post
        user = users.get_current_user()
        if user:  # signed in already

            # Retrieve person
            parent_key = ndb.Key('Persons', users.get_current_user().email())

            # Retrieve items
            query = ndb.gql("SELECT * "
                            "FROM Items "
                            "WHERE ANCESTOR IS :1 "
                            "ORDER BY date DESC",
                            parent_key)

            template_values = {
                'user_mail': users.get_current_user().email(),
                'logout': users.create_logout_url(self.request.host_url),
                'items': query,
            }

            template = jinja_environment.get_template('Main.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(self.request.host_url)

    def get(self):
	    self.show()
		
    def simpleTemplate(self, text):
        r1 = "angry";
        r2 = "sad";
        r3 = "happy";
        database = {};
        database["enraged"] = r1;
        database["annoyed"] = r1;
        database["irritated"] = r1;
        database["furious"] = r1;
        database["outraged"] = r1;
        database["fierce"] = r1;
        database["mad"] = r1;
        database["troubled"] = r1;
        database["melancholic"] = r2;
        database["depressed"] = r2;
        database["crestfallen"] = r2;
        database["sorrowful"] = r2;
        database["bitter"] = r2;
        database["heartbroken"] = r2;
        database["dejected"] = r2;
        database["gloomy"] = r2;
        database["mournful"] = r2;
        database["forlorn"] = r2;
        database["cheerful"] = r3;
        database["delighted"] = r3;
        database["excited"] = r3;
        database["joyful"] = r3;
        database["joyous"] = r3;
        database["glad"] = r3;
        database["blissful"] = r3;
        database["gleeful"] = r3;
        database["contented"] = r3;
        database["jolly"] = r3;
        database["ecstatic"] = r3;
        database["elated"] = r3;
        database["overjoyed"] = r3;
        textArray = text.split();
        changedText = "";
        for x in textArray:
            if (x in database):
                changedText = changedText + database[x] + " ";
            else:	
                changedText = changedText + x + " ";
        return changedText
	
    def antonymTemplate(self, text):
        data = {};
        data["sad"] = "happy";
        data["happy"]="sad";
        data["long"]="short";
        data["short"]="long";
        data["angry"]="calm";
        data["calm"]="angry";
        data["pretty"]="ugly";
        data["ugly"]="pretty";
        data["thin"]="fat";
        data["fat"]="thin";
        data["clever"]="stupid";
        data["stupid"]="clever";
        data["hot"]="cold";
        data["cold"]="hot";
        data["difficult"]="easy";
        data["easy"]="difficult";
        data["courteous"]="rude";
        data["rude"]="courteous";
        data["win"]="lose";
        data["lose"]="win";
        data["pass"]="fail";
        data["fail"]="pass";
        data["big"]="small";
        data["small"]="big";
        data["expensive"]="cheap";
        data["cheap"]="expensive"
        data["slow"]="fast";
        data["fast"]="slow";
        data["deep"]="shallow";
        data["shallow"]="deep";
        data["here"]="there";
        data["there"]="here";
        data["high"]="low";
        data["low"]="high";
        data["old"]="young";
        data["young"]="old";
        textArray = text.split();
        changedText = "";
        for x in textArray:
            if (x in data):
                changedText = changedText + data[x] + " "
            else:	
                changedText = changedText + x + " ";
        return changedText
	
    def post(self):
        # Retrieve person
        parent = ndb.Key('Persons', users.get_current_user().email())
        person = parent.get()
        if person == None:
            person = Persons(id=users.get_current_user().email())
            person.next_item = 1

        item = Items(parent=parent, id=str(person.next_item))
        item.item_id = person.next_item

        item.item_link = self.request.get('text')
        item.image_link = self.request.get('myRadios')
        if item.image_link == '':
            item.image_link = "ALERT: You did not select a template (This is not the changed text!)"
        elif item.image_link == "1":
            item.image_link = self.antonymTemplate(item.item_link)
        else:
            item.image_link = self.simpleTemplate(item.item_link)
        person.next_item += 1
        person.put()
        item.put()
        self.show()
			
# For deleting an item from wish list
class DeleteItem(webapp2.RequestHandler):
    # Delete item specified by user

    def post(self):
        item = ndb.Key('Persons', users.get_current_user().email(), 'Items', self.request.get('itemid'))
        item.delete()
        self.redirect('/main')
			
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
							   ('/deleteitem', DeleteItem),
							   ('/antonym', AntonymPage),
							   ('/simple', SimplePage)],
                              debug=True)
