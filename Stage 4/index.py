from flask import Flask, redirect, abort

app = Flask(__name__)

@app.route("/index.html")
# @app.route("/index")
def index():
    return redirect('/index.html')

@app.route('/milkshakes.html')
def milkshakes():
    return redirect('/milkshakes.html')

@app.route('/sundaes.html')
def sundaes():
    return redirect('/sundaes.html')

@app.route('/snowcones.html')
def snowcones():
    return redirect('/snowcones.html')

if __name__ == '__main__':
    app.run(debug=True)
    