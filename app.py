from flask import Flask, render_template
from myparser import pictures

app = Flask(__name__)

@app.route("/test")
def hello():
    return render_template('test.html')


@app.route("/")
def gallery():
    return render_template('gallery.html', mypictures = pictures())

if __name__ == "__main__":
    app.run(host='0.0.0.0')