from create_db import db, init_db
class sundaes (db.Model): 
    id = db.Column(db.integer, primary_key=True)
    