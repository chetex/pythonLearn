# Import flask library
from flask import Flask

# Create a flask app
app = Flask(__name__)

# Define a route
@app.route('/')
def hello_world():
    return 'This is a new Flask test!'

# Define a route
@app.route('/spain')
def hello_spain():
    return 'This is a new Flask spain!'

if __name__ == '__main__':
    app.run(debug=True)
