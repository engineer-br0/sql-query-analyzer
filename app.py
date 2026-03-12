from flask import Flask, request, jsonify;
from flask_cors import CORS
from analyzer import analyze_query

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/', methods=["GET"])
def home():
    return jsonify({
        "message": "sql query analyzer is running;.."
    })
    
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    
    query = data.get("query", "")
    
    suggestions = analyze_query(query)
    
    return jsonify({
        "query": query,
        "suggestions": suggestions
    })

# if __name__ == "__main__":
#     app.run(debug=True, port=9001)