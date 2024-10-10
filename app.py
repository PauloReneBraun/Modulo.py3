from flask import Flask # type: ignore

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/about")
def about():
    return "About me"

if __name__ == "__main__":
  app.run(debug=True)