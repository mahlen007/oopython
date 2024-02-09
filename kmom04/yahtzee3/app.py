#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler
import os
import re
import traceback
from flask import Flask, render_template, request, session, redirect, url_for
from src.scoreboard import Scoreboard
from src.hand import Hand

app = Flask(__name__)

@app.route("/about")
def about():
    """ About route """
    my_name = "Mattias Ahlén"
    my_course = "OOPython"
    my_acronym = "MADZ21"
    return render_template("about.html", name=my_name, course=my_course, acro=my_acronym)

@app.route("/")
def main():
    """ Main route """
    hand1=Hand()
    empty_dict = {
        "Ones": -1,
        "Twos": -1,
        "Threes": -1,
        "Fours": -1,
        "Fives": -1,
        "Sixes": -1,
        "Three Of A Kind": -1,
        "Four Of A Kind": -1,
        "Full House": -1,
        "Small Straight": -1,
        "Large Straight": -1,
        "Yahtzee": -1,
        "Chance": -1,
    }
    sb1=Scoreboard.from_dict(empty_dict)
    return render_template("index.html",handen=hand1,sb=sb1)

@app.route("/roll_dice")
def roll_dice():
    print(request.form)

@app.route("/reset")
def reset():
    """ Route for reset session """
    _ = [session.pop(key) for key in list(session.keys())]

    return redirect(url_for('main'))

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
