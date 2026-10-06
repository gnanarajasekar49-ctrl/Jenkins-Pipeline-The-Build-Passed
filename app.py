import os
from flask import Flask, jsonify

app = Flask(__name__)

# Read deployment metadata from Docker environment variables
BUILD_NUMBER = os.getenv("BUILD_NUMBER", "unknown")
GIT_COMMIT = os.getenv("GIT_COMMIT", "unknown")
BRANCH_NAME = os.getenv("BRANCH_NAME", "unknown")


@app.route("/")
def home():
    return "Payment application is running"


@app.route("/version")
def version():
    return jsonify({
        "application": "payment",
        "version": BUILD_NUMBER,
        "git_commit": GIT_COMMIT,
        "branch": BRANCH_NAME
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    