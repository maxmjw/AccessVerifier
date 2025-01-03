from flask import Flask, request, jsonify
import subprocess 
from app.utils import load_allowed_ips, extract_client_ip
from app.ip_updater import update_ips

app = Flask(__name__)

# Update IPs before starting the app
try:
    update_ips()
    app.logger.info("IP list updated successfully.")
except Exception as e:
    app.logger.error(f"Failed to update IP list: {e}")

# Load allowed IPs
allowed_ips = load_allowed_ips()
if not allowed_ips:
    app.logger.warning("Allowed IPs list is empty. All requests will be denied.")

if not allowed_ips:
    app.logger.warning("Allowed IPs list is empty. All requests will be denied.")

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200


@app.route("/verify", methods=["POST"])
def verify_access():
    """
    Endpoint for ip verification.
    """
    try:
        headers = request.get_data(as_text=True)
        client_ip = extract_client_ip(headers)
    except Exception as e:
        app.logger.error(f"Failed to extract client IP: {e}")
        return jsonify({"status": "error", "message": "Invalid request"}), 400

    if client_ip in allowed_ips:
        return jsonify({"status": "allowed"}), 200
    else:
        return jsonify({"status": "unauthorized"}), 401

@app.route("/refresh", methods=["POST"])
def refresh_ips():
    """
    Refresh the list of allowed IPs.
    """
    global allowed_ips
    allowed_ips = load_allowed_ips()
    app.logger.info("Allowed IPs list refreshed.")
    return jsonify({"status": "refreshed", "ips": allowed_ips}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)