#this is what i got from https://www.youtube.com/watch?v=aDOSQAq8cls
from flask import Flask, render_template

app = Flask(__name__)
ambientTemp=22
targetTemp=25

@app.route('/')
def index():
    return render_template("index.html",amb = ambientTemp, tar = targetTemp)
#@app.route('/about')
#def about() :
#    return render_template("about.html")

if __name__ == "__main__":
    app.run() 