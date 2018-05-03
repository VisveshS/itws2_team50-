from flask import *
app=Flask(__name__)
app.secret_key='1@zhKzq7uCVJrsRWHfunJe0NoAbEpQ9nHX1Srde3sl95cH7yww87XJzOmW'
@app.route('/')
def index():
    session['user']='Anthony'
    return '<h1>index</h1>'
@app.route('/get')
def showUser():
    if 'user' in session:
        return session['user']
    return 'nobody'
@app.route('/logout')
def logout():
    session.pop('user', None)
    return '<em>logged out</em>'
if __name__ == '__main__':
    app.run(debug=True)
