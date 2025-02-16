from flask import Flask
from .file_routes import file_routes
from .folder_routes import folder_routes
from .search_routes import search_routes
from .preview_routes import preview_routes
from .zip_routes import zip_routes
from .stats_routes import stats_routes


app = Flask(__name__)

app.register_blueprint(file_routes)
app.register_blueprint(folder_routes)
app.register_blueprint(search_routes)
app.register_blueprint(preview_routes)
app.register_blueprint(zip_routes)
app.register_blueprint(stats_routes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
