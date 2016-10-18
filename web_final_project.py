from flask import Flask, render_template, request
import giphypop
import os
#from dotenv import load_dotenv, find_dotenv
#load_dotenv(find_dotenv())
#import urllib,json
app = Flask(__name__)

#API Key from Giphy
#giphy = os.environ['GIPHY_PUBLIC_API']
g = giphypop.Giphy()

#pages
@app.route('/')
def index():
    return render_template('index_final_project.html')

@app.route('/about')
def about():
    return render_template('about_final.html')

@app.route('/search')
def index():
    return render_template('search_panel.html')

@app.route('/results')
def results():
    list_of_gifs = [] # make empty list
    gifs = request.values.get('gif') # You should define search key word as 'gif' on html file.
    results = g.search(gifs) # search gifs and put it into results 

# among results, we need only media url information. And put the information into outcome list that we have created
    for result in results: 
        list_of_gifs.append(result.media_url)
    return render_template('results_true.html', results=list_of_gifs)
# you should match the list name of outcome to the variable that you defined at html file for the result. 

if __name__ == '__main__':
    app.run(debug=True)












