from flask import Flask,render_template, request, url_for, redirect
import random

app = Flask(__name__,
template_folder='templates',
static_folder='static')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        birthday = request.form['bmonth']

        return redirect(url_for('fortune',
            b = birthday))

@app.route('/fortune/<string:b>', methods=['GET', 'POST'])
def fortune(b):
    fortune = [
    "You will find great success today.",
    "An exciting opportunity is on the horizon.",
    "Your kindness will lead to unexpected rewards.",
    "A thrilling adventure awaits you.",
    "You will overcome a challenge with ease.",
    "A surprise is in store for you.",
    "Your hard work will soon pay off.",
    "You will meet someone special soon.",
    "Expect good news in the near future.",
    "A positive change is coming your way.",
    "you will die",
    " you will marry dima"]
    selected_fortune = random.choice(fortune)
    if 3<= len(b) <=9:
        return render_template("fortune.html", fortune=fortune[len(b)-1])
    else:
        return render_template("home.html")
    return render_template("fortune.html", fortune=fortune[len(b)-1])
   







 























if __name__ == '__main__':
    app.run(debug = True)