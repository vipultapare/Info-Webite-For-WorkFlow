from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    return render_template('result.html', name=name, email=email, message=message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)