from flask import Flask, request, render_template
from booths import *
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html',num1=None,num2=None,product=None)

@app.route("/multiply/",methods = ['POST','GET'])
def eval():
	print "hi"
	num1 = int(request.form['num1'])
	num2 = int(request.form['num2'])
	print num1,num2
	res = str(multiply(num1,num2))
	print res
	return render_template('index.html',product = res ,num1=num1,num2=num2)


if __name__ == "__main__":
    app.run()