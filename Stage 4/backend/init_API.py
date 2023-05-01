# config.py #app.py #


from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import Column, ForeignKey, Integer, Unicode
from sqlalchemy.orm import relationship

import json
# tells flask where to put static files
# COLLECT_STATIC_ROOT = os.path.dirname(__file__) + '/static'
# COLLECT_STORAGE = 'flask_collect.storage.file'

#SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
#json_url = os.path.join(SITE_ROOT, "static", "defaultData.json")
#data = json.load(open(json_url))
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///defaultData.db'
app.config['SECRET_KEY'] = "random string"
# initialize the app with the extension
db = SQLAlchemy(app)
#push context
app.app_context().push()


# tables

#sundaes 
class sundaes (db.Model):
    id = db.Column('sundae_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    hasFlavors = db.Column(db.String(10))
    description = db.Column(db.String(50))
    Price = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)#Data to render the pic in browser

# initialize db
def __init__(sundae, name, hasFlavors, description, Price, data):
   sundae.name = name
   sundae.hasFlavors = hasFlavors
   sundae.description = description
   sundae.Price = Price
   sundae.data = data

#cones
class cones (db.Model):
    id = db.Column('cone_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    hasFlavors = db.Column(db.String(10))
    Price = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)#Data to render the pic in browser

    
# initialize db

def __init__(cone, name, hasFlavors, Price, data):
   cone.name = name
   cone.hasFlavors = hasFlavors
   cone.Price = Price
   cone.data = data



#bowls
class bowls(db.Model):
    id = db.Column('bowl_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    hasFlavors = db.Column(db.String(10))
    Price = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)#Data to render the pic in browser

# initialize db
def __init__(bowl, name, hasFlavors, Price, data):
   bowl.name = name
   bowl.hasFlavors = hasFlavors
   bowl.Price = Price


#milkshakes
class milkshakes (db.Model):
    id = db.Column('milkshake_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    hasFlavors = db.Column(db.String(10))
    Price = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)#Data to render the pic in browser
  
# initialize db
def __init__(milkshake, name, hasFlavors, Price, data):
   milkshake.name = name
   milkshake.hasFlavors = hasFlavors
   milkshake.Price = Price
   milkshake.data = data


#smoothies table
class smoothies (db.Model):
    id = db.Column('smoothie_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    hasFlavors = db.Column(db.String(10))
    Price = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)#Data to render the pic in browser
    
# initialize db
def __init__(smoothie, name, hasFlavors, Price, data):
   smoothie.name = name
   smoothie.hasFlavors = hasFlavors
   smoothie.Price = Price
   smoothie.data = data
  

#frappe table
class frappes (db.Model):
    id = db.Column('frappe_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    hasFlavors = db.Column(db.String(10))
    Price = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)#Data to render the pic in browser
  
# initialize db
def __init__(frappe, name, hasFlavors, Price, data):
   frappe.name = name
   frappe.hasFlavors = hasFlavors
   frappe.Price = Price
   frappe.data = data


#snowcone
class snowcones (db.Model):
    id = db.Column('snowcone_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    hasFlavors = db.Column(db.String(10))
    Price = db.Column(db.String(50))
    description = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)#Data to render the pic in browser

# initialize db
def __init__(snowcone, name, hasFlavors, Price, description, data):
   snowcone.name = name
   snowcone.hasFlavors = hasFlavors
   snowcone.Price = Price
   snowcone.description = description
   snowcone.data = data 



#snowcone
class flavors (db.Model):
    id = db.Column('flavors_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)#Data to render the pic in browser
  
# initialize db
def __init__(flavor, name, data):
   #display you can only use 3 flavors
   flavor.name = name
   flavor.data = data
 




@app.route('/api/test')
def test_api():
    return jsonify({'test':'success',
                    'anothertest': 'anothersuccess'})


@app.route('/api/getMilkshakes')
def milkshakes_api():
    milkshakes = get_all_milkshakes()
    return jsonify([milkshake.to_json() for milkshake in milkshakes])

# @app.route('/smoothies.html')
# def smoothies_page():
    
#         return render_template('/smoothies.html')

# @app.route('/sundaes.html')
# def sundaes_page():
#         return render_template('/sundaes.html')

# @app.route('/snowcones.html')
# def snowcones_page():
#         return render_template('/snowcones.html')

# @app.route('/frap.html')
# def fraps_page():
#         return render_template('/frap.html')

# @app.route('/wafflebowls.html')
# def wafflebowls_page():
#         return render_template('/wafflebowls.html')

# @app.route('/flavors.html')
# def flavorslist_page():
#         return render_template('/flavors.html')

# @app.route('/cones.html')
# def cones_page():
#         return render_template('/cones.html')

# @app.route('/shoppingcart.html')
# def shoppingcart():
#     return render_template('/shoppingcart.html')



# myId = 'abc123'
# @app.route('/managerPortalLogin/<id>')
# def validation(id):
#     if myId != id:
#         abort(404)
#     return f'UserID {id}'


def monitor(function=None):
    @wraps(function)
    def wrapper(*args, **kwargs):
        _ = function(*args, **kwargs)
        print("Ip Address : {} ".format(request.remote_user))
        print("Cookies : {} ".format(request.cookies))
        print(request.user_agent)
        return _
    return wrapper



if __name__ == "__main__":
    #init_db.run()
    db.create_all()
    #create_app.run()
    app.run(debug = True)
   
