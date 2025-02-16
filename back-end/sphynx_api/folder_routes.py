from flask import Blueprint, jsonify, request
import os
from .config import BASE_DIR

folder_routes = Blueprint("folder_routes", __name__)

@folder_routes.route('/mkdir', methods=['POST'])
def create_folder():
    """Creates a folder"""
    folder_name = request.args.get('name')

    if not folder_name:
        return jsonify({"error": "Missing folder name"}), 400

    folder_path = os.path.join(BASE_DIR, folder_name)

    if os.path.exists(folder_path):
        return jsonify({"error": "Folder already exists"}), 400

    try:
        os.makedirs(folder_path)
        return jsonify({"message": "Folder created successfully", "folder_name": folder_name})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@folder_routes.route('/rmdir', methods=['DELETE'])
def delete_folder():
    """Deletes a folder (only if empty)"""
    folder_name = request.args.get('name')

    if not folder_name:
        return jsonify({"error": "Missing folder name"}), 400

    folder_path = os.path.join(BASE_DIR, folder_name)

    if not os.path.exists(folder_path):
        return jsonify({"error": "Folder not found"}), 404

    if not os.path.isdir(folder_path):
        return jsonify({"error": "Not a folder"}), 400

    if os.listdir(folder_path):
        return jsonify({"error": "Folder is not empty"}), 400

    try:
        os.rmdir(folder_path)
        return jsonify({"message": "Folder deleted successfully", "folder_name": folder_name})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
