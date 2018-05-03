from flask import *
app=Flask(__name__)
@app.route('/login',methods=['GET','POST'])
def login():
    import sqlite3
    error = None
    Uempty=0;
    Pempty=0;
    JJ=None
    if request.method=='POST':
        u=request.form['username'];p=request.form['password'];
        conn=sqlite3.connect('./database/users.db')
        c=conn.cursor()
        c.execute('select id from user where username=? AND password=?',(u,p,))
        JJ=c.fetchone();
        if JJ !=None:JJ=str(JJ[0])
        conn.close()
#        if request.form['username'] == 'correct' and request.form['password'] == 'correct':
        if JJ!=None:
            error = 'log in successful'
        else:
            if request.form['username'] == '':
                Uempty='1'
            else:
                Uempty=None
            if request.form['password'] == '':
                Pempty='1'
            else:
                Pempty=None
            error = 'log in failed'            
    return render_template('login.html',error=error,uempty=Uempty,pempty=Pempty)
if __name__=='__main__':
    app.run(debug=True)
