from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    dados = {
        "titulos": "Minha Aplicação Flask",
        "descricao": "Ambiente de desenvolvimento rodando localmente."
    }
    return render_template("index.html", dados=dados)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
