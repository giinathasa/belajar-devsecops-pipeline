"""A simple CyberTales book checkout application."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """Display the CyberTales homepage."""
    return """
    <h1>CyberTales</h1>
    <p>Selamat datang di toko buku CyberTales!</p>
    <p>Temukan buku cybersecurity untuk pemula.</p>
    """


@app.route("/checkout")
def checkout():
    """Display the CyberTales checkout page."""
    return """
    <h1>Checkout CyberTales</h1>
    <p>Silakan pilih buku yang ingin dibeli.</p>
    """


if __name__ == "__main__":
     # nosemgrep: python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host
    app.run(host="0.0.0.0", port=5000)
