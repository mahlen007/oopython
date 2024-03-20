#!/usr/bin/env python3
"""
Wordchecker app
"""
# Importera relevanta moduler
import os
import re
import traceback
import json
from flask import Flask, render_template, request, session, redirect, url_for
from src.trie import Trie
from src.errors import SearchMiss

app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))
app.json.sort_keys = False

@app.route("/")
def main():
    """ Main route """
    reset_session()
    return render_template("index.html")

@app.route("/check")
def check():
    """ Route for check spelling """
    if session['from_check_spelling']:
        spelling_result=session['spelling_result']
        word=session['word']
        session['from_check_spelling']=False
    else:
        spelling_result=''
        word=''
    return render_template("check.html",spelling_result=spelling_result,word=word)

@app.route("/check_spelling",methods=["POST"])
def check_spelling():
    """ Route for check spelling """
    word=request.form.get("word")
    filename=session["filename"]
    removed_words=json.loads(session['removed_words']).split(' ')
    tr=Trie.create_from_file(filename)
    try:
        session['spelling_result']=tr.search(word)
    except SearchMiss:
        session['spelling_result']=False
    if word in removed_words:
        session['spelling_result']=False
    session['word']=word
    session['from_check_spelling']=True
    return redirect(url_for('check'))

@app.route("/prefix")
def prefix():
    """ Route for prefix search """
    if session['from_check_prefix']:
        prefix_result=session['prefix_result']
        pre_l=session['prefix_list']
        word=session['word']
        session['from_check_prefix']=False
    else:
        prefix_result=''
        pre_l=[]
        word=''
    return render_template("prefix.html",prefix_result=prefix_result,word=word,prefix_list=pre_l)

@app.route("/check_prefix",methods=["POST"])
def check_prefix():
    """ Route for check prefix """
    word=request.form.get("word")
    filename=session["filename"]
    removed_words=json.loads(session['removed_words']).split(' ')
    tr=Trie.create_from_file(filename)
    session['prefix_list']=tr.prefix_search(word)
    if word in removed_words:
        session['spelling_result']=False
    session['word']=word
    session['from_check_prefix']=True
    return redirect(url_for('prefix'))


@app.route("/list")
def list_words():
    """ Route for list the words """
    ch='a'
    filename=session["filename"]
    tr=Trie.create_from_file(filename)
    removed_words=json.loads(session['removed_words']).split(' ')
    nr_rem=len(removed_words)-1
    return render_template("list.html",trie=tr,letter=ch,removed_w=removed_words,no_removed=nr_rem)

@app.route("/remove")
def remove():
    """ Route for remove word """
    removed_w=json.loads(session['removed_words']).split(' ')
    word=session['r_word']
    session['r_word']=''
    s_result=session['spelling_result']
    return render_template("remove.html",spelling_result=s_result,word=word,removed_words=removed_w)

@app.route("/remove_word",methods=["POST"])
def remove_word():
    """ Route for add result to Leaderboard """
    removed_words=[]
    word=request.form.get("remove_word")
    print(word)
    filename=session["filename"]
    tr=Trie.create_from_file(filename)
    sp_result=tr.search(word)
    session['spelling_result']=sp_result
    removed_words=json.loads(session['removed_words']).split(' ')
    if word in removed_words:
        session['spelling_result']=False
    if sp_result is True:
        removed_words=json.loads(session['removed_words']).split(' ')
        if word not in removed_words:
            tr.delete(word)
            removed_words.append(word)
        session['removed_words']=json.dumps(' '.join(removed_words))
    session['r_word']=word
    return redirect(url_for('remove'))

@app.route("/change")
def change():
    """ Change dictionary """
    filename=session["filename"]
    return render_template("change.html",filename=filename)

@app.route("/change_dictionary",methods=["POST"])
def change_dictionary():
    """ Route for change dictionary """
    _ = [session.pop(key) for key in list(session.keys())]
    reset_session()
    filename=request.form.get("word_list")
    session['filename']=filename
    return redirect(url_for('change'))

@app.route("/redovisning")
def redovisning():
    """ Route for Redovisning """
    return render_template("redovisning.html")


def reset_session():
    """ Reset session """
    session['spelling_result']=''
    session['filename']="frequency.txt"
    session['word']=''
    session['r_word']=''
    session['prefix_result']=''
    session['prefix_list']=''
    session['from_check_spelling']=False
    session['from_check_prefix']=False
    session['removed_words']=json.dumps('')


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
