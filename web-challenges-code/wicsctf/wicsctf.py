import sqlite3
from flask import Flask, render_template, request, g
app = Flask(__name__)

DATABASE = "chal3.db" # yeah it should be named chal2.db but I'm not perfect

@app.route("/")
def index():
	return render_template("index.html")

# Hidden HTML comment challenge
@app.route("/chal1/")
def chal1():
	return render_template("chal1/chal1.html")

# SQL Injection Challenge
@app.route("/chal2/", methods=['GET'])
def chal2():
	search_term = request.args.get('search_term')
	res = ""
	if search_term == None:
		return render_template("chal2/chal2.html")
	# Connect to DB
	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	query = "SELECT result FROM SEARCH WHERE search_term='" + search_term + "';"
	try:
		cur.execute(query)
	except sqlite3.Error as e:
		result = e
	res = cur.fetchall()
	if not res:
		res = "Hmm... There's no results for that search. Try searching for 'dog', 'cat', or 'book'."

	return render_template("chal2/chal2.html", result=res)

# Path Traversal Challenge
@app.route("/chal3/")
def chal3():
	return render_template("chal3/chal3.html")

@app.route("/vault/your_vault/")
def chal3_your_vault():
	return render_template("chal3/your_vault.html")

@app.route("/vault/")
def chal3_vault():
	return render_template("chal3/root.html")


# Unvalidated GET Request Challenge
@app.route("/chal4/", methods=['GET'])
def chal4():
	price = request.args.get('price')
	flag=""
	if price == None:
		flag = ""
	elif price == "10":	
		flag="You bought the duck for $10!"
	else:
		flag="You changed the price of the duck! Here is your flag flag{deducktion}"
	
	return render_template("chal4/chal4.html", flag=flag)

# Integer Overflow challenge
@app.route("/chal5/", methods=['GET'])
def chal5():
	flag = ""
	tax = 13
	int_max = 2147483647
	price = request.args.get('price')
	if price == None:
		flag = ""
		return render_template("chal5/chal5.html", flag=flag)

	price = int(price)

	if price == 1000000:
		flag="You bought the diamond for $1000013 (tax included)"
	
	elif price >= int_max:
		flag = "Price is out of range!"
	
	elif price+tax > int_max:
		cost = -1*int_max + price + tax
		flag = "You bought the diamond for $" + str(cost) + ". Here is your flag: flag{sh1n3_br1gh+}"
	
	else:
		flag="Invalid price"

	return render_template("chal5/chal5.html", flag=flag)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
