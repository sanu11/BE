from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

URI = 'mongodb://username:password@127.0.0.1:27017/conferencedb'

client=MongoClient(URI)
db=client.conference
collection = db.details

money={'Gym':3500, 'WiFi':400, 'Spa':3000, 'Pool':500, 'Garden':1000}

app = Flask(__name__)

@app.route('/insert',methods=['POST'])
def insert():
	d={"Name":request.form['inputName'], "Email":request.form['inputEmail'], "Age":request.form['inputAge'], "Institute":request.form['inputInstitute'],"Country":request.form['inputCountry'], "Participant":request.form['participants'], "Currency":request.form['currency'], "Payment_type":request.form['payment_type'], "Hotel":request.form['Hotel'], "Gym":"0", "WiFi":"0", "Spa":"0", "Pool":"0", "Garden":"0", "total_expense":0}
	selected = request.form.getlist('check')
	any_selected = bool(selected)
	total = 0
	flag = 1
	all_docs = collection.find()
	for doc in all_docs:
		if d['Name'] == doc['Name'] and d['Email'] == doc['Email'] and d['Country'] == doc['Country']:
			flag = 0
			break
			
	if flag:
		if any_selected:
			for item in selected:
				d[item]='1'
				total += money[item]
		print "\n\ntotal", total
		
		if d['Currency'] == "Dollars":
			total /= 68
		elif d['Currency'] == "Euros":
			total /= 75
		elif d['Currency'] == "Pounds":
			total /= 94
		
		d['total_expense'] = total
		print "Extracted_Values:\n", d
		collection.insert(d)
		
	curren = d['Currency']
	return jsonify(result=total,currency=curren)

@app.route("/")
def main():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(host='127.0.0.1')
