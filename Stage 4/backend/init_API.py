# config.py #app.py #


from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import Column, ForeignKey, Integer, String, LargeBinary
from sqlalchemy.orm import relationship
from socket import gethostname
from flask_mail import Mail, Message
import json
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "defaultData.json")
#data = json.load(open(json_url))
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///defaultData.db'
app.config['SECRET_KEY'] = "SECRET_KEY"
# initialize the app with the extension
db = SQLAlchemy(app)
#push context

mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'rollingstoneicecreamenmu@gmail.com'
app.config['MAIL_PASSWORD'] = 'nuxlhzaibxavbszi'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
app.app_context().push()

# tables

#sundaes 
class Sundaes (db.Model):
    id = Column('sundae_id', String(50), primary_key=True)
    has_flavors = Column(String(10))
    name = Column(String(50))
    description = Column(String(50))
    price = Column(String(50))
    data = Column(LargeBinary, nullable=False) #Actual data, needed for Download
   
# initialize db
    def __init__(sundae, id, has_flavors, name, description, price, data):
        sundae.id = id
        sundae.has_flavors = has_flavors
        sundae.name = name
        sundae.description = description
        sundae.price = price
        sundae.data = data

#cones
class Cones (db.Model):
    id = Column('cone_id', String(50), primary_key=True)
    name = Column(String(50))
    has_flavors = Column(String(10))
    price = Column(String(50))
    data = Column(LargeBinary, nullable=False) #Actual data, needed for Download
# initialize db
    def __init__(cone, id, name, has_flavors, price, data):
        cone.id = id
        cone.name = name
        cone.has_flavors = has_flavors
        cone.price = price
        cone.data = data



#bowls
class Bowls (db.Model):
    id = Column('bowl_id', String(50), primary_key=True)
    name = Column(String(50))
    has_flavors = Column(String(10))
    price = Column(String(50))
    data = Column(LargeBinary, nullable=False) #Actual data, needed for Download
    

# initialize db
    def __init__(bowl, id, has_flavors, name, price, data):
        bowl.id = id
        bowl.name = name
        bowl.has_flavors = has_flavors
        bowl.price = price
        bowl.data = data


#milkshakes
class Milkshakes (db.Model):
    id = Column('milkshake_id', String(50), primary_key=True)
    name = Column(String(50))
    description = Column(String(10))
    price = Column(String(50))
    data = Column(LargeBinary, nullable=False) #Actual data, needed for Download
  
    # initialize db
    def __init__(milkshake, id, name, description, price, data):
        milkshake.id = id
        milkshake.name = name
        milkshake.description = description
        milkshake.price = price
        milkshake.data = data


#smoothies table
class Smoothies (db.Model):
    id = Column('smoothie_id', String(50), primary_key=True)
    name = Column(String(50))
    price = Column(String(50))
    data = Column(LargeBinary, nullable=False) #Actual data, needed for Download
   
    
    # initialize db
    def __init__(smoothie, id, name, price, data):
        smoothie.id = id
        smoothie.name = name
        smoothie.price = price
        smoothie.data = data
  

#frappe table
class Frappes (db.Model):
    id = Column('frappe_id', String(50), primary_key=True)
    name = Column(String(50))
    price = Column(String(50))
    data = Column(LargeBinary, nullable=False) #Actual data, needed for Download
 
  
# initialize db
    def __init__(frappe, id, name, price, data):
        frappe.id = id
        frappe.name = name
        frappe.price = price
        frappe.data = data


#snowcone
class Snowcones (db.Model):
    id = Column('snowcone_id', String(50), primary_key=True)
    name = Column(String(50))
    price = Column(String(50))
    description = Column(String(50))
    data = Column(LargeBinary, nullable=False) #Actual data, needed for Download

    # initialize db
    def __init__(snowcone, id, name, price, description, data):
        snowcone.id = id
        snowcone.name = name
        snowcone.price = price
        snowcone.description = description
        snowcone.data = data 


#snowcone
class Flavors (db.Model):
    id = Column('flavors_id', String(50), primary_key=True)
    name = Column(String(50))
    data = Column(LargeBinary, nullable=False) #Actual data, needed for Download
   
  
# initialize db
    def __init__(flavor, id, name, data):
   #display you can only use 3 flavors
        flavor.id = id
        flavor.name = name
        flavor.data = data

class Orders(db.Model):
    id = mapped_column(Integer, primary_key=True)
    items = relationship("Items", back_populates="order")
    email = Column(String(50))
    total = Column(String(50))
   
    # initialize db
    def __init__(cart, total, email):
        cart.email = email
        cart.total = total
 
class Items(db.Model):
    id = mapped_column(Integer, primary_key=True)
    order_id = mapped_column(Integer, ForeignKey("orders.id"))
    order = relationship("Orders", back_populates="items")
    pname = Column(String(50))
    price = Column(String(50))
    flavors = Column(String(50))
 

    def __init__(item, order_id, pname, price, flavors):
        item.order_id = order_id
        item.pname = pname
        item.price = price
        item.flavors = flavors


      






@app.route('/api/test')
def test_api():
    return jsonify({'test':'success',
                    'anothertest': 'anothersuccess'})

# #API to get items sold and their prices
#receives cart array
# @app.route('/api/get_items_sold')
# def get_items_sold_api():
#     items_sold = []
#     for item in items_list:
#         items_sold.append({
#             "id": item.id, 
#             "name": item.name, 
#             "price": item.price 
#         })
#     return jsonify({'id': item.id, 'name': item.name, 'price':item.price})


@app.route('/api/check_out_confirmation', methods = ['POST'])
def send_email_api():
    request_data = request.get_json()
    user_email = request_data['userEmail']
    total = request_data['total']
    cart = request_data['cart']

    order = Orders(total, user_email)
    db.session.add(order)
    db.session.commit()
    
    for i in cart:
        item = Items(order.id, i["pname"], i["price"], i["flavors"])
        db.session.add(item)
        db.session.commit()



    #get recipient info
    msg = Message('Thank you for your order! ', sender =   'rollingstoneicecreamenmu@gmail.com', recipients=[user_email])
    msg.subject =  "Here are your order details:"
    msg.body = ""
    
    for i in cart: 
        msg.body += i["pname"] + ", " + i["price"] + ", " + i["flavors"] + "\n"
    msg.body += "Total: " + total

    mail.send(msg)
    return "Success"

# @app.route('/api/shopping')
# def checkout():
#     return render_template('/Checkout.html')

@app.route('/api/getSnowcones')
def get_snowcones_api():
    results = Snowcones.query.all()
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
    results = Cones.query.all()
    result_list = []
    for item in results:
        result_list.append({
            "id": item.id,            
            "name": item.name,
            "hasFlavors": item.has_flavors,
            'price': item.price,
            'imgSrc': item.data.decode('utf-8')
        })
    return json.dumps({'data':result_list})

@app.route('/api/getSundaes')
def get_sundaes_api():
    results = Sundaes.query.all()
    result_list = []
    for item in results:
        result_list.append({
            "id": item.id,
            "hasFlavors": item.has_flavors,
            "name": item.name,
            "description": item.description,
            'price': item.price,
            'imgSrc': item.data.decode('utf-8')
        })
    return json.dumps({'data':result_list})

@app.route('/api/getWaffleBowls')
def get_waffles_api():
    results = Bowls.query.all()
    result_list = []
    for item in results:
        result_list.append({
            "id": item.id,
            "hasFlavors": item.has_flavors,
            "name": item.name,
            'price': item.price,
            'imgSrc': item.data.decode('utf-8')
        })
    return json.dumps({'data':result_list})

@app.route('/api/getSmoothies')
def get_smoothies_api():
    results = Smoothies.query.all()
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
    results = Milkshakes.query.all()
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

@app.route('/api/getFrappes')
def get_frappes_api():
    results = Frappes.query.all()
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
    results = Flavors.query.all()
    result_list = []
    for item in results:
        result_list.append({
            "id": item.id,
            "name": item.name,
            'imgSrc': item.data.decode('utf-8')
        })
    return json.dumps({'data':result_list})

@app.route('/api/getOrders')
def get_orders_api():
    results = Orders.query.all()
    result_list = []
    for item in results:
        item_list = []
        for i in item.items:
            item_list.append({
                'id': i.id,
                'pname': i.pname,
                'flavors': i.flavors,
                'price': i.price
            })
        result_list.append({
            "id": item.id,
            "email": item.email,
            'total': item.total,
            'items': item_list
        })
    return json.dumps({'data':result_list})

@app.route('/api/test/resetDbData')
def reset_db_data_api():
    f = open(json_url)
    data = json.load(f)
    for i in data['stores']:
        if i['name'] == 'snowConeType':
            db.session.query(Snowcones).delete()
            db.session.commit()
            for item in i['data']:
                snowcone = Snowcones(item['id'], item['name'], item['price'], item['description'], item['imgSrc'].encode('utf-8'))
                db.session.add(snowcone)
                db.session.commit()
        if i['name'] == 'sundaeType':
            db.session.query(Sundaes).delete()
            db.session.commit()
            for item in i['data']:
                sundae = Sundaes(item['id'], item['hasFlavors'], item['name'], item['description'], item['price'], item['imgSrc'].encode('utf-8'))
                db.session.add(sundae)
                db.session.commit()
        if i['name'] == 'coneType':
            db.session.query(Cones).delete()
            db.session.commit()
            for item in i['data']:
                cone = Cones(item['id'], item['name'], item['hasFlavors'], item['price'], item['imgSrc'].encode('utf-8'))
                db.session.add(cone)
                db.session.commit()
        if i['name'] == 'bowlType':
            db.session.query(Bowls).delete()
            db.session.commit()
            for item in i['data']:
                bowl = Bowls(item['id'], item['hasFlavors'], item['name'], item['price'], item['imgSrc'].encode('utf-8'))
                db.session.add(bowl)
                db.session.commit()
        if i['name'] == 'milkShakeType':
            db.session.query(Milkshakes).delete()
            db.session.commit()
            for item in i['data']:
                milkshake = Milkshakes(item['id'],item['name'], item['description'], item['price'],  item['imgSrc'].encode('utf-8'))
                db.session.add(milkshake)
                db.session.commit()
        if i['name'] == 'smoothieType':
            db.session.query(Smoothies).delete()
            db.session.commit()
            for item in i['data']:
                smoothie = Smoothies(item['id'], item['name'], item['price'], item['imgSrc'].encode('utf-8'))
                db.session.add(smoothie)
                db.session.commit()
        if i['name'] == 'frappeType':
            db.session.query(Frappes).delete()
            db.session.commit()
            for item in i['data']:
                frap = Frappes(item['id'], item['name'], item['price'], item['imgSrc'].encode('utf-8'))
                db.session.add(frap)
                db.session.commit()
        if i['name'] == 'flavors':
            db.session.query(Flavors).delete()
            db.session.commit()
            for item in i['data']:
                flavor = Flavors(item['id'], item['name'], item['imgSrc'].encode('utf-8'))
                db.session.add(flavor)
                db.session.commit()
    return jsonify({'dbreset':'success'})

    

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
   
