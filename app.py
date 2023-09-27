# Import necessary modules from the Flask and Redis libraries
from flask import Flask, render_template, jsonify, request
from redis import Redis
import timeit
import math

# Initialize the Flask application
app = Flask(__name__)

# Initialize a Redis client to connect to a local Redis server
redis = Redis(host='localhost', port=6379, decode_responses=True)

# Define the root route for the web application
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

# A slow calculation function that simulates time-consuming operations
def slow_calculation():
    return sum(math.sqrt(i) for i in range(1, 1000000))

# A fast calculation function that uses Redis caching to speed up operations
def fast_calculation():
    # Check if the result exists in the Redis cache
    result = redis.get('my_key')
    if result is None:
        # If not, perform the calculation and save it to the cache
        result = sum(math.sqrt(i) for i in range(1, 1000000))
        redis.set('my_key', result)
    else:
        # Convert the cached result to a float
        result = float(result)
    return result

# Define the /fast route
@app.route('/fast')
def fast_route():
    # Measure the time taken for the fast calculation using timeit
    elapsed_time = timeit.timeit('fast_calculation()', globals=globals(), number=1)
    result = fast_calculation()
    return {"result": f"Result {result}", "source": "Redis", "time": f"{elapsed_time:.6f} seconds"}

# Define the /slow route
@app.route('/slow')
def slow_route():
    # Measure the time taken for the slow calculation using timeit
    elapsed_time = timeit.timeit('slow_calculation()', globals=globals(), number=1)
    result = slow_calculation()
    return {"result": f"Result {result}", "source": "Python", "time": f"{elapsed_time:.6f} seconds"}

# Define the /lists route to demonstrate Redis Lists
@app.route('/lists')
def redis_lists():
    # Add elements to a Redis list using LPUSH and RPUSH
    redis.lpush('my_list', 'a')
    redis.lpush('my_list', 'b')
    redis.lpush('my_list', 'c')
    redis.rpush('my_list', 'x')

    # Retrieve elements from the Redis list using LRANGE
    elements = redis.lrange('my_list', 0, -1)
    return elements

# Define the /hashset route to demonstrate Redis HashSets
@app.route('/hashset')
def redis_hashsets():
    # Set fields in a Redis hash using HSET
    redis.hset('my_hash', 'key', 'value')
    redis.hset('my_hash', 'name', 'John')

    # Retrieve fields from the Redis hash using HGET
    value1 = redis.hget('my_hash', 'key')
    value2 = redis.hget('my_hash', 'name')
    return {"value1": value1, "value2": value2}

# Define the /count route to demonstrate Redis counters
@app.route('/count')
def page_view():
    # Increment the pageview count using Redis INCR
    redis.incr('pageview_count')
    return {"pageviews": redis.get('pageview_count')}

# Define the /flush route to clear the Redis cache
@app.route('/flush')
def flush():
    # Flush the current Redis database using FLUSHDB
    redis.flushdb()
    return "flushed"

# Start the Flask development server
if __name__ == '__main__':
    app.run(debug=True)
