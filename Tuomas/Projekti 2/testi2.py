from flask import Flask,request,render_template
from game import Game
app = Flask(__name__)
Username = []
game = Game


@app.route('/')
def start():
    return render_template("Alku.html")

@app.route('/Kirjaudu.html', methods=["GET","POST"])
def Kirjaudu():
    username = request.form.get("username")
    Username.append(username)
    return render_template("Kirjaudu.html")

@app.route('/Tarina.html', methods=["GET","POST"])
def tarina():
    return render_template("Tarina.html")


if __name__ == '__main__':
    app.run(use_reloader=True)