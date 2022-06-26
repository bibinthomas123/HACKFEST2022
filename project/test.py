
# key ="TxwE4e9Bh5MGvlLIQDJmyfcD1xuIwfn4"
# location ="Balanagar"
# url= "http://www.mapquestapi.com/geocoding/v1/address?key="+key+"&location="+location
# req = requests.get(url)
# data = req.json()['results'][0]
# location = data["locations"][0]
# print(location)


# from datetime import date, datetime

# Y = date.today().year    # dummy leap year to allow input X-02-29 (leap day)
# seasons = [('winter', (date(Y,  1,  1),  date(Y,  3, 20))),
#            ('spring', (date(Y,  3, 21),  date(Y,  6, 20))),
#            ('summer', (date(Y,  6, 21),  date(Y,  9, 22))),
#            ('autumn', (date(Y,  9, 23),  date(Y, 12, 20))),
#            ('winter', (date(Y, 12, 21),  date(Y, 12, 31)))]

# def get_season(now):
#     if isinstance(now, datetime):
#         now = now.date()
#     now = now.replace(year=Y)
#     return next(season for season, (start, end) in seasons
#                 if start <= now <= end)


# return(get_season())

#API  microsoft

#https://api.msn.com/weather/current?latLongList=28.652%2C77.2315%7C18.969%2C72.8212%7C17.366%2C78.476%7C12.9767%2C77.5753%7C22.5656%2C88.3702&locale=en-in&units=C&appId=9e21380c-ff19-4c78-b4ea-19558e93a5d3&apiKey=j5i4gDqHL6nGYwx5wi5kRhXjtf2c5qgFX9fzfk0TOo&ocid=msftweather&wrapOData=false


# address = "plot no 70, flat no 302 ,sri sainath aashray,padmanagar phase 1,chintal"

# params={
#     'key':api_key,
#     'address':address
# }

# response = requests.get(base_url, params=params)

# data = response.json()
# print(data)


import requests


address ="padmanagar phase 1,chintal"
API_KEY = 'AIzaSyB8uwWqb4hpqj_NetvyPeU4HObmvW8xj6s'


params = {
        'key': API_KEY,
        'address': address.replace(' ', '+')
}
     
base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
response = requests.get(base_url, params=params)
data = response.json()
print(data)
    
    

