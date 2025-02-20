from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Import the CORS extension
from backend.model import ActivityRecommender
from backend.database import get_session, Activity

app = Flask(__name__)

# Enable CORS for the entire app
CORS(app)

@app.route('/')
def index():
    # Serve the frontend template
    return render_template('index.html')

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    # Get query parameters from the request
    category = request.args.get('category')
    zone = request.args.get('zone')
    age_range = request.args.get('age_range')

    # Validate the category parameter
    if not category:
        return jsonify({"error": "Category is required"}), 400

    # Normalize zone and age_range to lowercase to avoid case mismatch
    if zone:
        zone = zone.lower()  # Convert zone to lowercase
    if age_range:
        age_range = age_range.lower()  # Convert age_range to lowercase

    # If no zone or age range is provided, set them to None
    if not zone:
        zone = None
    if not age_range:
        age_range = None

    # Get recommendations from the AI model
    recommender = ActivityRecommender()
    activities = recommender.recommend(category, zone, age_range)

    # Check if there are activities returned
    if not activities:
        return jsonify({"error": "No activities found for the given parameters"}), 404

    # Return the activities in JSON format
    return jsonify(activities)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
