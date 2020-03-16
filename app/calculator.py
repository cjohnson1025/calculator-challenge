from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/")
def test():
	# return "Hello"
	return render_template("calculator_page.html")

