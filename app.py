from flask import Flask

app = Flask(__name__)

n = 0

@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/hello')
def hello_aditya():
    global n 
    n += 1
    return f"Hello Abbas, You have visited the page for {n} times"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)