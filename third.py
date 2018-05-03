#from flask import Flask,render_template, url_for,request,redirect
from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 style=color:blue>This is an index page\n\n(Login and signup comes here)</h1>"
@app.route('/welcome/')
@app.route('/welcome/<Song>')
@app.route('/welcome/<input>/<Song>')
def hello(input=None,Song=None):
    #if input == None:return "<h2 style=color:red>ANONYMOUS</h2>"
    #else:return "<h1 style=color:green>HELLO %s !</h1>" % input
    return render_template('hello.html',name=input,song=Song)
@app.route('/test1/')
def test1():
    fname = 'hello'
    return "url for function %s=<h1/>%s" % (fname,url_for(fname))
    #return redirect(url_for(fname))#redirection
@app.errorhandler(404)
def page_error(therror):
        return "<h1 style=color:blue>SOME ERROR OCCURRED SOMEWHERE SOMEHOW :( </h1>"
if __name__=='__main__':
    app.run(debug=True)
