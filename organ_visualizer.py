class OrganVisualizer:
    """
    Main class that handles the input and output of the API.
    """
    def __init__(self):
        self.request_count = 0
        self.successful_request_count = 0
    
    def process_description(self, description: OrganDescription) -> OrganVisualization:
        """
        Takes an OrganDescription object as input and returns an OrganVisualization object as output.
        """
        self.request_count += 1
        visualization = OrganVisualization.generate_visualization(description)
        if visualization.is_valid():
            self.successful_request_count += 1
        return visualization
    
    def handle_error(self, description: OrganDescription) -> str:
        """
        Handles errors and returns a clear error message.
        """
        # Placeholder implementation
        return "Invalid organ description"
    
    def log_request(self, description: OrganDescription, visualization: OrganVisualization):
        """
        Logs requests and their outcomes for debugging and performance monitoring purposes.
        """
        # Placeholder implementation
        pass
    
    def get_request_count(self) -> int:
        """
        Returns the total number of requests.
        """
        return self.request_count
    
    def get_successful_request_count(self) -> int:
        """
        Returns the number of successful requests.
        """
        return self.successful_request_count

    def visualize_organ(self, organ_name: str) -> bytes:
        """
        Creates an OrganDescription from the organ name, processes it, and returns a visualization as bytes.
        """
        description = OrganDescription(organ_name)
        visualization = self.process_description(description)
        # Convert the visualization to bytes (this is a placeholder - you'll need to implement this)
        bytes_image = b""
        return bytes_image
