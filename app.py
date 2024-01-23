from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/home2", methods=['GET'])
def home2():
    return render_template("index2.html")

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)