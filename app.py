from flask import Flask, request
import subprocess

app = Flask(__name__)

SECRET_TOKEN = "MY-TOP-SECRET-TOKEN"

@app.route("/")
def home():
    return "Docker Vulnerable API"

@app.route("/dns")
def dns_lookup():
    domain = request.args.get("domain")

    result = subprocess.check_output(
        f"nslookup {domain}",
        shell=True
    )

    return result

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
