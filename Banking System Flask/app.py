import random
from flask import Flask, request, render_template
app = Flask(__name__)

headings=['Name', 'Phone', 'Aadhar No','Account No','Balance (in ₹)']
data= [
    ['Ankit', 9475937912, 4912,98765, 100.0],
]
headers=['Name', 'Phone', 'Aadhar No','PIN','Account No','Balance']
data_private= [
    ['Ankit', 9475937912, 4912,1234,98765, 100.0],
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/confirm',methods=['POST','GET'])
def confirm():
    name = request.form['fname']
    phone = int(request.form['phone'])
    password= int(request.form['pass'])
    aadhar=int(request.form['aadhar'])
    balance =float(request.form['money'])
    account = random.randint(10000,99999+1)
    lisg=[name, phone, aadhar,account,balance,]
    lips=[name, phone, aadhar,password,account,balance,]
    data.append(lisg)
    data_private.append(lips)
    return render_template("confirm.html",name=name,phone=phone, account=account, balance=balance, aadhar=aadhar)

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/welcome',methods=['POST','GET'])
def welcome():
    accounter = int(request.form['accounter'])
    passcheck = int(request.form['passcheck'])
    for i in range(len(data_private)):
        if accounter ==data_private[i][4] and passcheck ==data_private[i][3]:
            account  = accounter
            return render_template("welcome.html",accounter=account,name=data_private[i][0], account=data_private[i][4],phone=data_private[i][1],aadhar=data_private[i][2],balance=data_private[i][5])
    else:
        return render_template("error.html")

@app.route('/error',methods=['POST','GET'])
def error():
    accounter = int(request.form['accounter'])
    passcheck = int(request.form['passcheck'])
    for i in data_private:
        if accounter not in i or passcheck not in i:
            return render_template("error.html")

@app.route('/transaction',methods=['POST','GET'])
def transation():
    return render_template("withdraw_deposit.html")

@app.route('/success',methods=['POST','GET'])
def withdraw():
    accounter = int(request.form['accounteck'])
    passcheck = int(request.form['passbook'])
    transaction= int(request.form['transaction'])
    money = float(request.form['money'])
    for i in range(len(data_private)):
        if accounter ==data_private[i][4] and passcheck ==data_private[i][3]:
            if transaction==1:
                data_private[i][5]+=money
                data[i][4]+=money
                return render_template("success.html",name=data_private[i][0], account=data_private[i][4],phone=data_private[i][1],aadhar=data_private[i][2],balance=data_private[i][5])
            elif transaction==0:
                data_private[i][5]-=money
                data[i][4]-=money
                return render_template("success.html",name=data_private[i][0], account=data_private[i][4],phone=data_private[i][1],aadhar=data_private[i][2],balance=data_private[i][5])
    else:
        return render_template("error_deposit.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route("/display",methods=['POST','GET'])
def display():
    return render_template("display.html", headings=headings, data= data)



if __name__=='__main__':
    app.run(debug=True)