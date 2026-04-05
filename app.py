from flask import Flask, jsonify, request, render_template_string
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
            <a href="/health">Health</a>
            <a href="/metrics">Metrics</a>
            <a href="/dashboard">Dashboard</a>
        </div>
    </body>
    </html>
    """)

@app.route("/health")
def health():
    uptime = round(time.time() - start_time, 2)

    if "text/html" in request.headers.get("Accept", ""):
        return render_template_string("""
        <html>
        <head>
            <title>Health Status</title>
            <style>
                body {
                    background: #020617;
                    color: #e2e8f0;
                    font-family: Arial;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .card {
                    background: #1e293b;
                    padding: 40px;
                    border-radius: 16px;
                    text-align: center;
                    box-shadow: 0 0 25px rgba(0,0,0,0.5);
                }
                .status {
                    color: #22c55e;
                    font-size: 28px;
                    margin: 10px 0;
                }
                .meta {
                    color: #94a3b8;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>System Health</h1>
                <div class="status">OK</div>
                <div class="meta">Uptime: {{ uptime }} sec</div>
            </div>
        </body>
        </html>
        """, uptime=uptime)

    return {
        "status": "ok",
        "uptime_seconds": uptime
    }, 200

@app.route("/api")
def api():
    return jsonify(
        message="DevOps project running"
    ), 200

@app.route("/metrics")
def metrics():
    uptime = time.time() - start_time

    return f"""# =========================
# DevOps Metrics
# =========================

# HELP requests_total Total number of requests
# TYPE requests_total counter
requests_total {requests_count}

# HELP uptime_seconds Application uptime
# TYPE uptime_seconds gauge
uptime_seconds {uptime:.2f}
""", 200, {"Content-Type": "text/plain"}

@app.route("/metrics/ui")
def metrics():
    uptime = time.time() - start_time

    return f"""# =========================
# DevOps Metrics
# =========================

# HELP requests_total Total number of requests
# TYPE requests_total counter
requests_total {requests_count}

# HELP uptime_seconds Application uptime
# TYPE uptime_seconds gauge
uptime_seconds {uptime:.2f}
""", 200, {"Content-Type": "text/plain"}

@app.route("/dashboard")
def dashboard():
    return render_template_string("""
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body { background:#020617; color:#e2e8f0; font-family: Arial; text-align:center; }
            .card { background:#1e293b; padding:20px; border-radius:12px; margin:20px auto; width:400px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Requests Monitor</h2>
            <canvas id="chart"></canvas>
        </div>

        <script>
            let dataPoints = [];

            async function fetchMetrics() {
                const res = await fetch('/metrics');
                const text = await res.text();
                const value = parseInt(text.split(" ").pop());

                dataPoints.push(value);
                if (dataPoints.length > 10) dataPoints.shift();

                chart.data.labels = dataPoints.map((_, i) => i);
                chart.data.datasets[0].data = dataPoints;
                chart.update();
            }

            const ctx = document.getElementById('chart').getContext('2d');
            const chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: [],
                    datasets: [{
                        label: 'Requests',
                        data: [],
                        borderColor: '#38bdf8'
                    }]
                }
            });

            setInterval(fetchMetrics, 2000);
        </script>
    </body>
    </html>
    """)

# ----------------------
# Run
# ----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)