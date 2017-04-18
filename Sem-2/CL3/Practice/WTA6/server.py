
from flask import render_template
from flask import Flask,redirect,request
from bson.objectid import ObjectId

from pymongo import *

client=MongoClient('localhost',27017)
db=client.assignment_db
'''
app_info = db['app_info']
app_info.insert_one(tokeninfo)


userinfo=user_info.find_one({"SignUpUid":email})


collections
1)users

'''
app = Flask(__name__)


@app.route('/login',methods=['POST','GET'])
def login_post():
    print request.form
    user = db['users']
    user.insert_one({"Name":request.form['name'],"Password":request.form['password'],"Role":request.form['role'],"AdharNumber":request.form['number']})
    return render_template('login.html',name=request.form['name'],password=request.form['password'],msg="")
    
    
    
@app.route('/')
def login():
    return render_template('login.html',name="",password="",msg="")
    
    
    
@app.route('/signup',methods=['POST','GET'])
def signup():
    return render_template('signup.html')
    
                
                
@app.route('/verify',methods=['POST', 'GET'])
def verify():
    user = db['users']
    a = user.find_one({"Name":request.form['username'],"Password":request.form['password']})
    if a==None:
        print "invalid user/password"
        return render_template('login.html',name="",password="",msg="Invalid username/password")
    my_url = '/'+a['Role']+'/'+a['Name']
    print my_url
    return redirect(my_url)
    
    
    
@app.route('/doctor/')
@app.route('/doctor/<name>',methods=['POST','GET'])
def doctor(name=None):
    if request.method=='POST' or request.method=='GET':
        print "request accepted"
        appo = db['appointments']
        print "keys:",request.form.keys()
        if len(request.form.keys())!=0: 
            appo.update({"_id":ObjectId(str(request.form.keys()[0]))},{"$set":{"Result":request.form[request.form.keys()[0]]}})
        
    appo = db['appointments']    
    appo_list = appo.find({"Doctor":name})
    return render_template('doctor.html', name=name,appointments=appo_list)
    
    

@app.route('/patient/')
@app.route('/patient/<name>',methods=['POST','GET'])
def patient(name=None):
    if request.method=='POST' or request.method=='GET':
        print request.form
        if len(request.form)!=0:
            appo = db['appointments']
            appo.insert_one({"Name":name,"PatientsName":request.form['pname'],"PatientsAge":request.form['page'],"Doctor":request.form['doctor'],"Result":"Pending","Time":request.form['ptime']})
    
    user = db['users']
    doc_list = user.find({"Role":"doctor"})
    print doc_list.count()
    print doc_list[0]
    if doc_list==None:
        doc_list=[]
    appo = db['appointments']    
    appo_list = appo.find({"Name":name})

    return render_template('patient.html', name=name,doctors=doc_list,appointments=appo_list)
    
if __name__ == '__main__':
    app.run()
