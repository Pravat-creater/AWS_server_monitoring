from flask import Flask
import psutil

app = Flask(__name__)

@app.route("/")
def dashboard():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    return f"""
    <h1>Server Health Dashboard</h1>
    CPU: {cpu}%<br>
    Memory: {mem}%<br>
    Disk: {disk}%
    """

if __name__ == "__main__":
    app.run(debug=True)