from flask import Flask,render_template, request
from MySQL import mysql
app=Flask(__name__)
@app.route('/register', methods=['GET','POST'])
def register():
    msg=''
    if request.method =='POST' and 'username' in request.form and 'password' in request.form and "email" in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        mydb = mysql.connector.connect(
            host='remotemysql.com',
            user='Rz8hqnldk4',
            password ="nd0wk03xe0",
            database="Rz8hqnldk4"

        )
        mycursor = mydb.cursor()
        print(username,password,email)
        mycursor.execute('SELECT * FROM LoginDetails WHERE Name = %s AND Password = %s',(username,email))

        account = mycursor.fetchone()
        print(account)
        if account:
            msg='Account already exist!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'(A-Za-z0-9)+', Username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Kindly fill out the details!'
        else:
            mycursor.execute('INSERT INTO LoginDetails(Name,Password,Email) VALUES (%s,%s,%s)',(username,password,email))
            mydb.commit()
            msg = 'Your registration is Successful!'
            name=username

            return render_template('index.html', msg=msg,name=name)
    elif request.method == 'POST':
            msg = 'Kindly fill out the details!'
            return render_template('register.html', msg=msg)
            
       
    
