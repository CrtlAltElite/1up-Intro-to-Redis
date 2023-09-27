
## Resource File: Python Packages in Flask-Redis Projects

### Flask

#### What it's used for:
Web framework for building web applications.

#### Official Documentation:
[Flask Documentation](https://flask.palletsprojects.com/en/latest/)

#### Methods/Functions/Classes Used:
- `Flask()`: Initializes the Flask application
- `@app.route()`: Route decorator for endpoints
- `render_template()`: Renders HTML templates
- `jsonify()`: Converts Python dictionaries to JSON objects
- `request`: To get request data

#### Example:
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!"
```

---

### SQLAlchemy

#### What it's used for:
SQL Toolkit and Object Relational Mapper (ORM) for Python.

#### Official Documentation:
[SQLAlchemy Documentation](https://www.sqlalchemy.org/)

#### Methods/Functions/Classes Used:
- `SQLAlchemy()`: Initializes the SQLAlchemy instance
- `db.Column()`: Defines a column in the database table
- `db.Model`: Base class for models

#### Example:
```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
```

---

### Redis

#### What it's used for:
In-memory data store for caching and other purposes.

#### Official Documentation:
[Redis-Py Documentation](https://redis-py.readthedocs.io/en/stable/)

#### Methods/Functions/Classes Used:

- `Redis(host='localhost', port=6379, decode_responses=True)`: Initializes the Redis client
  - Parameters:
    - `host`: Redis server address
    - `port`: Redis server port
    - `decode_responses`: Automatically decode Redis bytes to Python strings

  **Example:**
  ```python
  redis = Redis(host='localhost', port=6379, decode_responses=True)
  ```

- `get(key)`: Retrieves a value for a key
  - Parameters:
    - `key`: The key for which to fetch the value
  **Example:**
  ```python
  value = redis.get('my_key')
  ```

- `set(key, value)`: Sets a value for a key
  - Parameters:
    - `key`: The key to set
    - `value`: The value to set
  **Example:**
  ```python
  redis.set('my_key', 'my_value')
  ```

- `lpush(key, *values)`: Inserts values at the head of the list stored at key
  - Parameters:
    - `key`: The list key
    - `*values`: The values to insert
  **Example:**
  ```python
  redis.lpush('my_list', 'a', 'b')
  ```

- `rpush(key, *values)`: Inserts values at the tail of the list stored at key
  - Parameters:
    - `key`: The list key
    - `*values`: The values to insert
  **Example:**
  ```python
  redis.rpush('my_list', 'z')
  ```

- `hset(name, key, value)`: Sets field in the hash stored at name to value
  - Parameters:
    - `name`: The hash name
    - `key`: The field key
    - `value`: The field value
  **Example:**
  ```python
  redis.hset('my_hash', 'name', 'John')
  ```

- `hget(name, key)`: Retrieves the value at `key` in the hash at `name`
  - Parameters:
    - `name`: The hash name
    - `key`: The field key
  **Example:**
  ```python
  value = redis.hget('my_hash', 'name')
  ```

- `incr(name)`: Increments the value at `name` by 1
  - Parameters:
    - `name`: The counter name
  **Example:**
  ```python
  redis.incr('pageview_count')
  ```

---

### Flask-Caching

#### What it's used for:
Adds caching support to Flask.

#### Official Documentation:
[Flask-Caching Documentation](https://flask-caching.readthedocs.io/en/latest/)

#### Methods/Functions/Classes Used:

- `Cache(config)`: Initializes the Cache instance
  - Parameters:
    - `config`: A dictionary containing cache configurations
  **Example:**
  ```python
  cache = Cache(config={'CACHE_TYPE': 'redis'})
  ```

- `@cache.memoize(timeout=60)`: Memoizes function results
  - Parameters:
    - `timeout`: The time in seconds to cache the result (default is 300 seconds), after this time the cached result will be discarded.
  **Example:**
  ```python
  @cache.memoize(timeout=60)
  def get_user_from_db(user_id):
      user = User.query.get(user_id)
      return user.to_dict() if user else None
  ```



