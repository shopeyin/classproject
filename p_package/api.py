from flask import request,jsonify,make_response

import random
import os,json 
from p_package import app,csrf,db
from p_package.models import Deal,User



from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()




@auth.get_password
def get_password(username):
    deets=db.session.query(User.pwd).filter(User.username==username).first()
    if deets:
        return deets.pwd
    else:
        return None


@auth.error_handler
def unauthorized():

    return make_response(jsonify({'error':'Unauthorized access'}),401)





@csrf.exempt
@app.route("/deal/api/v1.0/add/",methods=['POST'])

def add_deal():
    data=request.json
    if 'dealname' in data:

        dealname=data['dealname']
        dealurl=data['deal_url']


        #insert into Deal table
        dealobj= Deal(deal_name=dealname,deal_url=dealurl)
        db.session.add(dealobj)
        db.session.commit()
        #check if insertion was succesful
        dealid = dealobj.deal_id
        if dealid:
            rsp = {"status":"OK", "msg":"Deal Added"}
            return jsonify(rsp)
        else:
            rsp = {"status":"FAILED", "msg":"Database error"}
            return jsonify(rsp)
    else:
        rsp = {"status":"FAILED", "msg":"Wrong format"}



@app.route("/listdeal/api/v1.0/add/",methods=['GET'])
def listdeal():
    deal=db.session.query(Deal.deal_id,Deal.deal_name,Deal.deal_url).all()
    return jsonify(deal)


@csrf.exempt
@app.route("/editdeal/api/v1.0/edit/<int:id>" ,methods=['PUT'])
@auth.login_required
def edit_deal(id):
    # deal=db.session.query(Deal).get(id)
    # deal.deal_name="ola"
    # db.session.commit()
    # return "changed"

    deal=db.session.query(Deal).get(id)
    deal.deal_name=request.json['dealname']
    db.session.commit()
    return "changed"






