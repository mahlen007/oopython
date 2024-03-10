#!/usr/bin/env python3
"""
Wordchecker app
"""
# Importera relevanta moduler
import os
import re
import traceback
from flask import Flask, render_template, request, session, redirect, url_for
from src.trie import Trie
import json
#from src.scoreboard import Scoreboard
#from src.hand import Hand
#from src.leaderboard import Leaderboard
#from src.game import Game

app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))
app.json.sort_keys = False

@app.route("/")
def main():
    """ Main route """
    session['spelling_result']=''
    session['filename']="tiny_dictionary.txt"
    session['word']=''
    session['r_word']=''
    #session['removed_words']='test'
    session['removed_words']=json.dumps('')
    return render_template("index.html")

@app.route("/check")#,methods=["POST"])
def check():
    spelling_result=session['spelling_result']
    word=session['word']
    return render_template("check.html",spelling_result=spelling_result,word=word)
    #return render_template("add_result.html")

@app.route("/check_spelling",methods=["POST"])
def check_spelling():
    """ Route for check spelling """
    tr=Trie()
    word=request.form.get("word")
    #if session["filename"]=='':
    filename=session["filename"]
    #else:
    #    filename="tiny_dictionary.txt"
    removed_words=json.loads(session['removed_words']).split(' ')
    word_list=tr.read_from_file(filename)
    tr.insert_from_list(word_list)
    session['spelling_result']=tr.search(word)
    if word in removed_words:
        session['spelling_result']=False

    #print(tr.search(word))
    session['word']=word
    #session["trie"]=tr
    return redirect(url_for('check'))
    #return render_template("leaderboard.html",lb=lb1)

@app.route("/list")#,methods=["POST"])
def list_words():
    """ Route for list the words """
    tr=Trie()
    letter='a'
    #if session["filename"]=='':
    filename=session["filename"]
    #else:
    #    filename="tiny_dictionary.txt"
    word_list=tr.read_from_file(filename)
    tr.insert_from_list(word_list)
    removed_words=json.loads(session['removed_words']).split(' ')
    number_removed=len(removed_words)-1
    return render_template("list.html",trie=tr,letter=letter,removed_w=removed_words,no_removed=number_removed)
    #return render_template("add_result.html",sb=sb1)

@app.route("/remove")#,methods=["POST"])
def remove():
    #tr=Trie()
    #word=request.form.get("word")
    #if session["filename"]=='':
    #filename=session["filename"]
    #else:
    #    filename="tiny_dictionary.txt"
    removed_words=json.loads(session['removed_words']).split(' ')
    #word_list=tr.read_from_file(filename)
    #tr.insert_from_list(word_list)
    #session['spelling_result']=tr.search(word)
    word=session['r_word']
    session['r_word']=''
    
    #if word in removed_words:
    #    session['spelling_result']=False
    #word=request.form.get("word")
    spelling_result=session['spelling_result']
    print(spelling_result)
    return render_template("remove.html",spelling_result=spelling_result,word=word,removed_words=removed_words)
    #return render_template("add_result.html",sb=sb1)

@app.route("/remove_word",methods=["POST"])
def remove_word():
    """ Route for add result to Leaderboard """
    tr=Trie()
    removed_words=[]
    word=request.form.get("remove_word")
    print(word)
    #if session["filename"]=='':
    filename=session["filename"]
    #else:
    #    filename="tiny_dictionary.txt"
    word_list=tr.read_from_file(filename)
    tr.insert_from_list(word_list)
    sp_result=tr.search(word)
    session['spelling_result']=sp_result
    removed_words=json.loads(session['removed_words']).split(' ')
    if word in removed_words:
        session['spelling_result']=False
    #print(sp_result)
    #print(tr.search(word))
    #session['word']=word
    if sp_result==True:
        removed_words=json.loads(session['removed_words']).split(' ')
        if word not in removed_words: 
            removed_words.append(word)
        session['removed_words']=json.dumps(' '.join(removed_words))
        #print(removed_words)
    session['r_word']=word
    return redirect(url_for('remove'))
    #return render_template("leaderboard.html",lb=lb1)

@app.route("/change")#,methods=["POST"])
def change():
    #if session["filename"]=='':
    filename=session["filename"]
    #else:
    #    filename="tiny_dictionary.txt"
    return render_template("change.html",filename=filename)
    #return render_template("add_result.html",sb=sb1)

@app.route("/change_dictionary",methods=["POST"])
def change_dictionary():
    """ Route for add result to Leaderboard """
    _ = [session.pop(key) for key in list(session.keys())]
    session['spelling_result']=''
    session['filename']="tiny_dictionary.txt"
    session['word']=''
    session['r_word']=''
    session['removed_words']=json.dumps('')
    filename=request.form.get("word_list")
    session['filename']=filename
    
    return redirect(url_for('change'))
    #return render_template("leaderboard.html",lb=lb1)


@app.route("/about")
def about():
    """ About route """
    my_name = "Mattias Ahlén"
    my_course = "OOPython"
    my_acronym = "MADZ21"
    return render_template("about.html", name=my_name, course=my_course, acro=my_acronym)


@app.route("/setup",methods=["POST"])
def setup():
    """ Route for set up game with several players """
    return redirect(url_for('main'))

@app.route("/score",methods=["POST"])
def score():
    """ Route for lock in score in Scoreboard"""
    return redirect(url_for('main'))





@app.route("/show_leaderboard")#,methods=["POST"])
def show_leaderboard():
    """ Route for add score to Scoreboard """
    return render_template("leaderboard.html",lb=lb1)

@app.route("/roll_dice", methods=["POST"])
def roll_dice():
    """ Route for roll the dice """
    return redirect(url_for('main'))



@app.route("/delete_score",methods=["POST"])
def delete_score():
    """ Route for delete score """
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
