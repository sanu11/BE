from flask import Flask, render_template,request
from ubidots import ApiClient
from datetime import datetime
app = Flask(__name__)
app.config['DEBUG'] = True

api = ApiClient(token='WIPAcLJ460JE0X0tILNL6Cnv82mCrL')
@app.route('/')
def MainPage():
	return render_template('index.html')

@app.route('/create/',methods=['POST'])
def create():
	print "hi"
	name = request.form["name"]
	tag1 = request.form["tag1"]
	tag2 = request.form["tag2"]
	des = request.form["des"]
	tags=[tag1,tag2]
	print tags
	ds= api.get_datasources()
	present=0
	for i in ds:
		if str(i)==name:
			present=1
	if not present:
		new_datasource= api.create_datasource({"name":name,"tags":tags,"des":des})
		print "datasource created"
	print ds
	return render_template("datasource.html",name=name,tags=tags,des=des)

@app.route("/insert",methods=['POST'])
def insert():
	ds = api.get_datasources()[0]
	name= request.form["name"]
	unit = request.form["unit"]
	value1 =request.form["value1"]
	value2 =request.form["value2"]
	value3 =request.form["value3"]
	values = [value1,value2,value3]
	values = map(int,values)
	variable = ds.create_variable({"name":name , "unit":unit})
	variable.save_values([
    {'timestamp': 1380558972614, 'value': values[0]},
    {'timestamp': 1380558972915, 'value': values[1]},
    {'timestamp': 1380558973516, 'value': values[2]},])
	
	return render_template("variable.html",name=name,values=values)

@app.route("/display",methods=['GET','POST'])
def display():
	print "hi"
	datasource = api.get_datasources()
	variables= datasource[0].get_variables()
	x=[]
	length=[]
	count=0
	print variables
	for i in variables:
		c= i.get_values()
		l=[]
		length.append(count)
		count+=1
		print c
		for k in range(3):
			l.append(c[k]['value'])
		x.append(l)
	print x
	return render_template("values.html",values=x,variables=variables,name=datasource[0],length=length)


app.run(port =5003)
