from flask import Flask,render_template,redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admins.db'
db = SQLAlchemy(app)

class Admins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return f"Admin('{self.username}')"

with app.app_context():
      
       db.create_all()
       
def AddAdmin(name , passsword):
    admin = Admins(username = name , password=passsword)
    db.session.add(admin)
    db.session.commit()

@app.route("/")
def main():
    return 'hi'

@app.route("/log")
def login():
    return render_template('login.html')
    

if __name__ == "__main__":
    app.run(debug=True)
    
