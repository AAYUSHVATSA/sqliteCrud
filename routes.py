import sqlite3
from flask import *
app=Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/saveDetails',methods=['POST'])
def saveDetails():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        address=request.form['address']
        con =sqlite3.connect('employee.db')    
        cur=con.cursor()
        cur.execute('INSERT INTO Employees values(NULL,?,?,?)',(name,email,address))
        con.commit()
        msg='Data Added successfully '
        con.close()
        return render_template('success.html',msg=msg)


@app.route('/view')
def view():
    con =sqlite3.connect('employee.db')    
    cur=con.cursor()
    cur.execute('select * from Employees')
    rows=cur.fetchall()
    con.close()
    return render_template('view.html',rows=rows)

@app.route('/edit/<id>')
def edit(id):
    con =sqlite3.connect('employee.db')    
    cur=con.cursor()
    cur.execute('select * from Employees where id =?',(id,))
    rows=cur.fetchall()
    con.close()
    return render_template('edit.html',rows=rows)



@app.route('/saveEditDetails/<id>',methods=['POST'])
def saveEditDetails(id):
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        address=request.form['address']
        con =sqlite3.connect('employee.db')    
        cur=con.cursor()
        cur.execute('UPDATE Employees set name=?,email=?,address=? where id=?',(name,email,address,id))
        con.commit()
        msg='Data Edit successfully '
        con.close()
        return render_template('success.html',msg=msg)

@app.route('/delete/<id>')
def deleteRecord(id):
    con =sqlite3.connect('employee.db')    
    cur=con.cursor()
    cur.execute('delete from Employees where id =?',(id,))
    con.commit() 
    con.close()
    return redirect(url_for('view'))


if __name__=='__main__':
    app.run(debug=True)