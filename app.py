from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def register():
    return render_template('register.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return render_template('success.html', name=name, email=email)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7000, debug=True)