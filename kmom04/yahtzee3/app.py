#!/usr/bin/env python3
"""
Yahtzee app
"""
# Importera relevanta moduler
import os
import re
import traceback
from flask import Flask, render_template, request, session, redirect, url_for
from src.scoreboard import Scoreboard
from src.hand import Hand

app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))
app.json.sort_keys = False

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
    if 'started' not in session:
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
        no_rolls=0
        session["started"]='yes'
        h1=Hand()
        session["dice"]=h1.to_list()
        sb1=Scoreboard.from_dict(empty_dict)
        session["number"]=no_rolls
        session["score"]=sb1.to_dict()
        end_rolls1=''
        session["no_more_rolls"]=''
        print(end_rolls1)
        return render_template("index.html",handen=h1,sb=sb1,end_rolls=end_rolls1)
    empty_dict=session["score"]
    no_rolls=session["number"]
    h1=Hand(session["dice"])
    sb1=Scoreboard.from_dict(session["score"])
    end_rolls1=session.get('no_more_rolls')
    #print(end_rolls1)
    return render_template("index.html",handen=h1,sb=sb1,end_rolls=end_rolls1)

@app.route("/roll_dice", methods=["POST"])
def roll_dice():
    """ Route for roll the dice """
    #print(request.form)
    no_rolls=session['number']
    no_rolls+=1
    if no_rolls>=3:
        #print("Too many tries!")
        session['no_more_rolls']='No more rolls!'
    else:
        h1=Hand(session["dice"])
        dice_choosen=[]
        if request.form.get('die1')=='on':
            dice_choosen.append(0)
        if request.form.get('die2')=='on':
            dice_choosen.append(1)
        if request.form.get('die3')=='on':
            dice_choosen.append(2)
        if request.form.get('die4')=='on':
            dice_choosen.append(3)
        if request.form.get('die5')=='on':
            dice_choosen.append(4)
        h1.roll(dice_choosen)
        #print(dice_choosen)
        #sb1=Scoreboard.from_dict(session["score"])
        session['dice']=h1.to_list()
        session['number']=no_rolls
        session['no_more_rolls']=''
    return redirect(url_for('main'))

@app.route("/score",methods=["POST"])
def score():
    """ Route for lock in score """
    h1=Hand(session["dice"])
    sb1=Scoreboard.from_dict(session["score"])
    sb1.add_points(request.form.get("row"),h1)
    session["score"]=sb1.to_dict()
    session["number"]=1
    h1.roll()
    session["dice"]=h1.to_list()
    session['no_more_rolls']=''
    return redirect(url_for('main'))


@app.route("/reset")
def reset():
    """ Route for reset session """
    """ empty_dict = {
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
    } """
    #sb1=Scoreboard.from_dict(empty_dict)
    _ = [session.pop(key) for key in list(session.keys())]

    return redirect(url_for('main'))


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
