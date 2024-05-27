import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    FOO = os.getenv('FOO', "a value for FOO does not exist")
    return f'Hello, World! The value of the env var FOO is {FOO}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)