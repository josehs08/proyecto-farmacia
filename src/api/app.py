from flask import Flask, jsonify, request

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def root():
    return 'Hello World!'

@app.route("/api")
def api_test():
    return "API Test"

@app.route("/api2")
def api_test2():
    return "API Test 2"