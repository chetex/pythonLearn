# Import flask library
from flask import Flask

# Create a flask app
app = Flask(__name__)

# Define a route
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)