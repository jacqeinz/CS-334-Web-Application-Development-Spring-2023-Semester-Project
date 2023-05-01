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
json_url = os.path.join(SITE_ROOT, "defaultData.json")
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
   
# initialize db
    def __init__(sundae, id, name, has_flavors, description, price, data):
        sundae.id = id
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
    
    
# initialize db

    def __init__(cone, id, name, has_flavors, price, data):
        cone.id = id
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
    

# initialize db
    def __init__(bowl, id, name, has_flavors, price, data):
        bowl.id = id
        bowl.name = name
        bowl.has_flavors = has_flavors
        bowl.price = price
        bowl.data = data


#milkshakes
class milkshakes (db.Model):
    id = db.Column('milkshake_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(10))
    price = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
  
    # initialize db
    def __init__(milkshake, id, name, description, price, data):
        milkshake.id = id
        milkshake.name = name
        milkshake.description = description
        milkshake.price = price
        milkshake.data = data


#smoothies table
class smoothies (db.Model):
    id = db.Column('smoothie_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
   
    
    # initialize db
    def __init__(smoothie, id, name, description, price, data):
        smoothie.id = id
        smoothie.name = name
        smoothie.price = price
        smoothie.data = data
  

#frappe table
class frappes (db.Model):
    id = db.Column('frappe_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
 
  
# initialize db
    def __init__(frappe, id, name, price, data):
        frappe.id = id
        frappe.name = name
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


#snowcone
class flavors (db.Model):
    id = db.Column('flavors_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
   
  
# initialize db
    def __init__(flavor, id, name, data):
   #display you can only use 3 flavors
        flavor.id = id
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
    return json.dumps({'data':result_list})

@app.route('/api/getCones')
def get_cones_api():
    results = cones.query.all()
    result_list = []
    for item in results:
        result_list.append({
            "id": item.id,            
            "name": item.name,
            "has_flavors": item.has_flavors,
            'price': item.price,
            'imgSrc': item.data.decode('utf-8')
        })
    return json.dumps({'data':result_list})

@app.route('/api/getSundaes')
def get_sundaes_api():
    results = sundaes.query.all()
    result_list = []
    for item in results:
        result_list.append({
            "id": item.id,
            "name": item.name,
            "has_flavors": item.has_flavors,
            "description": item.description,
            'price': item.price,
            'imgSrc': item.data.decode('utf-8')
        })
    return json.dumps({'data':result_list})

@app.route('/api/getWaffleBowls')
def get_waffles_api():
    results = bowls.query.all()
    result_list = []
    for item in results:
        result_list.append({
            "id": item.id,
            "has_flavors": item.has_flavors,
            "name": item.name,
            "description": item.description,
            'price': item.price,
            'imgSrc': item.data.decode('utf-8')
        })
    return json.dumps({'data':result_list})

@app.route('/api/getSmoothies')
def get_smoothies_api():
    results = smoothies.query.all()
    result_list = []
    for item in results:
        result_list.append({
            "id": item.id,
            "name": item.name,
            'price': item.price,
            'imgSrc': item.data.decode('utf-8')
        })
    return json.dumps({'data':result_list})

@app.route('/api/getMilkshakes')
def get_milkshakes_api():
    results = milkshakes.query.all()
    result_list = []
    for item in results:
        result_list.append({
            "id": item.id,
            "name": item.name,
            "description": item.description,
            'price': item.price,
            'imgSrc': item.data.decode('utf-8')
        })
    return json.dumps({'data':result_list})

@app.route('/api/getFrappe.html')
def get_frappes_api():
    results = frappes.query.all()
    result_list = []
    for item in results:
        result_list.append({
            "id": item.id,
            "name": item.name,
            'price': item.price,
            'imgSrc': item.data.decode('utf-8')
        })
    return json.dumps({'data':result_list})

@app.route('/api/getFlavors')
def get_flavors_api():
    results = flavors.query.all()
    result_list = []
    for item in results:
        result_list.append({
            "id": item.id,
            "name": item.name,
            'imgSrc': item.data.decode('utf-8')
        })
    return json.dumps({'data':result_list})

@app.route('/api/test/resetDbData')
def reset_db_data_api():
    f = open(json_url)
    data = json.load(f)
    for i in data['stores']:
        if i['name'] == 'snowConeType':
            db.session.query(snowcones).delete()
            db.session.commit()
            for item in i['data']:
                snowcone = snowcones(item['id'], item['name'], item['price'], item['description'], item['imgSrc'].encode('utf-8'))
                db.session.add(snowcone)
                db.session.commit()
        if i['name'] == 'sundaeType':
            db.session.query(sundaes).delete()
            db.session.commit()
            for item in i['data']:
                sundae = sundaes(item['id'], item['hasFlavors'], item['name'], item['description'], item['price'], item['imgSrc'].encode('utf-8'))
                db.session.add(sundae)
                db.session.commit()
        if i['name'] == 'coneType':
            db.session.query(cones).delete()
            db.session.commit()
            for item in i['data']:
                cone = cones(item['id'], item['name'], item['has_flavors'], item['price'], item['imgSrc'].encode('utf-8'))
                db.session.add(cone)
                db.session.commit()
        if i['name'] == 'bowlType':
            db.session.query(bowls).delete()
            db.session.commit()
            for item in i['data']:
                bowl = bowls(item['id'], item['name'], item['price'], item['description'], item['imgSrc'].encode('utf-8'))
                db.session.add(bowl)
                db.session.commit()
        if i['name'] == 'milkShakeType':
            db.session.query(milkshakes).delete()
            db.session.commit()
            for item in i['data']:
                milkshake = milkshakes(item['id'], item['name'], item['description'], item['price'],  item['imgSrc'].encode('utf-8'))
                db.session.add(milkshake)
                db.session.commit()
        if i['name'] == 'smoothieType':
            db.session.query(smoothies).delete()
            db.session.commit()
            for item in i['data']:
                smoothie = smoothies(item['id'], item['name'], item['price'], item['imgSrc'].encode('utf-8'))
                db.session.add(smoothie)
                db.session.commit()
        if i['name'] == 'frappeType':
            db.session.query(frappes).delete()
            db.session.commit()
            for item in i['data']:
                frap = frappes(item['id'], item['name'], item['price'], item['imgSrc'].encode('utf-8'))
                db.session.add(frap)
                db.session.commit()
        if i['name'] == 'flavors':
            db.session.query(flavors).delete()
            db.session.commit()
            for item in i['data']:
                flavor = flavors(item['id'], item['name'], item['imgSrc'].encode('utf-8'))
                db.session.add(flavor)
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
   
