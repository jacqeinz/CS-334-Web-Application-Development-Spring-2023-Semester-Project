import sqlite3
import os.path
import json

# connect to the database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "initData.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()

# create a table to store the data
c.execute('CREATE TABLE IF NOT EXISTS IceCream (id TEXT, name TEXT, description TEXT, price REAL, img_src TEXT)')
# load the JSON file
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "defaultData.json")
with open(json_url) as f:
    data = json.load(f)

# insert the defaultData.json data into the table - excluses employee data w/ if/else statements
for store in data['stores']:
    for item in store['data']:
        if 'description' in item:
            conn.execute('INSERT INTO IceCream (id, name, description, price, img_src) VALUES (?, ?, ?, ?, ?)',
                  (item['id'], item['name'], item['description'], item['price'], item['imgSrc']))
        else:
            if 'price' in item:
                item['description'] = ""
                conn.execute('INSERT INTO IceCream (id, name, description, price, img_src) VALUES (?, ?, ?, ?, ?)',
                    (item['id'], item['name'], item['description'], item['price'], item['imgSrc']))
            elif 'id' in item:
                item['description'] = ""
                item['price'] = ""
                conn.execute('INSERT INTO IceCream (id, name, description, price, img_src) VALUES (?, ?, ?, ?, ?)',
                    (item['id'], item['name'], item['description'], item['price'], item['imgSrc']))


"""# insert a new row into the "IceCream" table
name = 'Vanilla'
price = 2.99
description = 'Classic vanilla flavor'
imgSource = '/strawberry.png'
Type = 'flavor'"""

# commit the changes to the database
conn.commit()

# close the database connection
conn.close()






