from flask import Flask, jsonify, request


app = Flask(__name__)

#home endpoint
@app.route('/')
def home():
    return jsonify(data='My MLE02 Home Page - Welcome to the New SITE!!!!')

if __name__ == '__main__':
    # basically saying if this is being importe then the app wont run
    # only run the app if this script is being executed directly
    app.run(host='0.0.0.0', port=5000)
