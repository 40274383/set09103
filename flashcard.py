from flask import Flask, redirect, url_for, render_template, request

from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
	return redirect(url_for('start'))

@app.route('/start', methods=['GET','POST'])
def start():
    if request.method == "POST":
        if request.form['button'] == "Start":
            return redirect(url_for('card1'))
    return render_template('start.html')

@app.route('/card1', methods=['GET','POST'])
def card1(flashcard=None):
    card1 = {
            'What is Tor?':'Tor is a software used to enable anonymous communication by directing Internet traffic through a overlay network in order to conceal a user\'s location'
            }
    for key, value in card1.items():
        if request.method == "POST":
            if request.form['submit_button'] == "Flip":
                flashcard = str(value)
            elif request.form['submit_button'] == "Next":
                return redirect(url_for('card2'))
        else:
            flashcard = key
    return render_template('project.html', flashcard=flashcard)

@app.route('/card2', methods=['GET','POST'])
def card2(flashcard=None):
    card2 = {"What does HTTP stand for?":"HyperText Transfer Protocol"}
    for key, value in card2.items():
        if request.method == "POST":
            if request.form['submit_button'] == "Flip":
                flashcard = str(value)
            elif request.form['submit_button'] == "Next":
                return redirect(url_for('card3'))
        else:
            flashcard = key
    return render_template('project.html', flashcard=flashcard)

@app.route('/card3', methods=['GET','POST'])
def card3(flashcard=None):
    card3 = {"What is the basic protcol that underpins the web?":"HTTP"}
    for key, value in card3.items():
        if request.method == "POST":
            if request.form['submit_button'] == "Flip":
                flashcard = str(value)
            elif request.form['submit_button'] == "Next":
                return redirect(url_for('card4'))
        else:
            flashcard = key
    return render_template('project.html', flashcard=flashcard)

@app.route('/card4', methods=['GET','POST'])
def card4(flashcard=None):
    card4 = {"What is hypertext?":"Hypertext is text displayed on an electronic display with links to other text"}
    for key, value in card4.items():
        if request.method == "POST":
            if request.form['submit_button'] == "Flip":
                flashcard = str(value)
            elif request.form['submit_button'] == "Next":
                return redirect(url_for('card5'))
        else:
            flashcard = key
    return render_template('project.html', flashcard=flashcard)

@app.route('/card5', methods=['GET','POST'])
def card5(flashcard=None):
    card5 = {"What links hypertext documents?":"Hyperlinks"}
    for key, value in card5.items():
        if request.method == "POST":
            if request.form['submit_button'] == "Flip":
                flashcard = str(value)
            elif request.form['submit_button'] == "Next":
                return redirect(url_for('card6'))
        else:
            flashcard = key
    return render_template('project.html', flashcard=flashcard)

@app.route('/card6', methods=['GET','POST'])
def card6(flashcard=None):
    card6 = {"What port does HTTP run over by default?":"Port 80"}
    for key, value in card6.items():
        if request.method == "POST":
            if request.form['submit_button'] == "Flip":
                flashcard = str(value)
            elif request.form['submit_button'] == "Next":
                return redirect(url_for('card7'))
        else:
            flashcard = key
    return render_template('project.html', flashcard=flashcard)

@app.route('/card7', methods=['GET','POST'])
def card7(flashcard=None):
    card7 = {"HTTP is a stateless protocol. What does this mean?":"That each request is processed without any knowledge of previous pages requested"}
    for key, value in card7.items():
        if request.method == "POST":
            if request.form['submit_button'] == "Flip":
                flashcard = str(value)
            elif request.form['submit_button'] == "Next":
                return redirect(url_for('card8'))
        else:
            flashcard = key
    return render_template('project.html', flashcard=flashcard)

@app.route('/card8', methods=['GET','POST'])
def card8(flashcard=None):
    card8 = {"What layer protocol is HTTP?":"HTTP is an application layer protocol"}
    for key, value in card8.items():
        if request.method == "POST":
            if request.form['submit_button'] == "Flip":
                flashcard = str(value)
            elif request.form['submit_button'] == "Next":
                return redirect(url_for('card9'))
        else:
            flashcard = key
    return render_template('project.html', flashcard=flashcard)

@app.route('/card9', methods=['GET','POST'])
def card9(flashcard=None):
    card9 = {"What does URL stand for?":"Uniform Resource Locator"}
    for key, value in card9.items():
        if request.method == "POST":
            if request.form['submit_button'] == "Flip":
                flashcard = str(value)
            elif request.form['submit_button'] == "Next":
                return redirect(url_for('card10'))
        else:
            flashcard = key
    return render_template('project.html', flashcard=flashcard)

@app.route('/card10', methods=['GET','POST'])
def card10(flashcard=None):
    card10 = {"How many HTTP verbs does the official HTTP Request Method registry list?":"39"}
    for key, value in card10.items():
        if request.method == "POST":
            if request.form['submit_button'] == "Flip":
                flashcard = str(value)
            elif request.form['submit_button'] == "Next":
                return redirect(url_for('end'))
        else:
            flashcard = key
    return render_template('project.html', flashcard=flashcard)

@app.route('/end', methods=['GET','POST'])
def end():
    if request.method == "POST":
        if request.form['restart_button'] == "Restart":
            return redirect(url_for('start'))
    return render_template('end.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
