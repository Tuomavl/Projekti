from flask import Flask, render_template, request
app = Flask(__name__)

result = []

@app.route('/', methods=["GET","POST"])
def home():
    result.append(request.form)
    print(request.form.get('search-box'))
    return render_template('Kirjaudu.html')
print(result)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
