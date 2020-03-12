# ------------------------------------------------------
# Nonogram
# ------------------
# The application outputs a picture made of black and white squares
# based on the user's input which is the size of the picture and the locations of the squares
# the python file handles the logic of the application, gets the input and renders it to the html file

# ------------------------------------------------------
# Author: Maxim pomerants 
# Last update: 01.01.2020
# ------------------------------------------------------
## import webapp2  - Python web framework compatible with Google App Engine
import webapp2
#import Jinja and os libraries
import jinja2
import os

#Load Jinja
jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

# -------------------------------------------------------------
# Main page- the home page of the application. contains name,id, and group name of
# the students and also have 3 links to pictures we were asked to make
# using the show_picture class
# -------------------------------------------------------------

class Main_page(webapp2.RequestHandler):
    # When we receive an HTTP GET request - display the "Get inputs" form
	def get(self):
		# Create a template object
		template = jinja_environment.get_template('main_page.html')

		# Creating an HTML page and response
		self.response.out.write(template.render())

# -----------------------------------------
# class takes an input from the user that will decide how the picture will look:
# size that has the width and height of the picture and pixs which contains only 0 or 1
# and it will put a black square where is 1 and white where is 0

# We will use HTML file to display the values from the users input and
#and we will design it using CSS
# -----------------------------------------


class show_picture(webapp2.RequestHandler):

		# define the method get in our class show_picture -
		# to handle http get requests

	def get(self):
		# get value of the size and pixs parameters
		size = self.request.get("size")
		pixs = self.request.get("pixs")

		# create a list that contains the number of rows and columns of the size input
		better_input = size.split(",")
		#get the number of rows and columns
		rows = int(better_input[0])
		columns = int(better_input[1])

		#empty list where there will be the pixs input so it will be possible to iterate on him
		list_of_pixs=[]

		#filling the list_of_picture list using the list w and the build-in functions split and str
		w= pixs.split(",")
		for j in w:
			list_of_pixs.append(str(j))

		#define a function that will allow to go down a line in the table in html when needed
		#further explanation will be provided in the html file
		def remeinder_of_columns(number):
			# boolean function that tells whether a number is divided by the number of collumns
			#with remainder of 0
			if number % columns==0:
				return True
			else:
				return False

		# Create a template object
		template = jinja_environment.get_template('show_picture.html')

		# Creating a dictionary - for each input parameter of the template, define which object to send
		parameters_for_template = {
			"rows": rows,
			"columns": columns,
			"list_of_pixs": list_of_pixs,
			"remeinder_of_columns": remeinder_of_columns,
		}

		# Creating a HTML page and response
		self.response.out.write(template.render(parameters_for_template))


# --------------------------------------------------
# Routing
# --------
# /            - shows the main page of the application and the needed links
#/show_picture - get the inputed parameters and outputs a picture
# --------------------------------------------------

app = webapp2.WSGIApplication([	('/',               Main_page),
								('/show_picture', show_picture)],
								debug=True)

