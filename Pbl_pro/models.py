from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class login_model(db.Model):
#     # __tablename__ = "table"
#     __tablename__="login_signup"
#     id = db.Column(db.Integer, primary_key=True)
#     email= db.Column(db.String())
#     pswd = db.Column(db.Integer(),unique = True)
#     def __init__(self,email,pswd):
#         self.email =email
#         self.pswd = pswd
#     def __repr__(self):
#         return f"{self.email}:{self.pswd}"
class sg(db.Model):

    __tablename__="signin"
    id1= db.Column(db.Integer, primary_key=True)
    txt=db.Column(db.String())
    e= db.Column(db.String())
    p= db.Column(db.Integer(),unique=True)

    # name = db.Column(db.String())

    # id = db.Column(db.Integer, primary_key=True)
    # employee_id = db.Column(db.Integer(),unique = True)
    # name = db.Column(db.String())
    # age = db.Column(db.Integer())
    # position = db.Column(db.String(80))

   
    def __init__(self,txt,e,p):
        self.txt=txt
        self.e =e
        self.p = p
       

    
    def __repr__(self):
        return f"{self.txt}:{self.e}:{self.p}"
    
        
    