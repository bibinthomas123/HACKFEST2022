from geopy.geocoders import Nominatim
import requests
import json
import time
from django.shortcuts import render
from flask import Blueprint, render_template
from datetime import date
from test import *
from datetime import date, datetime

views = Blueprint('views', __name__)


@views.route('/')
def home():
    Y = date.today().year    # dummy leap year to allow input X-02-29 (leap day)
    seasons = [('winter', (date(Y,  1,  1),  date(Y,  2, 20))),
            ('summer', (date(Y,  3, 21),  date(Y,  4, 20))),
            ('Rainy', (date(Y,  6, 21),  date(Y,  9, 22))),
            ('autumn', (date(Y,  9, 23),  date(Y, 12, 20))),
            ('winter', (date(Y, 12, 21),  date(Y, 12, 31)))]

    def get_season(now):
        if isinstance(now, datetime):
          now = now.date()
          now = now.replace(year=Y)
        return next(season for season, (start, end) in seasons
                if start <= now <= end)

    return render_template("Home.html" ,current_season = get_season(date.today()) )


@views.route('/search')
def search():
    return render_template("search.html")


@views.route('/results')
def results():
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode("Hyderabad")
    latitude=  location.latitude
    longitude= location.longitude
    t = time.localtime()
    current_time = time.strftime("%I:%M", t)
    today = date.today()
    d4 = today.strftime("%b-%d-%Y")

    HTML_current_time = str(current_time) + " " + str(d4)
    return render_template("results.html", current_time=HTML_current_time,latitude=latitude,longitude=longitude)


@views.route("/aboutUs")
def aboutUs():
    return render_template("aboutus.html")
