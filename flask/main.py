# Import necessary modules
from flask import Flask, request, redirect, url_for, jsonify
from redis import Redis
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO
import requests
from eventlet import monkey_patch
monkey_patch()

app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')
socketio = SocketIO(app, cors_allowed_origins='*', logger=True, engineio_logger=True)
redis = Redis(host='redis', port=6379, decode_responses=True, charset="utf-8")

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({'error': 'Invalid request. Missing required fields.'}), 400

        username = data['username']
        password = data['password']

        cachedUser = redis.get(username)
        if(cachedUser):
            socketio.emit('wsresponse', {"name": cachedUser, "source": "redis"})
            return jsonify({"name": cachedUser, "source": "redis"})

        form_data = {
            'username': username,
            'password': password
        }
        response = requests.post('http://fastapi:8000/login', data=form_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        if response.status_code == 200:
            data = response.json()
            token = data["access_token"]
            userRequest = requests.get('http://fastapi:8000/userInfo', headers={'Authorization': f'Bearer {token}'})
            if(userRequest.status_code == 200):
                userData = userRequest.json()
                redis.set(userData['username'], userData['name'])
                socketio.emit('wsresponse', {"name": userData['name'], "source": "postgresql"})
                return jsonify({"name": userData['name'], "source": "postgresql"})
        else:
            return jsonify("invalid credentiasl", 400)

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0", port=5420)
