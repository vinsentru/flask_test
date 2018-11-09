import logging
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world(methods=['GET', 'POST']):
    """
    Request handler
    """

    timestamp = datetime.now().strftime('%m-%d-%Y %I:%M:%S %p')

    app.logger.debug('{} {}'.format(timestamp, request.url))

    if request.method == 'GET':
        if request.headers.get('Accept') == 'application/json':
            return jsonify({"message": "Good morning"})
        else:
            return '<p>Hello, World</p>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
