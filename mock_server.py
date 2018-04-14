from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/sim_status', methods=['POST'])
def json_example():
    req_data = request.get_json()
    print(req_data)

    return jsonify(req_data)

if __name__ == '__main__':
    app.run(port=8000)
