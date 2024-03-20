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

@app.route("/check")#,methods=["POST"])
def check():
    """ Route for check spelling """
    spelling_result=session['spelling_result']
    word=session['word']
    return render_template("check.html",spelling_result=spelling_result,word=word)
    #return render_template("add_result.html")

@app.route("/check_spelling",methods=["POST"])
def check_spelling():
    """ Route for check spelling """
    #tr=Trie()
    word=request.form.get("word")
    #if session["filename"]=='':
    filename=session["filename"]
    #else:
    #    filename="tiny_dictionary.txt"
    removed_words=json.loads(session['removed_words']).split(' ')
    ##word_list=tr.create_from_file(filename)
    #tr.insert_from_list(word_list)
    #tr.create_from_file(filename)
    tr=Trie.create_from_file(filename)
    try:
        session['spelling_result']=tr.search(word)
    except SearchMiss:
        session['spelling_result']=False
    if word in removed_words:
        session['spelling_result']=False

    #print(tr.search(word))
    session['word']=word
    #session["trie"]=tr
    return redirect(url_for('check'))
    #return render_template("leaderboard.html",lb=lb1)

@app.route("/prefix")#,methods=["POST"])
def prefix():
    """ Route for prefix search """
    prefix_result=session['prefix_result']
    pre_l=session['prefix_list']
    word=session['word']
    backg='.bg-danger'
    return render_template("prefix.html",prefix_result=prefix_result,word=word,prefix_list=pre_l,backg=backg)

@app.route("/check_prefix",methods=["POST"])
def check_prefix():
    """ Route for check prefix """
    #tr=Trie()
    word=request.form.get("word")
    #if session["filename"]=='':
    filename=session["filename"]
    #else:
    #    filename="tiny_dictionary.txt"
    removed_words=json.loads(session['removed_words']).split(' ')
    #word_list=tr.read_from_file(filename)
    #tr.insert_from_list(word_list)
    tr=Trie.create_from_file(filename)
    session['prefix_list']=tr.prefix_search(word)
    #session['spelling_result']=tr.search(word)
    if word in removed_words:
        session['spelling_result']=False

    #print(tr.search(word))
    session['word']=word
    #session["trie"]=tr
    return redirect(url_for('prefix'))
    #return render_template("leaderboard.html",lb=lb1)


@app.route("/list")#,methods=["POST"])
def list_words():
    """ Route for list the words """
    #tr=Trie()
    ch='a'
    #if session["filename"]=='':
    filename=session["filename"]
    #else:
    #    filename="tiny_dictionary.txt"
    tr=Trie.create_from_file(filename)
    #word_list=tr.read_from_file(filename)
    #tr.insert_from_list(word_list)
    removed_words=json.loads(session['removed_words']).split(' ')
    nr_rem=len(removed_words)-1
    return render_template("list.html",trie=tr,letter=ch,removed_w=removed_words,no_removed=nr_rem)
    #return render_template("add_result.html",sb=sb1)

@app.route("/remove")#,methods=["POST"])
def remove():
    """ Route for remove word """
    #tr=Trie()
    #word=request.form.get("word")
    #if session["filename"]=='':
    #filename=session["filename"]
    #else:
    #    filename="tiny_dictionary.txt"
    removed_w=json.loads(session['removed_words']).split(' ')
    #word_list=tr.read_from_file(filename)
    #tr.insert_from_list(word_list)
    #session['spelling_result']=tr.search(word)
    word=session['r_word']
    session['r_word']=''
    #if word in removed_words:
    #    session['spelling_result']=False
    #word=request.form.get("word")
    s_result=session['spelling_result']
    print(s_result)
    return render_template("remove.html",spelling_result=s_result,word=word,removed_words=removed_w)
    #return render_template("add_result.html",sb=sb1)

@app.route("/remove_word",methods=["POST"])
def remove_word():
    """ Route for add result to Leaderboard """
    #tr=Trie()
    removed_words=[]
    word=request.form.get("remove_word")
    print(word)
    #if session["filename"]=='':
    filename=session["filename"]
    #else:
    #    filename="tiny_dictionary.txt"
    #word_list=tr.read_from_file(filename)
    #tr.insert_from_list(word_list)
    tr=Trie.create_from_file(filename)
    sp_result=tr.search(word)
    session['spelling_result']=sp_result
    removed_words=json.loads(session['removed_words']).split(' ')
    if word in removed_words:
        session['spelling_result']=False
    #print(sp_result)
    #print(tr.search(word))
    #session['word']=word
    if sp_result is True:
        removed_words=json.loads(session['removed_words']).split(' ')
        if word not in removed_words:
            tr.delete(word)
            removed_words.append(word)
        session['removed_words']=json.dumps(' '.join(removed_words))
        #print(removed_words)
    session['r_word']=word
    return redirect(url_for('remove'))
    #return render_template("leaderboard.html",lb=lb1)

@app.route("/change")#,methods=["POST"])
def change():
    """ Change dictionary """
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
    reset_session()
    #session['spelling_result']=''
    #session['filename']="tiny_dictionary.txt"
    #session['word']=''
    #session['r_word']=''
    #session['removed_words']=json.dumps('')
    filename=request.form.get("word_list")
    session['filename']=filename

    return redirect(url_for('change'))
    #return render_template("leaderboard.html",lb=lb1)

def reset_session():
    """ Reset session """
    session['spelling_result']=''
    session['filename']="tiny_frequency.txt"
    session['word']=''
    session['r_word']=''
    session['prefix_result']=''
    session['prefix_list']=''
    #session['removed_words']='test'
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
