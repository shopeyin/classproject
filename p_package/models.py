from datetime import datetime
from p_package import db

class User(db.Model):
    userid=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(255),nullable=False)
    # email = db.Column(db.String(50),unique=True)
    pwd=db.Column(db.String(255),nullable=False)
    user_created_on=db.Column(db.DateTime(),default=datetime.utcnow)

    def __repr__(self):
        return "<{}:{}>".format(self.userid,self.username)



member_skills=db.Table('member_skills', 
db.Column('memberid',db.Integer,db.ForeignKey('userprofile.profile_id'),primary_key=True),
db.Column('skillid',db.Integer,db.ForeignKey('skills.id'),primary_key=True)
)#it is optionalto heve both field

class Profile(db.Model):
    __tablename__= 'userprofile'
    profile_id=db.Column(db.Integer(),primary_key=True)
    firstname=db.Column(db.String(255),nullable=False)
    lastname=db.Column(db.String(255),nullable=False)
    email=db.Column(db.String(255),nullable=False)
    surname=db.Column(db.String(255),nullable=False)
    password=db.Column(db.String(255),nullable=False)
    profile_pix =  db.Column(db.String(255),nullable=False)
    user_created_on=db.Column(db.DateTime(),default=datetime.utcnow)
    #define the relationship here
    skills = db.relationship("Skills",secondary="member_skills",backref=db.backref('members'))


class Skills(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    skills_name = db.Column(db.String(255),nullable=False)


class Deal(db.Model):
    deal_id=db.Column(db.Integer(),primary_key=True)
    deal_name=db.Column(db.String(255),nullable=False)
    deal_url=db.Column(db.String(255),nullable=False)
    user_created_on=db.Column(db.DateTime(),default=datetime.utcnow)





# MODELS

class Transaction(db.Model):
    trans_id = db.Column(db.Integer(), primary_key=True)
    trans_status = db.Column(db.Integer())
    trans_date = db.Column(db.DateTime(), default=datetime.utcnow)
    trans_phone = db.Column(db.String(255))
    trans_amt = db.Column(db.Integer()) 
    trans_customer = db.Column(db.String(255), nullable=False)
    trans_ref = db.Column(db.String(255))
    trans_paystackref = db.Column(db.String(255))
    trans_others = db.Column(db.Text())
    trans_email = db.Column(db.String(255), nullable=False)

    # create a Foreign Key Column
    trans_productid = db.Column(db.Integer(), db.ForeignKey('items.item_id'))


class Items(db.Model):
    item_id = db.Column(db.Integer(), primary_key=True)
    item_amt = db.Column(db.Integer())
    item_name = db.Column(db.String(255), nullable=False)
    # the relationship can be used to retrieve many instances of the child class
    transactions = db.relationship('Transaction', backref='item')

    

# class Memberskills():
#     memberid = db.Column(db.Integer(),db.ForeignKey('profile.profile_id',primary_key=True))
#     skills_id = db.Column(db.Integer(),db.ForeignKey,nullable=False)
    
