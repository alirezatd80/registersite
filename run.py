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

def findUserByName(name):
    user = Admins.query.filter_by(username = name).all()
    return user

#other func
def stringfomat(text):
    return text[1:len(text)-2]
    
     
    

# routes
@app.route("/")
def main():
    return 'Home'

@app.route("/log")
def login():
    return render_template('login.html')

@app.route('/checklog' , methods = ['POST','GET'])
def checklog():
    if request.method == 'POST':   
       name = request.form['username']
       password = request.form['password']
       user = Admins.query.filter_by(username = name).first()
       if user and password == user.password:
           return redirect(url_for('adminpage',loguser=name))
       else:
           return render_template('login.html')
    

@app.route("/adminpage/<loguser>")
def adminpage(loguser):
    return render_template('adminpage.html',name=loguser)



#run app
if __name__ == "__main__":
    app.run(debug=True)
    
