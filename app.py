from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
  result = None
  if request.method == "POST":
    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    operation = request.form["operation"]
    
    if operation == "add":
      return num1 + num2
    elif operation == "subtract":
      return num1 - num2
    elif operation == "multiply":
      return num1 * num2
    elif operation == "division":
      return num1 / num2
  return render_template("index.html", result=result)

if__name__ = "__main__":
  app.run(debug=True)
  
    
    