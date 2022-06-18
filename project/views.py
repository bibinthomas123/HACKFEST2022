from django.shortcuts import render
from flask import Blueprint, render_template

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("Home.html")
@views.route('/search')
def search():
    return render_template("search.html")    
@views.route('/results')
def results():
    return render_template("results.html")  

@views.route("/aboutUs")
def aboutUs():
    return render_template("aboutus.html")