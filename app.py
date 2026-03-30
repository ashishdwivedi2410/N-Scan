from flask import Flask, render_template
from sniffer import start_sniffing
from database import get_logs
import threading

app = Flask(__name__)

@app.route("/")
def dashboard():
    logs = get_logs()
    return render_template("dashboard.html", logs=logs)

def run_sniffer():
    start_sniffing()

if __name__ == "__main__":
    t = threading.Thread(target=run_sniffer)
    t.daemon = True
    t.start()

    app.run(debug=True)
