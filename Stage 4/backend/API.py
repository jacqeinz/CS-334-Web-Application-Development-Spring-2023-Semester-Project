from flask import Flask, redirect, abort

app = Flask(__name__)

@app.route('/milkshakes')
def milkshakes_page():
       milkshakes = get_all_milkshakes()
       return jsonify([milkshakes.to_json() for milkshake in milkshakes])

if __name__ == '__main__':
    app.run(debug=True)
