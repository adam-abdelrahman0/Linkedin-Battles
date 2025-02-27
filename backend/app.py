from flask import Flask
from flask_cors import CORS
from routes.users import users_bp
from routes.matchups import matchups_bp

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Register routes
app.register_blueprint(users_bp, url_prefix="/api/users")
app.register_blueprint(matchups_bp, url_prefix="/api/matchups")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

