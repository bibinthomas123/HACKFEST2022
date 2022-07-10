from flask import request
import json
import time
from flask import Blueprint, render_template
from datetime import date
from test import *
from datetime import date, datetime
import http.client, urllib.parse
import json

views = Blueprint('views', __name__)



# error handler

@views.errorhandler(404)  # catches the error 404
def error404(error):
    return render_template("error_page.html", error_code=404), 404


@views.errorhandler(500)  # catches the error 404
def error500(error):
    return render_template("error_page.html", error_code=500), 500



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

    return render_template("Home.html", current_season=get_season(date.today()))




@views.route('/search')
def search():
    return render_template("search.html")


@views.route('/results', methods=["POST", "GET"])
def results():
    city_name = None
    if request.method == "POST":
        city_name = request.form.get("text")

    conn = http.client.HTTPConnection('geocode.xyz')

    params = urllib.parse.urlencode({
            'auth': 'YOUR_API_KEY',
            'locate': city_name,
            'region': 'IN',
            'json': 1,
            })

    conn.request('GET', '/?{}'.format(params))
    

    res = conn.getresponse()
    if res.status==200:   #checks the server response code 
        data = res.read()
        json_data = json.loads(data)
        if  json_data["longt"] =="0.00000" and json_data["latt"]=="0.00000":  #if the user enters an invalid place name the api returns lat and lon value as 0.0000 0.0000 
            error = "Invalid place name or Try within India or check the spelling and try again "
            return render_template ("Error.html", error=error ,error_code=404)
        else:
            latitude  = json_data["latt"]
            longitude = json_data["longt"]
            print(data)
    else:
        error404()   
  


    t =time.localtime()
    current_time = time.strftime("%I:%M", t)
    today = date.today()
    d4 = today.strftime("%b-%d-%Y")

    HTML_current_time = str(current_time) + " " + str(d4)

    return render_template("results.html", current_time=HTML_current_time, latitude=latitude, longitude=longitude , city_name=city_name)


@views.route("/aboutUs")
def aboutUs():
    return render_template("aboutus.html")
