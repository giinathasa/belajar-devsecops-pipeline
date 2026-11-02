"""Aplikasi Flask sederhana untuk pengujian pipeline."""
import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    """Endpoint utama."""
    return jsonify(message="Hello DevSecOps", status="ok")


@app.route("/health")
def health():
    """Endpoint health check."""
    return jsonify(status="healthy")


@app.after_request
def add_security_headers(response):
    """Tambahkan header keamanan dasar."""
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "5000")))
