from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html',msg="",data="")

@app.route("/check/",methods=['POST','GET'])
def check():
	data = request.form['data']
	res = checker(data)
	res = str(res) + "%"
	print res
	return render_template('index.html',msg=res,data=data)

def checker(data):
	f = open('data.txt','r')
	file_data=""
	for line in f:
		file_data = file_data + line

	a = file_data.split('.')

	b = data.split('.')

	count =0
	print "Data in file :\n", a
	print "Data to be checked :\n" ,b
	for i in a:
		for j in b:
			if i.strip()==j.strip():
				count+=1
	print "Copied lines : ", count
	print "Total lines : " , len(b)
	percent= float(count)/float(len(b))*100

	print "Percentage of plagiarism : " , percent
	return percent 

if __name__ == "__main__":
    app.run()