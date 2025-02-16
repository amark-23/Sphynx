from flask import Blueprint, jsonify, send_file, request
import os
import mimetypes
from .config import BASE_DIR

preview_routes = Blueprint("preview_routes", __name__)

@preview_routes.route('/preview/<path:filename>', methods=['GET'])
def preview_file(filename):
    """Previews images and text files from the external HDD"""
    file_path = os.path.join(BASE_DIR, filename)

    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    mime_type, _ = mimetypes.guess_type(file_path)

    if mime_type and mime_type.startswith("image"):
        # Return image files directly
        return send_file(file_path, mimetype=mime_type)

    elif mime_type and mime_type.startswith("text"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            return jsonify({"filename": filename, "content": content})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    else:
        return jsonify({"error": "Preview not supported for this file type"}), 400

