import os
import jwt
import base64


from flask import Flask
from flask import request, jsonify, _request_ctx_stack
from flask_cors import cross_origin
from werkzeug.local import LocalProxy
from functools import wraps
#from unlocker import unlock

app = Flask(__name__)


app.secret_key = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'


# Authentication annotation
current_user = LocalProxy(lambda: _request_ctx_stack.top.current_user)



# Authentication attribute/annotation
def authenticate(error):
    resp = jsonify(error)
    resp.status_code = 401
    return resp





def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization', None)
        if not auth:
            return authenticate({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'})
        parts = auth.split()
        if parts[0].lower() != 'bearer':
            return {'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}
        elif len(parts) == 1:
            return {'code': 'invalid_header', 'description': 'Token not found'}
        elif len(parts) > 2:
            return {'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}
        token = parts[1]
        try:
            payload = jwt.decode(
                token,
                base64.b64decode('Xof5C1goOo-9_jszdP5rYWJFEAHlUQoQaibB_1vPul1_nYVp83qQwYc1eOIm9gfA'.replace("_","/").replace("-","+")),
                audience='JGYrHw8RuZQfKsIHt0ozaTEJaXQaZRdn'
            )
        except jwt.ExpiredSignature:
            return authenticate({'code': 'token_expired', 'description': 'token is expired'})
        except jwt.InvalidAudienceError:
            return authenticate({'code': 'invalid_audience', 'description': 'incorrect audience, expected: JGYrHw8RuZQfKsIHt0ozaTEJaXQaZRdn'})
        except jwt.DecodeError:
            return authenticate({'code': 'token_invalid_signature', 'description': 'token signature is invalid'})
        _request_ctx_stack.top.current_user = user = payload
        return f(*args, **kwargs)
    return decorated




# Page to trigger the door-opening function
@app.route('/api/open-door', methods=['GET'])
@cross_origin(headers=['Content-Type','Authorization'])
@requires_auth
def get_tasks():
    #unlock()
    return "hello world"


 


if __name__ == '__main__':
    context = ('certkey/cert.pem', 'certkey/privkey.pem')
    app.run(host='0.0.0.0', ssl_context=context, debug=True)


i
