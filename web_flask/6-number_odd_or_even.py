#!/usr/bin/python3
""" A script that starts a Flask web application """

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def ctex(text):
    return("C {}".format(text.replace("_", " ")))


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ display “n is a number” only if n is an integer"""
    return("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ display “n is a number” only if n is an integer"""
    return(render_template("5-number.html", n=n))


app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd(n):
    """ display “n is a number” only if n is an integer"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
