from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def initial_page():
	return render_template("calculator_page.html")

@app.route("/", methods=['POST'])
def calculation():
	eq = request.form['equation']
	if eq:
		return json.dumps({'html':'<span>It worked</span>'})
	return render_template("calculator_page.html")

