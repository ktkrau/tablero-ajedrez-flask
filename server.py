from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<int:n>')
def index(n):
    return render_template('index.html', n=n, n2=4)

@app.route('/<int:n>/<int:n2>')
def nivel_dos(n2, n):
    return render_template('index.html', n2=n2, n=n)



if __name__=="__main__":
    app.run(debug=True)

