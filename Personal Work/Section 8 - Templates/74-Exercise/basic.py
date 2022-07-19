from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report.html')
def report():
    username = request.args.get('username')
    hasUppercase = any(letter.isupper() for letter in username)
    hasLowercase = any(letter.islower() for letter in username)
    endsWNumber= username[-1].isdigit()
    return render_template('report.html', username=username, hasUppercase = hasUppercase, hasLowercase=hasLowercase, endsWNumber=endsWNumber)


if __name__ == '__main__':
    app.run(debug=True)
