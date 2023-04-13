from flask import Flask, request,render_template
import numpy as np
import pandas as pd
import joblib
import pickle
model1 =pickle.load(open('flighdel.pkl',"rb")) 
ct=joblib.load("flighdel.pkl") 



# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("iindex.html")
@app.route('/ass')
def assesment():
    return render_template("iindex2.html")

@app.route('/prediction',methods=['POST'])
def predict():
 if request.method == 'POST':
    name=request.form['name']
    month=request.form['month']
    dayofmonth=request.form['dayofmonth']
    dayofweek=request.form['dayofweek']
    origin=request.form['origin']
    if(origin=='msp'):
        origin1,origin2,origin3,origin4,origin5=0,0,0,0,1
    if(origin == 'dtw'):
         origin1,origin2,origin3,origin4,origin5=1,0,0,0,0
    if(origin == 'jfk'):
         origin1,origin2,origin3,origin4,origin5=0,0,1,0,0
    if(origin == 'sea'):
         origin1,origin2,origin3,origin4,origin5=0,1,0,0,0
    if(origin == 'alt'):
         origin1,origin2,origin3,origin4,origin5=0,0,0,1,0
    destination=request.form["destination"]
    if(destination=="msp"):
        destination1,destination2,destination3,destination4,destination5=0,0,0,0,1
    if(destination=="dtw"):
         destination1,destination2,destination3,destination4,destination5= 1,0,0,0,0
    if(destination=="jfk"):
        destination1,destination2,destination3,destination4,destination5=0,0,1,0,0
    if(destination=="sea"):
         destination1,destination2,destination3,destination4,destination5= 0,1,0,0,0
    if(destination=="alt"):
        destination1,destination2,destination3,destination4,destination5=0,0,0,1,0
    dept=request.form['dept']  #dept ime 
    arrtime=request.form['arrtime']   
     #crs dept time
    actdept=request.form['actdept']  #dept time #crs dept
    dept15=int(dept)-int(actdept)
    total=[(name,month,dayofmonth,dayofweek,origin1,origin2,origin3,origin4,origin5, destination1,destination2,destination3,destination4,destination5,arrtime,dept15)]

    y_pred=model1.predict(total)
    print(y_pred)
    if(y_pred==[0.]):
           ans="The flight will be on time"
    else:
        ans="The flight will be delayed"
    return render_template("index3.html",showcase=ans)
 return render_template("iindex.html")



# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
