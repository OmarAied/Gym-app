from flask import Blueprint 
#Stores standard routes for the website
views = Blueprint('views', __name__)

@views.route('/')
def home(): #Whenever / is typed for url, takes to home
    return "<h1>Test</h1>"

