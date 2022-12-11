from flask import Flask,request,render_template

app = Flask(__name__)
Username = []



@app.route('/Alku.html', methods=["GET","POST"])
def start():
    return render_template("Alku.html")

@app.route('/Kirjaudu.html', methods=["GET","POST"])
def kirjaudu():
    username = request.form.get("username")
    Username.append(username)
    return render_template("Kirjaudu.html")

@app.route('/Tarina.html', methods=["GET","POST"])
def tarina():
    return render_template("Tarina.html")

@app.route('/Mapview.html', methods=["GET","POST"])
def mapview():
    return render_template("Mapview.html")

@app.route('/leaderboard.html', methods=["GET","POST"])
def leaderboard():
    return render_template("leaderboard.html")

if __name__ == '__main__':
    app.run(use_reloader=True)