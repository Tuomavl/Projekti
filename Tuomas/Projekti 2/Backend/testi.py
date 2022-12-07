from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/username', methods = ['GET'])
def username():
    output = request.form.to_dict()
    name = output["name"]






if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

