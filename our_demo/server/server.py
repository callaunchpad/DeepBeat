


import os
from flask import send_file

from flask import Flask
app = Flask(
    __name__, static_url_path='', static_folder=os.path.abspath('../static'))


@app.route('/', methods=['GET', 'POST'])
def index():
    return send_file('../static/index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
