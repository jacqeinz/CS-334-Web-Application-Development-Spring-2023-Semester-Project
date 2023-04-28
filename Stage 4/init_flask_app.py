# config.py #app.py #


from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# # tells flask where to put static files
# COLLECT_STATIC_ROOT = os.path.dirname(__file__) + '/static'
# COLLECT_STORAGE = 'flask_collect.storage.file'
# # create the app
app = Flask(__name__)
# # configure the SQLite database, relative to the app instance folder
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///defaultData.db'
# app.config['SECRET_KEY'] = "random string"
# # initialize the app with the extension
# db = SQLAlchemy(app)
# app.app_context().push()

# # tables

# #sundaes 
# class sundae (db.Model):
#     id = db.Column('sundae_id', db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     hasFlavors = db.Column(db.String(10))
#     description = db.Column(db.String(50))
#     Price = db.Column(db.String(50))
#     #img?
# # initialize db
#     def __init__(sundae, name, hasFlavors, description, Price ):
#         sundae.name = name
#         sundae.hasFlavors = hasFlavors
#         sundae.description = description
#         sundae.Price = Price
#         #img?

# #cones
# class cone (db.Model):
#     id = db.Column('cone_id', db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     hasFlavors = db.Column(db.String(10))
#     Price = db.Column(db.String(50))
#     #img?
# # initialize db

#     def __init__(cone, name, hasFlavors, Price ):
#         cone.name = name
#         cone.hasFlavors = hasFlavors
#         cone.Price = Price
#         #img?


# #bowls
# class bowl (db.Model):
#     id = db.Column('bowl_id', db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     hasFlavors = db.Column(db.String(10))
#     Price = db.Column(db.String(50))
#     #img?
# # initialize db
#     def __init__(bowl, name, hasFlavors, Price ):
#         bowl.name = name
#         bowl.hasFlavors = hasFlavors
#         bowl.Price = Price
#         #img?

# #milkshakes
# class milkshake (db.Model):
#     id = db.Column('milkshake_id', db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     hasFlavors = db.Column(db.String(10))
#     Price = db.Column(db.String(50))
#     #img?
# # initialize db
# def __init__(milkshake, name, hasFlavors, Price ):
#    milkshake.name = name
#    milkshake.hasFlavors = hasFlavors
#    milkshake.Price = Price
#    #img?

# #smoothies table
# class smoothie (db.Model):
#     id = db.Column('smoothie_id', db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     hasFlavors = db.Column(db.String(10))
#     Price = db.Column(db.String(50))
#     #img?
# # initialize db
# def __init__(smoothie, name, hasFlavors, Price ):
#    smoothie.name = name
#    smoothie.hasFlavors = hasFlavors
#    smoothie.Price = Price
#    #img?

# #frappe table
# class frappe (db.Model):
#     id = db.Column('frappe_id', db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     hasFlavors = db.Column(db.String(10))
#     Price = db.Column(db.String(50))
#     #img?
# # initialize db
# def __init__(frappe, name, hasFlavors, Price ):
#    frappe.name = name
#    frappe.hasFlavors = hasFlavors
#    frappe.Price = Price
#    #img?

# #snowcone
# class snowcone (db.Model):
#     id = db.Column('snowcone_id', db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     hasFlavors = db.Column(db.String(10))
#     Price = db.Column(db.String(50))
#     description = db.Column(db.String(50))
#     #img?
# # initialize db
# def __init__(snowcone, name, hasFlavors, Price, description ):
#    snowcone.name = name
#    snowcone.hasFlavors = hasFlavors
#    snowcone.Price = Price
#    snowcone.description = description
#    #img?


# #snowcone
# class flavors (db.Model):
#     id = db.Column('flavors_id', db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
  
#     #img?
# # initialize db
# def __init__(flavors, name ):
#    flavors.name = name
#    #img?



@app.route('/')
def index():
    return render_template('index.html')



if __name__ == "__main__":
    #init_db.run()
    # db.create_all()
    #create_app.run()
    app.run(debug = True)
   
