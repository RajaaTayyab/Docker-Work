from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello_world():
    r.incr('hits')
    return f"This page is using Redis and has been visited {r.get('hits')} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
