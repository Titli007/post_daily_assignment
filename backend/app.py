from flask import Flask

app = Flask(__name__)

# Register your blueprints (assuming your routes are in news.py)
from routes.news_routes import news_bp  # Adjust the import according to your package structure
app.register_blueprint(news_bp)

@app.route('/')
def index():
    return "Welcome to the News API!"

if __name__ == '__main__':
    app.run(debug=True)

