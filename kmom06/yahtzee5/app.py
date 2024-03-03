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
from src.leaderboard import Leaderboard
from src.game import Game

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
    if 'players' not in session:
        no_rolls=0
        session["started"]='yes'
        session["highest_score"]=''
        session["highest_score_owner"]=''
        h1=Hand()
        session["dice"]=h1.to_list()
        session["number"]=no_rolls
        end_rolls1=''
        session["no_more_rolls"]=''
        session["round"]=[]
        return render_template("start.html")
    game=Game()
    game.players.from_list(session["players"])
    playerinfo=session["player_turn"]
    no_rolls=session["number"]
    h1=Hand(session["dice"])
    sb1=Scoreboard.from_dict(session["score"])
    end_rolls1=session.get('no_more_rolls')
    return render_template("index.html",handen=h1,sb=sb1,end_rolls=end_rolls1,player=playerinfo)

@app.route("/setup",methods=["POST"])
def setup():
    """ Route for set up game with several players """
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
    no_players=int(request.form.get("no_players"))
    game=Game()
    #rolls=0
    for x in range(no_players):
        #print("for-loop"+str(x))
        sb=Scoreboard.from_dict(empty_dict)
        game.players.enqueue((int(x+1),sb.to_dict()))
        #print(game.players.size())
    player_tuple=game.players.dequeue()
    player_turn=player_tuple[0]
    session["player_turn"]=player_turn
    session["score"]=player_tuple[1]
    session["players"]=game.players.to_list()
    return redirect(url_for('main'))

@app.route("/score",methods=["POST"])
def score():
    """ Route for lock in score in Scoreboard"""
    h1=Hand(session["dice"])
    sb1=Scoreboard.from_dict(session["score"])
    game=Game()
    game.players.from_list(session["players"])
    sb1.add_points(request.form.get("row"),h1)
    session["score"]=sb1.to_dict()
    session["number"]=1
    player_turn=session["player_turn"]

    if sb1.finished() is False: ### Ändras vid testning
        game.players.enqueue((int(player_turn),sb1.to_dict()))
        h1.roll()
        session["dice"]=h1.to_list()
        session['no_more_rolls']=''
        player_tuple=game.players.dequeue()
        session["score"]=player_tuple[1]
        session["player_turn"]=player_tuple[0]
        session["players"]=game.players.to_list()
    else:
        game.round_score=session["round"]
        game.round_score.append((player_turn,sb1.get_total_points()))
        session["round"]=game.round_score

        if game.players.is_empty():
            session["players"]=game.players.to_list()
            return redirect(url_for('add_score'))
        player_tuple=game.players.dequeue()
        session["player_turn"]=player_tuple[0]
        session["score"]=player_tuple[1]
        session["players"]=game.players.to_list()
        h1.roll()
        session["dice"]=h1.to_list()
        return redirect(url_for('main'))
    return redirect(url_for('main'))

@app.route("/add_score")#,methods=["POST"])
def add_score():
    """ Route for add score to Scoreboard """
    #sb1=Scoreboard.from_dict(session["score"])
    game=Game()
    game.players.from_list(session["players"])
    game.round_score_from_list(session["round"])
    return render_template("add_result.html",gm=game)
    #return render_template("add_result.html",sb=sb1)

@app.route("/add_result",methods=["POST"])
def add_result():
    """ Route for add result to Leaderboard """
    sb1=Scoreboard.from_dict(session["score"])
    score_=sb1.get_total_points()
    name=request.form.get("fname")
    lb1=Leaderboard()
    lb1.load("score.json")
    lb1.add_entry(score_,name)
    #lb1.sort()
    lb1.save("score.json")
    return redirect(url_for('show_leaderboard'))
    #return render_template("leaderboard.html",lb=lb1)

@app.route("/show_leaderboard")#,methods=["POST"])
def show_leaderboard():
    """ Route for add score to Scoreboard """
    lb1=Leaderboard()
    lb1.load("score.json")
    #print(lb1.ul.size())
    lb1.sort()
    return render_template("leaderboard.html",lb=lb1)

@app.route("/roll_dice", methods=["POST"])
def roll_dice():
    """ Route for roll the dice """
    no_rolls=session['number']
    no_rolls+=1
    if no_rolls>=3:
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
        session['dice']=h1.to_list()
        session['number']=no_rolls
        session['no_more_rolls']=''
    return redirect(url_for('main'))



@app.route("/delete_score",methods=["POST"])
def delete_score():
    """ Route for delete score """
    lb1=Leaderboard()
    lb1.load("score.json")
    lb1.sort()
    #print(request.form.get("row"))
    lb1.remove_entry(int(request.form.get("row")))
    lb1.save("score.json")
    return render_template("leaderboard.html",lb=lb1)


@app.route("/reset")
def reset():
    """ Route for reset session """
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
