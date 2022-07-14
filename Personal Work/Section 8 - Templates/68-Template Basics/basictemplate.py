from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Pika"
    letters = list(name)
    nerds_dictionary = {'nerd_name' : 'Sam'}
    return render_template('basic.html', name=name, letters=letters, nerds_dictionary = nerds_dictionary)

if __name__ == '__main__':
    app.run(debug=True)
