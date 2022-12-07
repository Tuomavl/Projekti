from flask import Flask, render_template, request
import json


app = Flask(__name__)


@app.route('/username', methods=["GET","POST"])
def username():
    result = print(request.form.get('search-box'))
    return render_template('Kirjaudu.html'),result

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
