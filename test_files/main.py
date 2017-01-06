from flask import Flask, render_template, request

app = Flask(__name__)

name = ['Mahesh','Ranaweera','Sachin','Sachith']

#homepage
@app.route('/')
def index():
    return 'This is the homepage'

#mainpage
@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)

#register
@app.route('/register')
def register():
    return render_template("register.html", selected='register', names=name)

@app.route('/register2', methods=['POST'])
def reply():
    name2=request.form['name2']
    return render_template("register2.html", finalname=name2)


if __name__ == "__main__":
    app.run()