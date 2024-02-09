from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

#this is making the app a flask app
app = Flask(__name__)

#home page
@app.route('/')
#index page
@app.route('/index')
def index():
    return render_template('index.html')
#weather page
@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    
    if not bool(city.strip()):
        city = "Austin"
    
    weather_data = get_current_weather(city)
    
    #city is not found by the API, 200 is a success code abreviated by cod
    if not weather_data['cod'] == 200:
        return render_template('city_not_found.html')
        
    return render_template(
        "weather.html",
        #these variables we're defining are the same ones we would use in the template html document
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port = 8000)