from flask import Flask
#from unlocker import unlock

app = Flask(__name__)

@app.route('/api/open-door', methods=['GET'])
def get_tasks():
    #unlock()
    return "hello world"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
