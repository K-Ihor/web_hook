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


def check_def(signal):
    if signal == "OK":
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%/nВсЁ ПОЛУЧИЛОСЬ/n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    else:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%/n ВСЕ ХЕРНЯ ДАВАЙ ПО НОВОЙ /n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


check_def(check_git_lab)


# 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


if __name__ == "__main__":
    app.run()