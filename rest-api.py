from flask import Flask
from unlocker import unlock

app = Flask(__name__)

@app.route('/api/open-door', methods=['GET'])
def get_tasks():
    unlock()
    return "hello world"

if __name__ == '__main__':
    context = ('certkey/cert.pem', 'certkey/privkey.pem')
    app.run(host='0.0.0.0', ssl_context=context, debug=True)
