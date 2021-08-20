from flask import Flask,jsonify,render_template
from jinja2 import TemplateNotFound

app = Flask(__name__)

@app.route("/")
def homepage():
    try:
        return render_template("home.html"),200
    except Exception as err:
        return render_template('404.html'),404

@app.route('/<string:fn>') 
def aboutUS(fn):
    try:
        return render_template(fn),200
    except Exception as err:
        return render_template('404.html'),404

if __name__ == '__main__':
    app.run(debug=True) # start flask app 