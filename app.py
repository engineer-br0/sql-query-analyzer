from flask import Flask, jsonify;

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return jsonify({
        "message": "sql query analyzer is running;.."
    })
    
    

if __name__ == "__main__":
    app.run(debug=True, port=9001)