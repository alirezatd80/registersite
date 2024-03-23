from flask import Flask,render_template,redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy

#setting
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admins.db'
db = SQLAlchemy(app)

#models
class Admins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return f"{self.username}:{self.password}"

#create database file
with app.app_context():
      
       db.create_all()

#database functions 
def AddAdmin(name , passsword):
    admin = Admins(username = name , password=passsword)
    db.session.add(admin)
    db.session.commit()

def getall():
   allAdmins = Admins.query.all()
   return str(allAdmins)

def findByUsername(name):
    user = Admins.query.filter_by(username = name).all()
    return user 

# routes
@app.route("/<username>")
def main(username):
     return "hi"      

@app.route("/log")
def login():
    return render_template('login.html')

@app.route("/adminpage")
def adminpage():
    return render_template('adminpage.html')



#run app
if __name__ == "__main__":
    app.run(debug=True)
    
