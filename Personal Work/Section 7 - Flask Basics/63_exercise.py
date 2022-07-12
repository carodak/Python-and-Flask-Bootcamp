# Set up your imports here!
# import ...
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome Nerd! Go to /nerdy_latin/name to see your name in nerdy latin!</h1>"

@app.route('/nerdy_latin/<name>')
def nerdylatin(name):
    nerdy_name = name
    if name[-1]=='y':
        nerdy_name = nerdy_name[:-1]+'iful'
    else:
        nerdy_name = nerdy_name+'y'
    return '<h1>Hi {}! Your nerdylatin name is {}!</h1>'.format(name, nerdy_name)


if __name__ == '__main__':
    app.run(debug=True)
