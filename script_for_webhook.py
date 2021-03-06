import os

from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def foo():
    data = json.loads(request.data)
    print(f"#############################################/n{data}/n########################")
    print("New commit by: {}".format(data['commits'][0]['author']['name']))
    print("####  OK  #####")
    os.system('pkill -F HUP /var/run/gunicorn.pid')
    return "OK"


@app.route('/reload')
def reload():
    return 'Hello World!'





if __name__ == "__main__":
    app.run()
