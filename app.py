from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Mock service status data representing internal platform services
SERVICES = [
    {"name": "Adviser Portal",      "status": "operational",  "uptime": "99.98%"},
    {"name": "Document Service",    "status": "operational",  "uptime": "99.95%"},
    {"name": "Notification Engine", "status": "degraded",     "uptime": "97.32%"},
    {"name": "Reporting API",       "status": "operational",  "uptime": "99.87%"},
    {"name": "Authentication",      "status": "operational",  "uptime": "100.00%"},
    {"name": "Data Sync Service",   "status": "maintenance",  "uptime": "98.61%"},
]

@app.route("/")
def index():
    now = datetime.utcnow().strftime("%d %B %Y, %H:%M UTC")
    operational = sum(1 for s in SERVICES if s["status"] == "operational")
    return render_template(
        "index.html",
        services=SERVICES,
        last_updated=now,
        operational=operational,
        total=len(SERVICES)
    )

@app.route("/health")
def health():
    # Health check endpoint used by Render to confirm the app is running
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)