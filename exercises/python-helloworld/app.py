from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    response = {}
    response['status'] = 200
    response['data'] = {
        'result': 'OK - healthy'
    } 
    return jsonify(response)

@app.route("/metrics")
def metrics():
    response = {}
    response['status'] = 200
    response['data'] = {
        'UserCount': 140,
        'UserCountActive': 23
    } 
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
