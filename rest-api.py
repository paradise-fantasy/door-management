from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/open-door', methods=['GET'])
def get_tasks():
#    return jsonify({'tasks': tasks})
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)
