from flask import Flask, request, jsonify



app = Flask(__name__)


@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')

    if num1 is None or num2 is None:
        return jsonify({'error': 'Missing parameters'}), 400

    try:
        result = int(num1) + int(num2)
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
