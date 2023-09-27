# Import necessary modules
from flask import Flask, render_template, jsonify, request
from redis import Redis
import timeit
import math
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

# Initialize Flask app
app = Flask(__name__)

# Initialize Redis instance
# Connect to Redis server running on localhost at port 6379
redis = Redis(host='localhost', port=6379, decode_responses=True)

# Configure SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'

# Configure flask-caching to use Redis
# CACHE_TYPE specifies the backend to use, in this case, Redis.
# CACHE_REDIS_URL specifies the URL to connect to the Redis server.
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'

# Initialize SQLAlchemy and Cache instances
db = SQLAlchemy(app)
cache = Cache(app)

# Define User model for SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }

# Create tables and add a test user.
# This function is meant to be run in the Flask shell
def create_tables():
    db.create_all()
    new_user = User(username="john")
    db.session.add(new_user)
    db.session.commit()

# Memoize the get_user_from_db function with a 60-second timeout
# This means that returned values are cached for 60 seconds.
@cache.memoize(timeout=60)
def get_user_from_db(user_id):
    user = User.query.get(user_id)
    if user:
        return user.to_dict()
    return None

# Define a route for getting user data by ID
@app.route('/user/<int:user_id>')
def get_user(user_id):
    # get_user_from_db is called, but due to caching, if the data is already
    # in the cache, it will be returned without hitting the database.
    user_data = get_user_from_db(user_id)
    if user_data:
        return jsonify({"source": "database", "user": user_data})
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/')
def index():
    return render_template('index.html')

def slow_calculation():
    return sum(math.sqrt(i) for i in range(1, 1000000))

def fast_calculation():
    result = redis.get('my_key')
    if result is None:
        result = sum(math.sqrt(i) for i in range(1, 1000000))
        redis.set('my_key', result)
    else:
        result = float(result)
    return result

@app.route('/fast')
def fast_route():
    elapsed_time = timeit.timeit('fast_calculation()', globals=globals(), number=1)
    result = fast_calculation()
    return {"result": f"Result {result}", "source": "Redis", "time": f"{elapsed_time:.6f} seconds"}

@app.route('/slow')
def slow_route():
    elapsed_time = timeit.timeit('slow_calculation()', globals=globals(), number=1)
    result = slow_calculation()
    return {"result": f"Result {result}", "source": "Python", "time": f"{elapsed_time:.6f} seconds"}

@app.route('/lists')
def redis_lists():
    # Push elements to a list
    redis.lpush('my_list', 'a')
    redis.lpush('my_list', 'b')
    redis.lpush('my_list', 'c')
    redis.rpush('my_list', 'x')

    # Retrieve elements from a list
    elements = redis.lrange('my_list', 0, -1)
    print(elements) 
    return elements


@app.route('/hashset')
def redis_hashsets():
    # Set fields in a hash
    redis.hset('my_hash', 'key', 'value')
    redis.hset('my_hash', 'name', 'John')

    # Retrieve fields from a hash
    value1 = redis.hget('my_hash', 'key')
    value2 = redis.hget('my_hash', 'name')
    print(value1, value2)  
    return {"value1":value1,"value2":value2}

@app.route('/count')
def page_view():
    redis.incr('pageview_count')
    return {"pageviews": redis.get('pageview_count')}

@app.route('/flush')
def flush():
    redis.flushdb()
    return "flushed"



if __name__ == '__main__':
    app.run(debug=True)

