import mysql.connector

class UserOperation():
    def connection(self):
        con=mysql.connector.connect(host="localhost",port="3306",user="root",password="Rish@880abh",database="cheers&co.")
        return con
    
    def user_insert(self,fname,lname,user_name,email,password):
        db=self.connection()
        mycursor=db.cursor()

        sq="insert into user (fname,lname,user_name,email,password) values (%s,%s,%s,%s,%s)"
        record=[fname,lname,user_name,email,password]
        
        mycursor.execute(sq,record)
        db.commit()

        mycursor.close()
        db.close()
        return
    
    def user_check(self,user_name):
        db=self.connection()
        mycursor=db.cursor()

        sq="select user_name from user where user_name=%s"
        record=[user_name]

        mycursor.execute(sq,record)
        mycursor.fetchall()
        urc=mycursor.rowcount

        if(urc==0):
            return 0
        else:
            return 1
        
    def email_check(self,email):
        db=self.connection()
        mycursor=db.cursor()

        sq="select email from user where email=%s"
        record=[email]

        mycursor.execute(sq,record)
        mycursor.fetchall()
        erc=mycursor.rowcount

        if(erc==0):
            return 0
        else:
            return 1
        

    
    


        
