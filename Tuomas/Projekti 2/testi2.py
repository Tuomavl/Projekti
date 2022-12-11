from flask import Flask,request,render_template,redirect

app = Flask(__name__)
Username = []



@app.route('/', methods=["GET","POST"])
def start():
    return render_template("Alku.html")

@app.route('/Kirjaudu.html', methods=["GET","POST"])
def kirjaudu():
    username = request.args.get("username")
    Username.append(username)
    redirect("/Tarina.html")
    return render_template("Kirjaudu.html")

@app.route('/Tarina.html', methods=["GET","POST"])
def tarina():
    print(Username)
    return render_template("Tarina.html")

@app.route('/Mapview.html', methods=["GET","POST"])
def mapview():
    return render_template("Mapview.html")

@app.route('/leaderboard.html', methods=["GET","POST"])
def leaderboard():
    return render_template("leaderboard.html")


if __name__ == '__main__':
    app.run(use_reloader=True)