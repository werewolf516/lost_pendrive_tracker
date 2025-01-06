from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to receive data
@app.route("/receive-data", methods=["POST"])
def receive_data():
    data = request.get_json()
    if data:
        with open("received_geolocation.txt", "a") as file:
            file.write(f"\n--- Received Data ---\n")
            for key, value in data.items():
                file.write(f"{key.capitalize()}: {value}\n")
        return jsonify({"message": "Data received and saved."}), 200
    return jsonify({"error": "No data received."}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

