from flask import request, render_template,make_response,abort,redirect,flash,session,url_for
from flask import flash

from p_package import mail, Message,csrf

from werkzeug.security import  generate_password_hash,check_password_hash 
from flask import send_from_directory
from p_package.myforms import ContactForm,LoginForm,SignUp,Usersignup,Register,Payment
from p_package import app, db
from p_package.models import User,Profile,Skills,member_skills,Items
from sqlalchemy import or_,desc
from flask import jsonify
from money import Money
import random
import os
import json



from werkzeug.datastructures import CombinedMultiDict
from werkzeug import secure_filename

from PIL import Image



    

@app.route('/tran/',methods=['GET','POST'])
def tran():
    if request.method == 'GET':
        form=Payment()
        items= db.session.query(Items).all()
        return render_template('pay.html',items=items,form=form)
    else:
        customer=request.form['custname']
        email= request.form['email']
        phone = request.form['phone']
        prodid= request.form['product']
        deets = db.session.query(Items).get(prodid)
        amt=deets.item_amt
        trans_ref=random.random()
        trans_obj=Transaction(trans_status=0,trans_amt=amt,trans_phone=phone,trans_email=email)
        db.session.add(trans_obj)
        db.session.commit()
        session['trans_id']=trans_obj.trans_id
        return redirect('/makepay')


@app.route('/makepay/',methods=['GET',''])
def makepay():
    transid=session['trans_id']
    transaction_details=db.session.query(Transaction).get(transid)
    productid=transaction_details.trans_productid
    productname=db.session.query(Items).get(productid)
    return render_template('pay.html',deets=transaction_details,productname=productname)


def generate_rand():
    drand = ""
    for i in range(10):
        drand = drand + str(random.randrange(0,9))
    return drand



@csrf.exempt
@app.route('/loadamt', methods=['POST'])
def load():
    id=request.form['itemid']
    amt=db.session.query(Items).get(id)
    if amt != None:
        formatted=Money(amount=amt.item_amt,currency="NGN")
        return str(formatted)
    else:
        return "YOU need to make a choice"


@app.route('/paystack/')
def paystack():
    return render_template('paystack,html')

# @app.route('/pay/')
# def pay():
#     re

# @app.route('/register/')
# def register():
#     form=SignUp()
#     return render_template('register.html',form=form)






# @app.route('/signup/')
# def signup():
#     formdata=SignUp()
#     return render_template('signup.html', myform=formdata)












# @app.route('/pro/')
# def pro():
#     return render_template('/pro.html')





@app.route('/contacus/')
def contacus():

    return render_template('contacus.html')


@csrf.exempt
@app.route('/submitcon/',methods=['GET','POST'])
def submitcon():
    data= f"<select><option>Lagos</option></select>"
    return "I got her"



@csrf.exempt
@app.route('/jsonsub/',methods=['GET','POST'])
def jsonsub():

    j=db.session.query(Profile.firstname,Profile.lastname).all()
    return jsonify(j)
    
    




@app.route('/search/')
def search():
    return render_template('search.html')

@app.route('/example/')
def example():
    deal= '{"no":1,"description":"50% discount on tubers of yam"}'
    deal_dict = json.loads(deal)
    python_tup=('a','b','c')
    json_equiv=json.dumps(python_tup)
    return render_template ('json.html',deal_dict=deal_dict,json_equiv=json_equiv)






@app.route('/signup/')
def signup():
    userobj= User(username='messi@yahoo.com',pwd='ola')
    db.session.add(userobj)
    db.session.commit()
    return "added"

# @app.route('/homee/')
# def home():
#     mylist=['tola','bola']
#     title='welcome'
#     name='tommy'
#     age=[4,5,6]
#     data={'title':'welcome', 'age':'[2,3]'}
#     return render_template('index.html',myage=age,data=data,myname=name,title=title,mylist=mylist)

# @app.errorhandler(404) 
def error404(error):
    return render_template('404.html',error=error),404




@app.errorhandler(500)
def error500(error):
    return render_template('500.html',error=error),500




@app.route('/test')
def test():
    obj = make_response('this a mimic not found',404)
    obj.headers['content-encoding'] = 'text/plain.html'
    return obj


@app.route('/tes/<username>')
def tes(username):
    if username =='ola':
        obj = make_response(' not found',404)
        obj.headers['content-encoding'] = 'text/plain.html'
        return obj
    else:
        abort(403)

@app.route('/contactus/')
def contactus():
    formdata=ContactForm()
    return render_template('contactus.html',formi=formdata)


@app.route('/formsubmit/',methods=['POST'])
def formsubmit():
    form = ContactForm()
    if form.validate_on_submit():
        return  'thank you for filling'
    else:
        return render_template('contactus.html',formi=form)
        # return 'you will be redirected'
    

# # #@app.route('/home/',methods=['POST','GET'])
# # #def hom():
# #     if request.method =='GET':
# #         return 'login form here'
# #     else:
# #         return 'submit your form'
# #     return 'hello world'
# # #app.add_url_rule('/home/','home', hello)

# @app.route('/product/')
# @app.route('/product/<productname>')
# def mypage(productname=None):
#     if productname==None:
#         return "show all product"
#     if productname == 'rice':
#         return "All about rice"
#     elif productname == 'beans':
#         return "All about Beans"
#     else:
#         return f"we do not {productname}"

# @app.route('/aboutus/')
# def about():

#     return render_template('about.html')


@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template ('login.html')
    else:
        username=request.form['username']
        password = request.form['pwd']
        if username == 'tom' and password =='123':
            session['username']= username
            return redirect("/home")
            
        else:
            flash("invalid login")
            return  redirect ("/login")



# @app.route('/getse/')
# def getses():
#      if 'username' in session:
#          return session ['username']
#      return 'not logged in'

# @app.route('/logout/')
# def logout():
#     session.pop('username', None)
#     return redirect('/login')
 
# @app.route('/sett/')
# def setcookie():
#     resp=make_response('setting cookies')
#     resp.set_cookie('frame','flask')
#     return 
    
# @app.route('/prac/')
# def ses():
#     session['user']='oladimeji'
#     return render_template('prac.html')
    
# @app.route('/getse/')
# def getses():
#     if 'user' in session:
#         return session ['user']
#     return 'not logged in'



@app.route('/prac/')
def prac():
    return render_template('prac.html')
    

# @app.route('/profile/')
# def profile():
#     return render_template('profile.html')

# @app.route('/ourproduct/')
# def products():
#     return render_template('products.html')

# @app.route('/ourstore/<int:storeid>')
# def store(storeid):
#     return render_template('store.html')

@app.route('/home/')
def home():
    form=Usersignup
    return render_template('bootstrap.html',form=form)


@app.route('/profiler/',methods=['GET','POST'])
def profiler():
    form=Usersignup()
    allskills=db.session.query(Skills).all()
    if request.method =='GET':
        return render_template('profiler.html',form=form,allskills=allskills)
    else:
        #retrieve form date
        if form.validate_on_submit():
            ppt = request.files['passport']
            name, ext = os.path.splitext(ppt.filename)
            newname=secure_filename(name) + str(random.random()) + ext
            ppt.save(app.config['UPLOAD_FOLDER'] + newname)


            # image=Image.open(app.config['UPLOAD_FOLDER'])
            # image.thumbnail((400,400))
            # image.save(app.config['UPLOAD_FOLDER'] + 'thumb.jpg')

            #os.remove(app.config['UPLOAD_FOLDER'] + newname)

            skills=request.form.getlist('skills')
            mydata = Profile(firstname=request.form['firstname'],lastname=request.form['lastname'],email=request.form['email'],password=request.form['password'],profile_pix = newname)
            db.session.add(mydata)
            db.session.commit()
            membid = mydata.profile_id
        #how to insert into association table
            if skills:
                for s in skills:
                    statement = member_skills.insert().values(memberid=membid,skillid=s)
                    db.session.execute(statement)
                    db.session.commit()
            return render_template('profiler.html',form=form,allskills=allskills)
        else:
            return render_template('profiler.html',form=form,allskills=allskills)

 

@app.route('/viewimage/<path:filename>')
def download_file(filename):
    return send_from_directory('../' + app.config['UPLOAD_FOLDER'],filename,as_attachment=True)
 #querying database
@app.route('/allmembers/')
def allmembers():
    #members=db.session.query(Profile).order_by(desc(Profile.lastname))
    members = Profile.query.filter(Profile.lastname=='coder').all()
    return render_template('report.html', members=members)
      #db.session.query(Profile)
    # return render_template('report.html', members=members)
    

#JOINING TABLE
@app.route('/userdetails/<userid>')
def userdetails(userid):
    memskills=db.session.query(skills_name,member_skills).joinall()
    return render_template('userdetails.html',memskills=memskills)

    # SELECT * FROM `member_skills` JOIN skills WHERE memberid = 5


@app.route('/skills/')
def skill():
    m=db.session.query(Skills)
    return render_template('skills.html',m=m)

@app.route('/register/',methods=['GET','POST'])
def register():
    myform=Register()
    if request.method=='GET':
        return render_template('register.html',myform=myform)
    else:
        if myform.validate_on_submit():
            x=request.form['username']
            y=request.form['password']
            userobj=User(username=x,pwd=y)
            db.session.add(userobj)
            db.session.commit()
            session['username']= userobj.userid
            session['username']= userobj.username
            return render_template('tem.html')
        else:
            return render_template('register.html',myform=myform)

@app.route('/tem/')
def tem():
    return render_template('tem.html')




   



@app.route('/loginn/',methods=['GET','POST'])
def loginn():
    form=LoginForm()
    if request.method=='GET':
        return render_template('loginn.html',form=form)
    else:
        if form.validate_on_submit():
            # username = request.form['username']
            # password = request.form['password']
            data=db.session.query(User).filter(User.username==request.form['username'],User.pwd==request.form['password']).first()
            if data != None:
                # session['username'] = request.form['username']
                # session['user']=data.userid
                return redirect('/mypro/')

            # if data.count() > 0:
            #     
            #     return redirect('/mypro')
            else:
                flash('invalid password')
                return render_template('loginn.html',form=form)
        else:
            return render_template('loginn.html',form=form)
   
@app.route('/mypro/')
def mypro():
    id=session['user']
    t = db.session.query(User).filter(User.userid==id).first()
    return render_template('mypro.html',id=id,t=t)
    # if session.get('username'):
    #     return render_template('mypro.html')
    # else:
    #     return redirect('/loginn.html')

@app.route('/update/',methods=['POST'])
def update():
    form=LoginForm()
    id=session['user']
    user=db.session.query(User).get(id)
    user.pwd=request.form['password']
    db.session.commit()
    return render_template('update.html', form=form)


@app.route('/editprofile/<int:profileid>')
def editprofile(profileid):
    form=LoginForm()
    id=session['user']
    if session.get('user'):
        det=db.session.query(User).get_or_404(profileid)
        return render_template('edit.html',det=det,form=form)
    else:
        return redirect('/loginn')

@app.route('/loginn/')
def delete():
    form=LoginForm()
    id=session['user']
    user=db.session.query(User).get(id)
    db.session.delete(user)
    db.session.commit()
    return render_template('loginn.html',form=form)


@app.route('/logout/')    
def logout():
     if session.get('username'):
         session.pop('username')
     return redirect('/loginn')




# @app.route('/mail/')
# def mymail():
#     msg= Message(subject='Hello',sender='tommyslipz@gmail.com',recipients=['oladimejicoder@gmail.com','kaysho109@gmail.com'])
#     msg.body="oladimeji"
#     msg.html = "<b>testing<b>"
#     mail.send(msg)        
