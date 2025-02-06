from flask import Blueprint, render_template
#Stores standard routes for the website
views = Blueprint('views', __name__)

@views.route('/')
def home(): #Whenever / is typed for url, takes to home
    return render_template("home.html") #Renders home.html

