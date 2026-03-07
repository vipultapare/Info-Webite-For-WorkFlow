from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    """Return a greeting message."""
    return jsonify({"message": "Hello from Docker!"})


@app.route("/health")
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy"}), 200


@app.route("/api/data")
def get_data():
    """Return sample data."""
    data = {
        "id": 1,
        "name": "Sample Data",
        "status": "active"
    }
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)