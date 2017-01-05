from flask import Flask, render_template

app = Flask(__name__)

#homepage
@app.route('/')
def index():
    return 'This is the homepage'

#mainpage
@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)


if __name__ == "__main__":
    app.run()