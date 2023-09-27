from flask import Flask, render_template, jsonify, request
from redis import Redis
import timeit
import math

app = Flask(__name__)
redis = Redis(host='localhost', port=6379, decode_responses=True)

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


# Redis can be used for Real Time analytics like tracking page views
@app.route('/pageview')
def page_view():
    redis.incr('pageview_count')
    return {"pageviews": redis.get('pageview_count')}


if __name__ == '__main__':
    app.run(debug=True)

# come back and add working with lists and dictionaries