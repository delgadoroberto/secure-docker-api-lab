from flask import Flask, request
import subprocess
import os
import re

app = Flask(__name__)

SECRET_TOKEN = os.getenv("SECRET_TOKEN")

@app.route("/")
def home():
    return "Docker Vulnerable API"

@app.route("/dns")
def dns_lookup():
    domain = request.args.get("domain")

    if not re.match(r'^[a-zA-Z0-9.-]+$', domain):
        return "Invalid domain", 400

    result = subprocess.check_output(
        ["/usr/bin/nslookup", domain]
    )

    return result

if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1")
