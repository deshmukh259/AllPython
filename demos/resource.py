from flask import Flask

app = Flask(__name__)

@app.route("/index/<order>")
def index(order):
    print("indexxx")
    return order;


if __name__ == '__main__':
    print(__name__)
    print(app)
    app.run(host="0.0.0.0",port=80)

