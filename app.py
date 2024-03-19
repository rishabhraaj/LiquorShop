from flask import Flask,render_template,request,flash,redirect,url_for
from user import UserOperation



app=Flask(__name__)

userobj=UserOperation() #User object


@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=="GET":
        return render_template("signup.html")
    else:
        fname=request.form["fname"]
        lname=request.form["lname"]
        user_name=request.form["user_name"]
        email=request.form["email"]
        password=request.form["password"]

        urc=userobj.user_check(user_name)
        erc=userobj.email_check(email)

        if(urc==0 and erc==0):
            userobj.user_insert(fname,lname,user_name,email,password)
            flash("Successfully Registered! Login Now!")
            return redirect(url_for("login"))
        else:
            if(erc!=0 and urc!=0):
                flash("USername and Email already Exists!")
            elif(urc!=0):
                flash("Username already exists!")
            else:
                flash("Email already exists!")
            return redirect(url_for("signup"))


if __name__ == "__main__":
    app.run(debug=True)