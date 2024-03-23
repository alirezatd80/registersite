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
    
class RegisteredUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phonenumber = db.Column(db.String(20), nullable=False)
    typeuser = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"{self.fullname},{self.age},{self.email},{self.phonenumber},{self.type}"

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

def addRegisterUser(name,age,email,phonenumber,typeuser):
   adduser =  RegisteredUser(fullname = name , age = age , email = email , phonenumber = phonenumber , typeuser=typeuser)
   db.session.add(adduser)
   db.session.commit()
    

#other func
def stringfomat(text):
    return text[1:len(text)-2]
    
     
    

# routes
@app.route("/")
def main():
    
    return render_template('main.html')

@app.route('/Register' , methods = ['POST','GET'])
def register():
    if request.method =='POST':
        name = request.form['FullName']
        age = request.form['Age']
        email = request.form['email']
        phonenumber = request.form['PhoneNumber']
        typeuser = request.form['section']
        addRegisterUser(name,age,email,phonenumber,typeuser)
        return render_template('main.html')
    else:
        return render_template('main.html')
            


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
    users = RegisteredUser.query.all()
    return render_template('adminpage.html',name=loguser,users=users)



#run app
if __name__ == "__main__":
    app.run(debug=True)
    
