

from flask import Flask, redirect, render_template,request
from database1 import adddata
app=Flask(__name__)  # create object of flask class
@app.route("/")
def home():
    return render_template("home1.html")
@app.route("/reglink")
def regfun():
    return render_template("register.html")
@app.route('/savelink' ,methods=["POST"])
def save():
   name=request.form["name"]  
   adhar_no=request.form["adhar_no"] 
   phone=request.form["phone"] 
   city=request.form["city"]
   vaccine=request.form["vaccine"]
   center=request.form["center"]
   t=(name,adhar_no,phone,city,vaccine,center)
   adddata(t)
   return redirect("reglink")
  
  
    
    
if __name__=="__main__" :
    app.run(debug=True)   
