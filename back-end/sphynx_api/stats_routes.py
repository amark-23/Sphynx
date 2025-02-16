from flask import Blueprint, jsonify
import os
from .config import BASE_DIR

stats_routes = Blueprint("stats_routes", __name__)

@stats_routes.route('/stats', methods=['GET'])
def get_stats():
    """Returns storage usage statistics"""
    total_size = 0
    total_files = 0
    most_recent_upload = None
    latest_time = 0

    try:
        for root, _, files in os.walk(BASE_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
                total_files += 1
                file_mtime = os.path.getmtime(file_path)
                if file_mtime > latest_time:
                    latest_time = file_mtime
                    most_recent_upload = file

        return jsonify({
            "total_files": total_files,
            "total_size": f"{total_size / (1024 * 1024):.2f} MB",
            "most_recent_upload": most_recent_upload or "No files uploaded"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

