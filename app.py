from flask import Flask, render_template
from network_monitor import check_device

app = Flask(__name__)

@app.route("/")
def dashboard():
    devices = ["8.8.8.8", "1.1.1.1"]
    results = [check_device(ip) for ip in devices]
    return render_template("dashboard.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)