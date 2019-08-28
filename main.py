import uuid

from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_word():
    url = "https://s3.amazonaws.com/chinese-word-a-day/%s.mp3" % datetime.today().strftime('%m%d%Y')
    json = {
        'payload': {
            'google': {
                'expectUserResponse': False,
                'richResponse': {
                    'items': [
                        {
                            'simpleResponse': {
                                'textToSpeech': '<speak><audio src="%s"></audio></speak>' % url
                            }
                        }
                    ]
                }
            }
        }
    }
    return jsonify(json)


if __name__ == '__main__':
    app.run()
