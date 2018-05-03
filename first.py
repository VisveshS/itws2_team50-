from flask import Flask
app=Flask(__name__)
@app.route('/')
def helloworld():
    return "<h1 style=color:blue>HOME</h1>"
@app.route('/child1')
def helloworldc():
    return "<h3 style=color:green><em>child</em></h3>"
if __name__=='__main__':
    app.run(debug=True)
