// API call
let queryUrl = "https://api.openweathermap.org/data/2.5/onecall?";
let lat = "lat=17.489773&";
let lon = "lon=78.461007&";
let apiOptions = "units=metric&exclude=minutely,alerts&";
let apiKey = "appid=dbb76c5d98d5dbafcb94441c6a10236e";
// let file = queryUrl + lat + lon + apiOptions + apiKey;
let file = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyD510cSUK4f64fv3yoiVhaMECtf1L6gItU"

fetch(file)
.then((response) => response.json())
.then((data) => {

console.log(data)

// Weather main data
})