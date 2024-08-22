from flask import Flask,render_template
import random
app = Flask(__name__,
template_folder='templates',
static_folder='static')

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/fortune')
def fortune():
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
    return render_template("fortune.html", fortune=selected_fortune)



 























if __name__ == '__main__':
    app.run(debug = True)