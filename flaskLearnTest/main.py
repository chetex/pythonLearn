# This is a sample Python script.

# Press ⇧⌘F11 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Hola, Mundo!'

if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
