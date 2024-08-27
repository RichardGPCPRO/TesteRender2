from flask import Flask

app = Flask(__name__)

@app.get('/')
def index():
    return 'app renderizado'

@app.get('/inscrito/<nome_inscrito>')
def inscrito(nome_inscrito):
    return f"olá {nome_inscrito}"

@app.get('/melhorcanaldoyoutube')
def meucanal():
    return 'é o programação na prática'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
#if __name__ == '__main__': 
    #app.run()
