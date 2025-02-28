from flask import Flask
from flask_cors import CORS
from routes.users import users_bp
from routes.matchups import matchups_bp

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests
@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

# Register routes
app.register_blueprint(users_bp, url_prefix="/api/users")
app.register_blueprint(matchups_bp, url_prefix="/api/matchups")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

