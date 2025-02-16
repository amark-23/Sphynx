from flask import Blueprint, jsonify, send_file, request
import os
import zipfile
import shutil
from .config import BASE_DIR

zip_routes = Blueprint("zip_routes", __name__)

@zip_routes.route('/zip', methods=['GET'])
def zip_folder():
    """Compresses a folder into a ZIP and allows downloading it"""
    folder_name = request.args.get('folder')

    if not folder_name:
        return jsonify({"error": "Missing folder name"}), 400

    folder_path = os.path.join(BASE_DIR, folder_name)

    if not os.path.exists(folder_path):
        return jsonify({"error": "Folder does not exist"}), 404

    if not os.path.isdir(folder_path):
        return jsonify({"error": "Not a folder"}), 400

    zip_filename = f"{folder_name}.zip"
    zip_path = os.path.join(BASE_DIR, zip_filename)

    try:
        # Create a ZIP file
        shutil.make_archive(zip_path.replace(".zip", ""), 'zip', folder_path)

        return send_file(zip_path, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Clean up ZIP file after sending
        if os.path.exists(zip_path):
            os.remove(zip_path)

