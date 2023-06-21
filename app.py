from flask import Flask, request, jsonify
from organ_visualizer import OrganVisualizer, OrganDescription

app = Flask(__name__)
visualizer = OrganVisualizer()

@app.route('/visualize', methods=['POST'])
def visualize_organ():
    """
    Endpoint for visualizing an organ based on a text-based description.
    """
    description = OrganDescription(request.json['description'])
    visualization = visualizer.process_description(description)
    if visualization.is_valid():
        visualizer.log_request(description, visualization)
        return jsonify({"organ": visualization.get_organ(), "condition": visualization.get_condition()}), 200
    else:
        error_message = visualizer.handle_error(description)
        return jsonify({"error": error_message}), 400
