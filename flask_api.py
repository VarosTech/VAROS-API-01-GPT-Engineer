from flask import Flask, request, Response
from organ_visualizer import OrganVisualizer

class FlaskAPI:
    """
    Class that sets up the Flask API framework and handles the HTTP requests
    """
    def __init__(self, organ_visualizer: OrganVisualizer):
        """
        Initializes the class and sets up the necessary libraries and dependencies
        """
        self.app = Flask(__name__)
        self.organ_visualizer = organ_visualizer
        self.setup_routes()

    def setup_routes(self):
        """
        Method that sets up the Flask API routes
        """
        @self.app.route('/visualize_organ', methods=['POST'])
        def visualize_organ():
            organ_description = request.json.get('organ_description')
            bytes_image = self.organ_visualizer.visualize_organ(organ_description)
            return Response(bytes_image, mimetype='image/png')

        @self.app.route('/organ/visualize/<organ_name>', methods=['GET'])
        def visualize_organ_by_name(organ_name):
            try:
                jpeg_bytes = self.organ_visualizer.visualize_organ(organ_name)
                return Response(jpeg_bytes, mimetype="image/jpeg")
            except ValueError as e:
                return str(e), 400

    def run(self):
        """
        Method that starts the Flask API server and listens for incoming requests
        """
        self.app.run()


if __name__ == '__main__':
    ov = OrganVisualizer()
    api = FlaskAPI(ov)
    api.run()
