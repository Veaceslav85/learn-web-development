from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1 style="text-align:center">ZAEBALI</h1>'\
    '<p style="text-align:center ">Priehali</p>'\
    '<img src="">'


@app.route("/bye")
def bye():
        return 'bye-bye'

@app.route('/<name>/<int:years>')
def salut(name,years):
    return f"Salut drujok, {name}, ai {years} ani?"

mesajul = "Privet"
print(mesajul)
var = 1
print(var)

if __name__=="__main__":
    app.run(debug=True)