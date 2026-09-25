existing_models = ["Beedle", "Crossroads", "M2", "Panique"]

from flask import Flask, jsonify

app = Flask(__name__)


def find_model(model):
    for model in existing_models:
        if model in existing_models:
            return model

    return None


@app.route("/")
def welcome():
    return jsonify({"message": "Welcome to Flatiron Cars"}), 200


@app.route("/<model>")
def get_model(model):
    raw_model = find_model(model)

    if raw_model is None:
        return jsonify({"error": "No models called {model} exists in our catalog"}), 404

    return jsonify({"message": "Flatiron {model} is in our fleet"}), 200


if __name__ == "__main__":
    app.run(debug=True)
