from flask import jsonify
from service import app

COUNTERS = {}


@app.route("/health")
def health():
    return jsonify(status="OK"), 200


@app.route("/")
def index():
    return jsonify(name="Counter Service", version="1.0"), 200


@app.route("/counters/<name>", methods=["POST"])
def create_counter(name):
    app.logger.info("Request to create counter: %s", name)
    if name in COUNTERS:
        return jsonify(error=f"Counter {name} already exists"), 409
    COUNTERS[name] = 0
    return jsonify({name: COUNTERS[name]}), 201


@app.route("/counters/<name>", methods=["GET"])
def read_counter(name):
    app.logger.info("Request to read counter: %s", name)
    if name not in COUNTERS:
        return jsonify(error=f"Counter {name} does not exist"), 404
    return jsonify({name: COUNTERS[name]}), 200


@app.route("/counters/<name>", methods=["PUT"])
def update_counter(name):
    app.logger.info("Request to update counter: %s", name)
    if name not in COUNTERS:
        return jsonify(error=f"Counter {name} does not exist"), 404
    COUNTERS[name] += 1
    return jsonify({name: COUNTERS[name]}), 200


@app.route("/counters/<name>", methods=["DELETE"])
def delete_counter(name):
    app.logger.info("Request to delete counter: %s", name)
    COUNTERS.pop(name, None)
    return "", 204
