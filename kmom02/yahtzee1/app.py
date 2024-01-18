#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler
from flask import Flask, render_template
from car import Car
from src.hand import Hand

app = Flask(__name__)

@app.route("/about")
def about():
    """ About route """
    my_car = Car("BMW", 90000)
    my_name = "Mattias Ahlén"
    my_course = "OOPython"
    my_acronym = "MADZ21"
    return render_template("about.html", name=my_name, course=my_course, acro=my_acronym)

@app.route("/")
def main():
    """ Main route """
    hand1=Hand()
    die_list=hand1.dice_name().split(", ")
    die1=die_list[0]
    die1=die_list[0]
    die1=die_list[0]
    die1=die_list[0]
    die1=die_list[0]
    return render_template("index.html",handen=hand1,die1=die_list[0]+'.png',die2=die_list[1]+'.png',die3=die_list[2]+'.png',die4=die_list[3]+'.png',die5=die_list[4]+'.png')

if __name__ == "__main__":
    app.run()

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    app.run(debug=True)