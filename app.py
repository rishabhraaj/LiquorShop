from flask import Flask,render_template,request,flash,redirect,url_for
from user import UserOperation
from encryption import Encryption
from validate import MyValidate


app=Flask(__name__)

app.secret_key="88098as0d8a0sd8asd"

userobj=UserOperation() #User object
validobj=MyValidate()  #Validation object


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

        # ******************** PASSWORD ENCRYPTION ***********
        e=Encryption()
        password=e.convert(password)

        # ******************** VALIDATION (FORM FIELDS SHOULD NOT BE EMPTY) ***********************
        frm=[fname,lname,user_name,email,password]
        if(not validobj.required(frm)):
            flash("The field Cannot be empty!")
            return redirect(url_for("signup"))
        

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

@app.route("/otp_verify")
def otp_verify():
    return render_template("otp.html")
if __name__ == "__main__":
    app.run(debug=True)