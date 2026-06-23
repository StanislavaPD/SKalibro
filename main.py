from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    print("ROUTE WORKS")
    return "SKalibro is running!"

if __name__ == "__main__":
    print("STARTING SERVER...")
    app.run(debug=True)