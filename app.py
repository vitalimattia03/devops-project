from flask import Flask, jsonify
import time
import logging

app = Flask(__name__)

# ----------------------
# Logging setup
# ----------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# ----------------------
# Metrics
# ----------------------
start_time = time.time()
requests_count = 0

# ----------------------
# Middleware
# ----------------------
@app.before_request
def before_request():
    global requests_count
    requests_count += 1
    app.logger.info("Request received")

@app.after_request
def after_request(response):
    app.logger.info(f"Response: {response.status_code}")
    return response

# ----------------------
# Routes
# ----------------------
@app.route("/")
def home():
    return "OK", 200

@app.route("/health")
def health():
    uptime = time.time() - start_time
    return jsonify(
        status="ok",
        uptime_seconds=uptime
    ), 200

@app.route("/api")
def api():
    return jsonify(
        message="DevOps project running"
    ), 200

@app.route("/metrics")
def metrics():
    return jsonify(
        requests_total=requests_count
    ), 200

@app.route("/fail")
def fail():
    return jsonify(
        error="forced failure"
    ), 500

# ----------------------
# Run
# ----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)