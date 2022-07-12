from flask import Flask # from flask package import Flask class

# Create an application object as an instance of the Flask class
# name = python predefined variable set to the name of the modulee in which it is used
# if name = __main__, we are directly running the module
app = Flask(__name__)

@app.route('/') #127.0.0.1:5000
def index():
    return "<h1> Hello Nerd! </h1>"

@app.route('/information') #127.0.0.1:5000/information
def info():
    return "<h1> You are a cute nerd! </h1>"

@app.route('/nerd/<name>') #the name would be directly passed in the url
def nerd(name):
    return '<h1> Welcome to your page {}! 100th letter: {}</h1>'.format(name.upper(), name[100])

if __name__ == '__main__':
    app.run(debug=True)
