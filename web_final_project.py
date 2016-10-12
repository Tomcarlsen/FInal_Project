from flask import Flask, render_template, request
import giphypop
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
app = Flask(__name__)

#API Key from Giphy
giphy = os.environ['GIPHY_PUBLIC_API']

#adjusting the search (have to fix the search)
search_terms = #["horse", "head", "mask"]
field_keywords = "+".join(search_terms)
url = "http://api.giphy.com/v1/gifs/search?q=" + field_keywords + "api_key=" + giphy

@app.route('/')
def index():
    name = request.values.get('name', 'Nobody')
    greeting = "Hello {}".format(name)
    return render_template('results_true.html', greeting=greeting)

app.run(debug=True)

#@app.route('/about')
#def about():
#    return render_template('about_page.html')

#@app.route('/results')
#def results():
#    stock = request.values.get('stock')
#    price = get_stock_price(stock)
#    return render_template('results.html', price=price)

#Fixing the giphy API

#slack = Slacker(os.environ['SLACK_API_TOKEN'])
#api_key = os.environ['FORECASTIO_API_TOKEN']

#def get_weather(address, api_key):
 #   geolocator = Nominatim()
  #  location = geolocator.geocode(address)
   # if location == None:
    #    return "Location not found."
    #else:
     #   forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude).currently()
      #  return "{} and {} in {} and it is Hillary's fault!".format(forecast.summary, forecast.temperature, location.address)

#print(get_weather("3022 Broadway, NYC", api_key))
#slack.chat.post_message('#bots', get_weather("NYC", api_key), username="Donald", icon_url="http://images.huffingtonpost.com/2016-02-15-1455534387-1672884-nbcfiresdonaldtrumpafterhecallsmexicansrapistsanddrugrunners.jpg")












def get_stock_price(ticker):
    quotes = getQuotes(ticker)
    price = quotes[0]['LastTradePrice']
    return "The price of {} is {}".format(ticker, price)

@app.route('/')
def index():
    name = request.values.get('name', 'Nobody')
    greeting = "Hello {}".format(name)
    return render_template('index.html', greeting=greeting)

@app.route('/about')
def about():
    return render_template('about_page.html')

@app.route('/results')
def results():
    stock = request.values.get('stock')
    price = get_stock_price(stock)
    return render_template('results.html', price=price)

#@app.route('/users/<username>')
#def profile():
#    return render_template('profile.html', user=user)    

app.run(debug=True)



