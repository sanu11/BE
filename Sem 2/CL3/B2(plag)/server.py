from flask import Flask , request, render_template

app = Flask(__name__)

@app.route('/')
def fun():
    return render_template('index.html',msg="")
    
@app.route('/check/',methods=['POST','GET'])
def check():
    a = checker(request.form['string'])
    return render_template('index.html',msg=a)

def checker(str1):
    file_data=""
    with open('data.txt','rt') as f:
        for line in f:
            file_data = file_data + line
            
    a = file_data.split('.')
    print a
    b = str1.split('.')
    print b
    count = 0
    for i in a:
        for j in b:
            if i==j:
                count=count+1
                
    print "count = ",count
    percentage = str(float(count)/len(b)*100.0) + "%"                
    return percentage

if __name__=="__main__":
    app.run()
