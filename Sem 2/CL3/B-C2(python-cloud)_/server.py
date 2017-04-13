
from flask import Flask,request,render_template
from ubidots import ApiClient

# SwWv78hxFMR42afpUyIKGKtwnNBtEV

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('ubi.html',product=None)

@app.route('/datasource',methods=['POST'])
def create_datasource():
    name=request.form['name']
    tags=[request.form['tag1'],request.form['tag2']]
    description=request.form['description']
    print name,str(tags),description

    already_present=''
    api = ApiClient(token='s4d6ZNJZ7snnwpQhm4EGlscRJwtPvG')
    all_datasources = api.get_datasources()
    print type(all_datasources)
    for i in all_datasources:
        if str(i) == name:
            print name+' is there'
            already_present='yes'
    if not already_present:
        new_datasource = api.create_datasource({"name": name, "tags": tags, "description": description}) 	#create new datasource
        print "datasource created\n"
    return render_template('datasource.html',name=name,tags=str(tags),description=description,already_present=already_present)

@app.route('/insert',methods=['POST'])
def insert_variable():
    vname=request.form['vname']
    unit=request.form['unit']
    v1=request.form['value1']
    v2=request.form['value2']
    v3=request.form['value3']
    values=[ v1,v2,v3 ]

    api = ApiClient(token='s4d6ZNJZ7snnwpQhm4EGlscRJwtPvG')
    all_datasources = api.get_datasources()
    print all_datasources 
    name=all_datasources[0]

    new_variable = all_datasources[0].create_variable({"name": vname, "unit": unit})					#create a new variable in the datasource
    print "variable0 created\n"

    new_variable.save_values([												#saving multiple values
    {'timestamp': 1380558972614, 'value': values[0]},
    {'timestamp': 1380558972915, 'value': values[1]},
    {'timestamp': 1380558973516, 'value': values[2]},])
    print "value saved to variable"

    return render_template('create_variable.html',name=name    ,variable=vname,unit=unit,values=values)

@app.route('/get_value',methods=['POST'])
def get_value_variable():
    api = ApiClient(token='s4d6ZNJZ7snnwpQhm4EGlscRJwtPvG')
    all_datasources = api.get_datasources()
    print all_datasources 
    name=all_datasources[0]
    variables=all_datasources[0].get_variables()	#all values
    print variables
    values_all=[]
    length=[]
    count=0
    for i in variables:
        values=[]
    	c=i.get_values()
        for k in range(3):
            values.append(c[k]['value'])
        length.append(count)
        count+=1
        values_all.append(values)
    print values_all

    return render_template('get_variables.html',name=name,variables=variables,values=values_all,length=length)    
if __name__=="__main__":
    app.run(port=5003)
