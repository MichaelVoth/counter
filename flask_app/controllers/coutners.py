from flask import Flask, render_template, session, redirect, request    #Imports flask functionalilty
from flask_app import app   #Imports flask app


@app.route("/")
def coutner_page():     #adds to the counter every refresh
    if 'count' not in session:  #Creates count in session if none
        session['count'] = 0
    else:
        session['count'] += 1   #adds to session count
    return render_template("index.html")

@app.route('/destroy_session')
def reset_page():       #resets the count
    session.clear()
    return redirect('/')

@app.route('/add')
def add_count():        #adds 2 to the count
    session['count'] += 1
    return redirect('/')

@app.route('/custom', methods=['POST'])
def custom_count():     #adds a custom amount to count
    if request.form['custom_amount'] == "": #ignores if input was empty
        session['count'] -= 1
        return redirect('/')
    session['custom_amount'] = request.form['custom_amount']    #adds form data to session
    session['count'] = int(session['count']-1) + int(session['custom_amount'])  #adds custom amount to session count
    session.pop("custom_amount")    #erases custom amount before redirecting
    return redirect('/')