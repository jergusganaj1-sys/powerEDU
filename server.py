import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Stav servera (jednoduchá simulácia pre powerEDU)
server_state = {
    "status": "online",
    "active_clients": 0,
    "system": "powerEDU Cloud Backend"
}

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "powerEDU Cloud Server je aktívny",
        "status": server_state["status"]
    })

@app.route("/status", methods=["GET"])
def get_status():
    return jsonify(server_state)

@app.route("/shutdown", methods=["POST"])
def master_shutdown():
    # Token alebo kľúč môžeš doplniť neskôr, zatiaľ reaguje priamo
    server_state["status"] = "offline"
    server_state["active_clients"] = 0
    return jsonify({"message": "⚡ MASTER SHUTDOWN úspešne vykonaný!"}), 200

if __name__ == "__main__":
    # Render automaticky pridelí port cez premennú prostredia PORT, inak predvolený 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
