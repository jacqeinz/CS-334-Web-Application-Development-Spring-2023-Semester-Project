import sqlite3
import os.path
import json
from flask import Flask, request, jsonify

# connect to the database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "defaultData.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()

# create a table to store the data
c.execute('CREATE TABLE IF NOT EXISTS IceCream (id TEXT, name TEXT, description TEXT, price REAL, img_src TEXT)')
# load the JSON file
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "defaultData.json")
with open(json_url) as f:
    data = json.load(f)

app = Flask(__name__)

#Code to update an item: 
@app.route('/api/update_item', methods=['POST'])
def update_item():
    global conn
    request_data = request.get_json()
    name = request_data['name']
    new_price = request_data['price']
    new_description = request_data['description']
    new_img_src = request_data['img_src']

    # update the item with the new information
    conn.execute('UPDATE IceCream SET price=?, description=?, img_src=? WHERE name=?',
        (new_price, new_description, new_img_src, name))

    # commit the changes to the database
    conn.commit()

    return jsonify({'success': True})

#Code to add a new item: 
@app.route('/api/add_item', methods=['POST'])
def adde_item():
    global conn
    request_data = request.get_json()
    name = request_data['name']
    new_price = request_data['price']
    new_description = request_data['description']
    new_img_src = request_data['img_src']

    # add the item with the new information
    conn.execute('INSERT INTO IceCream (id, name, description, price, img_src) VALUES (?, ?, ?, ?, ?)',
        (new_price, new_description, new_img_src, name))

    # commit the changes to the database
    conn.commit()

    return jsonify({'success': True})

#Code to delete an item: 
@app.route('/api/delete_item', methods=['POST'])
def delete_item():
    global conn
    request_data = request.get_json()
    name = request_data['name']

    # delete the item from the database
    conn.execute('DELETE FROM IceCream WHERE name=?', (name,))

    # commit the changes to the database
    conn.commit()

    return jsonify({'success': True})



