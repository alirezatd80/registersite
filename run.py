from flask import Flask,render_template,redirect,request,url_for

app = Flask(__name__)

@app.route("/")
def main():
    return 'hi'

@app.route("/log")
def login():
    return render_template('login.html')
    

if __name__ == "__main__":
    app.run(debug=True)
    
