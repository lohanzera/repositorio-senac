from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Página inicial com o botão

@app.route('/login')
def login():
    return render_template('login.html')  # Página de login

if __name__ == '__main__':
    app.run(debug=True)