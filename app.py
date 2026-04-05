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
    return render_template_string("""
    <html>
    <head>
        <title>DevOps Project</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: #e2e8f0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background: #1e293b;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 0 20px rgba(0,0,0,0.3);
                text-align: center;
            }
            h1 {
                margin-bottom: 10px;
            }
            a {
                display: block;
                margin: 10px;
                color: #38bdf8;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>DevOps Project</h1>
            <p>Flask + CI/CD + Monitoring</p>
            <a href="/health">Health Check</a>
            <a href="/metrics">Metrics</a>
            <a href="/api">API</a>
        </div>
    </body>
    </html>
    """)

@app.route("/health")
def health():
    uptime = time.time() - start_time

    data = {
        "status": "ok",
        "uptime_seconds": round(uptime, 2)
    }

    if "text/html" in request.headers.get("Accept", ""):
        return render_template_string("""
        <html>
        <head>
            <style>
                body { font-family: Arial; background:#0f172a; color:#e2e8f0; text-align:center; padding-top:50px;}
                .card { background:#1e293b; padding:30px; border-radius:12px; display:inline-block;}
                .ok { color:#22c55e; font-size:24px;}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Health Status</h1>
                <p class="ok">OK</p>
                <p>Uptime: {{ uptime }} sec</p>
            </div>
        </body>
        </html>
        """, uptime=data["uptime_seconds"])

    return data, 200

@app.route("/api")
def api():
    return jsonify(
        message="DevOps project running"
    ), 200

@app.route("/metrics")
def metrics():
    data = {
        "requests_total": requests_count
    }

    if "text/html" in request.headers.get("Accept", ""):
        return render_template_string("""
        <html>
        <head>
            <style>
                body { font-family: Arial; background:#020617; color:#e2e8f0; text-align:center; padding-top:50px;}
                .card { background:#1e293b; padding:30px; border-radius:12px; display:inline-block;}
                .metric { font-size:28px; color:#38bdf8;}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Metrics</h1>
                <p>Total Requests</p>
                <p class="metric">{{ requests }}</p>
            </div>
        </body>
        </html>
        """, requests=data["requests_total"])

    return data, 200

@app.route("/fail")
def fail():
    return jsonify(
        error="forced failure"
    ), 500

# ----------------------
# Run
# ----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)