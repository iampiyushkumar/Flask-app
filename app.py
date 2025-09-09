from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome, Piyush!"

@app.route("/<name>")
def greet(name):
    # Simple normalization: "piyush" -> "Piyush"
    return f"Welcome, {name.capitalize()}!"

if __name__ == "__main__":
    # Bind to 0.0.0.0 so it's reachable from Docker
    app.run(host="0.0.0.0", port=5000)
