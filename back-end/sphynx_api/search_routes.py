from flask import Blueprint, jsonify, request
import os
from .config import BASE_DIR

search_routes = Blueprint("search_routes", __name__)

@search_routes.route('/search', methods=['GET'])
def search_files():
    """Searches for files"""
    query = request.args.get('query', '').lower()
    folder = request.args.get('folder', '').strip()

    if not query:
        return jsonify({"error": "Missing search query"}), 400

    search_dir = os.path.join(BASE_DIR, folder) if folder else BASE_DIR

    if not os.path.exists(search_dir):
        return jsonify({"error": "Folder does not exist"}), 404

    try:
        matched_files = []
        for root, _, files in os.walk(search_dir):
            for file in files:
                if query in file.lower():
                    matched_files.append(os.path.relpath(os.path.join(root, file), BASE_DIR))

        return jsonify({"query": query, "folder": folder, "matched_files": matched_files})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
