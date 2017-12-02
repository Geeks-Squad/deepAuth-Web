from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    li1=['RAMA',[['Chennai','123'],['Trichy','34'],['Madurai','10']]]
    return render_template('index.html',li=li1)

@app.route('/pending')
def pending():
    li1=['RAMA',[['Rama Ganapathy','Success','City'],['Sreeram Ganesan','Success','City'],['Vyas','Rejected','City']]]
    return render_template('pending.html',li=li1)

@app.route('/view/<userid>',methods=['GET'])
def view(userid):
    li1=['RAMA',['1234 5678 9101','Sreeram','Trichy','sreeram@gmail.com','12345678910','proof1.jpg','proof2.jpg','success','success'],
         ['aadhar no','Name','City','email','phone','proof1_image','proof2_image','Deep AUth status', 'GOV Status / NO']]
    return render_template('view.html',li=li1)
@app.route('/total')
def total():
    li1=['RAMA',[['Rama Ganapathy','Madurai','rama@gmail.com','1234 5678 9101','success','success'],
         ['Sreeram Ganesan','Trichy','sreeram@gmail.com','1234 5678 9102','Rejected','Rejected'],
                 ['name','city','email','aadhaar','deepAuth status','gov status']]]
    return render_template('total.html',li=li1)
@app.route('/approved')
def approved():
    li1=['RAMA',[['Vyas','Madurai','rama@gmail.com','1234 5678 9101','Success','Success'],
         ['Bharani','Trichy','sreeram@gmail.com','1234 5678 9102','Success','Success']]]
    return render_template('approved.html',li=li1)
if __name__ == '__main__':
    app.run(debug=True)
