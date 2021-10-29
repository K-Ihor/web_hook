from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def foo():
    data = json.loads(request.data)
    print(f"#############################################/n{data}/n########################")
    print("New commit by: {}".format(data['commits'][0]['author']['name']))
    print("####  OK  #####")
    return "OK"


if __name__ == "__main__":
    app.run()