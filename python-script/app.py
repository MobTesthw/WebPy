from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_three():
    data = request.get_json()
    number = data.get('number')
    result = number + 3
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)