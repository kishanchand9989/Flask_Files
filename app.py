from flask import Flask
from flask import request,redirect,url_for,render_template,jsonify
app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def UserPage():
    return render_template("Details.html")
  
if __name__=="__main__":
    app.run(host="0.0.0.0")
