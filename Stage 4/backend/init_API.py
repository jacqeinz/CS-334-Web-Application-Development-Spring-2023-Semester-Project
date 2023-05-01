# config.py #app.py #


from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import Column, ForeignKey, Integer, Unicode
from sqlalchemy.orm import relationship
from socket import gethostname

import json
# tells flask where to put static files
# COLLECT_STATIC_ROOT = os.path.dirname(__file__) + '/static'
# COLLECT_STORAGE = 'flask_collect.storage.file'

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
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
    has_flavors = db.Column(db.String(10))
    description = db.Column(db.String(50))
    price = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)#Data to render the pic in browser

# initialize db
def __init__(sundae, name, has_flavors, description, price, data):
   sundae.name = name
   sundae.has_flavors = has_flavors
   sundae.description = description
   sundae.price = price
   sundae.data = data

#cones
class cones (db.Model):
    id = db.Column('cone_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    has_flavors = db.Column(db.String(10))
    price = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)#Data to render the pic in browser

    
# initialize db

def __init__(cone, name, has_flavors, price, data):
   cone.name = name
   cone.has_flavors = has_flavors
   cone.price = price
   cone.data = data



#bowls
class bowls(db.Model):
    id = db.Column('bowl_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    has_flavors = db.Column(db.String(10))
    price = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)#Data to render the pic in browser

# initialize db
def __init__(bowl, name, has_flavors, price, data):
   bowl.name = name
   bowl.has_flavors = has_flavors
   bowl.price = price
   bowl.data = data


#milkshakes
class milkshakes (db.Model):
    id = db.Column('milkshake_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    has_flavors = db.Column(db.String(10))
    price = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)#Data to render the pic in browser
    # initialize db
    def __init__(milkshake, name, has_flavors, price, data):
        milkshake.name = name
        milkshake.has_flavors = has_flavors
        milkshake.price = price
        milkshake.data = data


#smoothies table
class smoothies (db.Model):
    id = db.Column('smoothie_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    has_flavors = db.Column(db.String(10))
    price = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)#Data to render the pic in browser
    
    # initialize db
    def __init__(smoothie, name, has_flavors, price, data):
        smoothie.name = name
        smoothie.has_flavors = has_flavors
        smoothie.price = price
        smoothie.data = data
  

#frappe table
class frappes (db.Model):
    id = db.Column('frappe_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    has_flavors = db.Column(db.String(10))
    price = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)#Data to render the pic in browser
  
# initialize db
def __init__(frappe, name, has_flavors, price, data):
   frappe.name = name
   frappe.has_flavors = has_flavors
   frappe.price = price
   frappe.data = data


#snowcone
class snowcones (db.Model):
    id = db.Column('snowcone_id', db.String(50), primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.String(50))
    description = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download

    # initialize db
    def __init__(snowcone, id, name, price, description, data):
        snowcone.id = id
        snowcone.name = name
        snowcone.price = price
        snowcone.description = description
        snowcone.data = data 
    # def toJson(self):
    #     return json.dumps(self, default=lambda o: o.__dict__)



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


@app.route('/api/getSnowcones')
def get_snowcones_api():
    results = snowcones.query.all()
    result_list = []
    for item in results:
        result_list.append({
            "id": item.id,
            "name": item.name,
            "description": item.description,
            'price': item.price,
            'imgSrc': item.data.decode('utf-8')
        })
    return json.dumps(result_list)

@app.route('/api/test/resetDbData')
def reset_db_data_api():
    f = open(SITE_ROOT+'\defaultData.json')
    data = json.load(f)
    for i in data['stores']:
        if i['name'] == 'snowConeType':
            db.session.query(snowcones).delete()
            db.session.commit()
            for item in i['data']:
                snowcone = snowcones(item['id'], item['name'], item['price'], item['description'], item['imgSrc'].encode('utf-8'))
                db.session.add(snowcone)
                db.session.commit()
    return jsonify({'dbreset':'success'})

    


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
    if 'liveconsole' not in gethostname():
        app.run(debug = True)
   
