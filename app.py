from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route("/api/marina", methods=["POST"])
def run_marina():
    data = request.get_json()
    proposition = data.get("proposition") if data else None
    if not proposition:
        return jsonify({"error": "No proposition provided"}), 400
    
    try:
        marina_bin = os.path.join("/app/marina", "marina")
        result = subprocess.run(
            [marina_bin, proposition],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            return jsonify({"error": result.stderr.strip()}), 500
        return jsonify({"result": result.stdout.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
