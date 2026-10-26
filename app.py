
from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello! My Python app is running in Docker!",
        "hostname": socket.gethostname(),
        "status": "success"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/info")
def info():
    return jsonify({
        "app": "Docker Practice App",
        "port": int(os.environ.get("PORT", 5000)),
        "hostname": socket.gethostname()
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
