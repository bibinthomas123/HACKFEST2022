from geopy.geocoders import Nominatim
import requests
import json
import time
from django.shortcuts import render
from flask import Blueprint, render_template
from datetime import date


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("Home.html")


@views.route('/search')
def search():
    return render_template("search.html")


@views.route('/results')
def results():



    geolocator = Nominatim(user_agent="MyApp")

    location = geolocator.geocode("Hyderabad")

    latitude=  location.latitude
    longitude= location.longitude
    print(location.latitude)
    print(location.longitude)

    t = time.localtime()
    current_time = time.strftime("%I:%M", t)
    today = date.today()
    d4 = today.strftime("%b-%d-%Y")

    HTML_current_time = str(current_time) + " " + str(d4)
    return render_template("results.html", current_time=HTML_current_time,latitude=latitude,longitude=longitude)


@views.route("/aboutUs")
def aboutUs():
    return render_template("aboutus.html")
