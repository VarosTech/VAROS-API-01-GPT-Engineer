from flask import jsonify
from typing import Dict

def handle_error(error_message: str) -> Dict[str, str]:
    response = {"error": error_message}
    return jsonify(response)
