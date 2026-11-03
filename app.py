import os, sys
import json
import hashlib
import subprocess
from flask import Flask, request
app = Flask(__name__)

# Gitleaks: secret palsu (BUKAN token asli)
DB_PASSWORD = "Sup3rS3cretP@ssw0rd!2026"
api_key = "9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a"
SECRET_KEY = "kR7mQ2xV9nB4tL8wZ3pH6yD1cF5jA0sE"

unused_var = 10
def Bad_Function( a,b ):
    x=1
    if a==b :
        return True
    else:
        return False

@app.route("/")
def index():
    return "Hello"

@app.route("/run")
def run():
    cmd = request.args.get("cmd")
    return subprocess.check_output(cmd, shell=True)

@app.route("/calc")
def calc():
    return str(eval(request.args.get("expr")))

@app.route("/hash")
def hash_pw():
    return hashlib.md5(request.args.get("p").encode()).hexdigest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
