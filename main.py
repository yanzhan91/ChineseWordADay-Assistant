import uuid

from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_word():
    return jsonify({
        "uid": uuid.uuid4(),
        "updateDate": datetime.today().strftime('%Y-%m-%dT00:00:00.0Z'),
        "titleText": "ChineseWordADay",
        "mainText": "",
        "streamUrl": "https://s3.amazonaws.com/chinese-word-a-day/%s.mp3" % datetime.today().strftime('%m%d%Y'),
        "redirectionUrl": "https://s3.amazonaws.com/chinese-word-a-day/redirect.html"
    })


if __name__ == '__main__':
    app.run()
