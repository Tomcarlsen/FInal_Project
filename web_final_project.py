from flask import Flask, render_template, request
import giphypop
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import urllib,json
app = Flask(__name__)

#API Key from Giphy
giphy = os.environ['GIPHY_PUBLIC_API']

#pages
@app.route('/')
def index():
    greeting = "Hello gif lover"
    return render_template('index_final_project.html', greeting=greeting)


@app.route('/about')
def about():
    return render_template('about_final.html')

@app.route('/results')
def results():
    gifs = request.values.get('gif')
    url = "http://api.giphy.com/v1/zifs/search?q=" + field_keywords + "api_key=" + giphy
    data = json.loads(urllib.urlopen(url).read())
    
    results = g.search(gifs)

    media_one = results[0]
    media_two = results[2]
    media_four = results[4]
    media_five = results[6]
    media_six = results[8]
    media_seven = results[10]
    media_eight = results[12]
    media_nine = results[14]
    media_ten = results[16]

    url_one = results[1]
    url_two = results[3]
    url_four = results[5]
    url_five = results[7]
    url_six = results[9]
    url_seven = results[11]
    url_eight = results[13]
    url_nine = results[15]
    url_ten = results[17]

   
    return render_template('results_true.html', results=results)#, #price=price)



if __name__ == '__main__':
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












